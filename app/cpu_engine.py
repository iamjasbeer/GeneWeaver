
from app.scoring import count_mismatches


def find_candidates(sequence, guide, max_mismatches=2):

    sequence = sequence.upper()
    guide = guide.upper()

    if not guide:
        raise ValueError("Guide sequence cannot be empty")

    if max_mismatches < 0:
        raise ValueError("Maximum mismatches cannot be negative")

    guide_length = len(guide)
    candidates = []

    # Sliding window matching
    for start in range(len(sequence) - guide_length + 1):

        end = start + guide_length

        # Extract DNA window
        window = sequence[start:end]

        # Calculate mismatches
        mismatches = count_mismatches(guide, window)

        # Check mismatch limit
        if mismatches <= max_mismatches:

            candidates.append({
                "start": start,
                "end": end,
                "sequence": window,
                "mismatches": mismatches
            })

    return candidates
