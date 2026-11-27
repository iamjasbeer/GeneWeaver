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