import pytest
from app.parser import parse_fasta

def test_parse_fasta(tmp_path):
    # Create a temporary FASTA file
    fasta_content = """>seq1
                     ATGCATGC
                     >seq2
                    TGCATGCA
                    """
    fasta_file = tmp_path / "test.fasta"
    fasta_file.write_text(fasta_content)
    result = parse_fasta(fasta_file)
    assert len(result) == 2
    assert result[0].id == "seq1"
    assert result[0].sequence == "ATGCATGC"
    assert result[1].id == "seq2"
    assert result[1].sequence == "TGCATGCA"