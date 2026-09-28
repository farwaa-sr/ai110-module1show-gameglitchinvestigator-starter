from logic_utils import check_guess
from app import check_guess as check_guess_app

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

# Added tests using AI agent mode
def test_hint_direction_guess_below_secret():
    # Regression test for the reversed-hint bug: guessing below the
    # secret must tell the player to go HIGHER, not LOWER.
    _, message = check_guess_app(40, 50)
    assert "HIGHER" in message
    assert "LOWER" not in message

def test_hint_direction_guess_above_secret():
    # Regression test for the reversed-hint bug: guessing above the
    # secret must tell the player to go LOWER, not HIGHER.
    _, message = check_guess_app(60, 50)
    assert "LOWER" in message
    assert "HIGHER" not in message


