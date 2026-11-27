from app.parser import parse_fasta
from app.cpu_engine import find_candidates


FASTA_FILE = "data/sample.fasta"

# Example guide sequence
GUIDE_SEQUENCE = "ATGCGT"

MAX_MISMATCHES = 2


def main():
    print("=" * 50)
    print("GeneWeaver - CRISPR Candidate Scanner")
    print("=" * 50)

    # Step 1: Read sequences from FASTA
    records = parse_fasta(FASTA_FILE)

    print(f"\nLoaded {len(records)} DNA sequence(s)\n")

    total_candidates = 0