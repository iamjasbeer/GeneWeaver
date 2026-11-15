# GeneWeaver - DNA Sequence Utilities

# Valid DNA bases
VALID_BASES = set("ATGCN")


def normalize_sequence(sequence: str) -> str:
    """
    Remove whitespace and convert DNA sequence to uppercase.
    """
    return "".join(sequence.split()).upper()

def validate_dna(sequence: str, allow_n: bool = True) -> bool:
    """
    Check whether a DNA sequence contains valid bases.
    A, T, G, C are valid.
    N represents an unknown DNA base (optional).
    """
    sequence = normalize_sequence(sequence)

    valid = VALID_BASES if allow_n else set("ATGC")

    return bool(sequence) and all(
        base in valid for base in sequence
    )


def gc_content(sequence: str) -> float:
    """
    Calculate the percentage of G and C bases.
    """
    sequence = normalize_sequence(sequence)

    if not sequence:
        return 0.0

    gc_count = sequence.count("G") + sequence.count("C")

    return (gc_count / len(sequence)) * 100