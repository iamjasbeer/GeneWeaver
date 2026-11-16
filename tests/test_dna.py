import pytest
from app.dna import validate_dna, gc_content

def test_validate_dna():
    assert validate_dna("ATGCN")

def test_validate_dna_invalid():
    assert not validate_dna("ATGX")

def test_gc_content():
    assert gc_content("GGCCAT") == 66.66666666666666
