def count_mismatches(sequence_a, sequence_b):
    """
    Count differences between two DNA sequences.
    """

    if len(sequence_a) != len(sequence_b):
        raise ValueError("Sequences must have equal length")

    mismatches = 0

    for base_a, base_b in zip(sequence_a.upper(), sequence_b.upper()):
        if base_a != base_b:
            mismatches += 1

    return mismatches
