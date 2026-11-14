# GeneWeaver - DNA Sequence Utilities

# Valid DNA bases
VALID_BASES = set("ATGCN")


def normalize_sequence(sequence: str) -> str:
    """
    Remove whitespace and convert DNA sequence to uppercase.
    """
    return "".join(sequence.split()).upper()