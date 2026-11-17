
from Bio import SeqIO
from app.dna import normalize_dna


def parse_fasta(file_path):
    """
    Read DNA sequences from a FASTA file.

    Args:
        file_path: Path to FASTA file.

    Returns:
        List of dictionaries containing sequence IDs and DNA.
    """

    sequences = []

    for record in SeqIO.parse(file_path, "fasta"):

        sequence = normalize_dna(str(record.seq))

        sequences.append({
            "id": record.id,
            "sequence": sequence
        })

    return sequences
