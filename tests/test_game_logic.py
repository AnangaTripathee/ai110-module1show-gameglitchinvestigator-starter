from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

def test_hint_too_high_message():
    # Confirms the backwards hint bug is fixed: guess above secret tells you to go LOWER
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_secret_always_integer():
    # Confirms the string conversion bug is fixed: integer secret compares correctly
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_secret_not_converted_to_string():
    # Targets the string conversion bug: 60 > 50 numerically, but "60" < "50" as strings.
    # A correct integer comparison must return "Too High", not a wrong string-comparison result.
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_even_attempt_secret_is_integer():
    # On what used to be even-numbered attempts the secret was stringified; with the fix,
    # integer comparison holds: 40 < 50 should tell the player to go HIGHER.
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")
