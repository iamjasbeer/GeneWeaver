import pytest
def test_count_mismatches():
    # Test case 1: Sequences with no mismatches
    seq_a = "ACGT"
    seq_b = "ACGT"
    assert count_mismatches(seq_a, seq_b) == 0

    # Test case 2: Sequences with some mismatches
    seq_a = "ACGT"
    seq_b = "AGCT"
    assert count_mismatches(seq_a, seq_b) == 2

    # Test case 3: Sequences with all mismatches
    seq_a = "AAAA"
    seq_b = "TTTT"
    assert count_mismatches(seq_a, seq_b) == 4

    # Test case 4: Sequences of different lengths
    seq_a = "ACGT"
    seq_b = "ACGTA"
    with pytest.raises(ValueError):
        count_mismatches(seq_a, seq_b)