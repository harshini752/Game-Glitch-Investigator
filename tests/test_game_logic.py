import sys
sys.path.insert(0, '.')

from logic_utils import check_guess

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

# Bug 2: check_guess must return a (outcome, message) tuple,
# and the message must guide the player in the correct direction.
def test_check_guess_returns_tuple():
    # check_guess should return a 2-tuple (outcome, message)
    result = check_guess(50, 50)
    assert isinstance(result, tuple) and len(result) == 2, (
        "check_guess should return a (outcome, message) tuple"
    )

def test_too_high_message_says_lower():
    # Bug 2: when guess > secret, message incorrectly says "Go HIGHER!" instead of "Go LOWER!"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "lower" in message.lower(), (
        f"Expected hint to say 'lower' when guess is too high, got: '{message}'"
    )

def test_too_low_message_says_higher():
    # Bug 2: when guess < secret, message incorrectly says "Go LOWER!" instead of "Go HIGHER!"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "higher" in message.lower(), (
        f"Expected hint to say 'higher' when guess is too low, got: '{message}'"
    )
