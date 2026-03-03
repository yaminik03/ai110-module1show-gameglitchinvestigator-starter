import pytest
from app import update_score

def test_update_score_clamps_negative_single():
    # Decrements that would go negative should return 0
    assert update_score(0, "Too Low", 1) == 0
    assert update_score(0, "Too High", 1) == 0
    # small positive score decremented below zero clamps to 0
    assert update_score(3, "Too Low", 1) == 0

def test_update_score_clamps_negative_repeated():
    # Repeated decrements should never produce negative scores
    score = 3
    score = update_score(score, "Too Low", 1)  # becomes 0
    assert score == 0
    score = update_score(score, "Too Low", 2)  # stays 0
    assert score == 0

def test_win_awards_minimum_points():
    # Very large attempt number would compute low/negative points, but minimum 10 should be applied
    result = update_score(0, "Win", 1000)
    assert result >= 10
