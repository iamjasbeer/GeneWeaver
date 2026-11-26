
import pytest

from app.cpu_engine import has_valid_pam, find_candidates


def test_valid_pam():
    assert has_valid_pam("AGG")
    assert has_valid_pam("TGG")


def test_invalid_pam():
    assert not has_valid_pam("ATA")
    assert not has_valid_pam("GGA")


def test_find_candidate_with_pam():
    sequence = "ATGCGTAGG"
    guide = "ATGCGT"

    results = find_candidates(sequence, guide)

    assert len(results) == 1
    assert results[0]["start"] == 0
    assert results[0]["end"] == 6
    assert results[0]["sequence"] == "ATGCGT"
    assert results[0]["mismatches"] == 0


def test_candidate_with_mismatch():
    sequence = "ATGCTTAGG"
    guide = "ATGCGT"

    results = find_candidates(
        sequence,
        guide,
        max_mismatches=1
    )

    assert len(results) == 1
    assert results[0]["mismatches"] == 1


def test_reject_too_many_mismatches():
    sequence = "TTGCTTAGG"
    guide = "ATGCGT"

    results = find_candidates(
        sequence,
        guide,
        max_mismatches=1
    )

    assert results == []


def test_empty_guide():
    with pytest.raises(ValueError):
        find_candidates("ATGCGTAGG", "")


def test_negative_mismatch_limit():
    with pytest.raises(ValueError):
        find_candidates("ATGCGTAGG", "ATGCGT", -1)
