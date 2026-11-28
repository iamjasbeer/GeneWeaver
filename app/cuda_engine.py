import numpy as np
from numba import cuda


@cuda.jit
def scan_kernel(sequence, guide, output, guide_length,
                sequence_length, max_mismatches):

    # Each GPU thread handles one starting position
    start = cuda.grid(1)

    # Output has one slot per possible guide + PAM window
    if start >= output.size:
        return

    mismatches = 0

 # Compare the guide with this genome window
    for i in range(guide_length):
        if sequence[start + i] != guide[i]:
            mismatches += 1

            if mismatches > max_mismatches:
                break

    # Default: this position is not a candidate
    output[start] = 255

    # Check mismatch limit and PAM
    if mismatches <= max_mismatches:
        pam_start = start + guide_length

        pam_first = sequence[pam_start]
        pam_second = sequence[pam_start + 1]
        pam_third = sequence[pam_start + 2]

        # PAM pattern NGG, where N is A/T/G/C
        valid_first = (
            pam_first == 65 or
            pam_first == 84 or
            pam_first == 71 or
            pam_first == 67
        )

        if (
            valid_first
            and pam_second == 71
            and pam_third == 71
        ):
            output[start] = mismatches


def find_candidates_cuda(sequence, guide, max_mismatches=2):
    """
    GPU-based CRISPR candidate scanner.
    Returns candidate dictionaries similar to cpu_engine.py.
    """

    sequence = sequence.upper()
    guide = guide.upper()

    if not guide:
        raise ValueError("Guide sequence cannot be empty")

    if max_mismatches < 0:
        raise ValueError("Maximum mismatches cannot be negative")

    if not cuda.is_available():
        raise RuntimeError(
            "CUDA GPU is not available. Check NVIDIA GPU and drivers."
        )

    guide_length = len(guide)
    sequence_length = len(sequence)

    # Number of windows containing guide + 3-base PAM
    n_windows = sequence_length - guide_length - 2

    if n_windows <= 0:
        return []

    # Convert DNA strings into ASCII uint8 arrays
    sequence_array = np.frombuffer(
        sequence.encode("ascii"),
        dtype=np.uint8
    )

    guide_array = np.frombuffer(
        guide.encode("ascii"),
        dtype=np.uint8
    )

    # Copy input arrays to GPU memory
    d_sequence = cuda.to_device(sequence_array)
    d_guide = cuda.to_device(guide_array)

    # Allocate GPU output array
    d_output = cuda.device_array(
        n_windows,
        dtype=np.uint8
    )

    threads_per_block = 128
    blocks_per_grid = (
        n_windows + threads_per_block - 1
    ) // threads_per_block

    # Launch GPU kernel
    scan_kernel[
        blocks_per_grid,
        threads_per_block
    ](
        d_sequence,
        d_guide,
        d_output,
        guide_length,
        sequence_length,
        max_mismatches
    )

    # Copy results from GPU to CPU
    mismatch_results = d_output.copy_to_host()

    candidates = []

    for start, mismatches in enumerate(mismatch_results):
        if mismatches == 255:
            continue

        end = start + guide_length
        target = sequence[start:end]
        pam = sequence[end:end + 3]

        candidates.append({
            "start": start,
            "end": end,
            "sequence": target,
            "pam": pam,
            "mismatches": int(mismatches),
            "score": guide_length - int(mismatches)
        })

    return candidates