import re

def check_password_strength(password):
    # Criteria definitions
    length_error = len(password) < 8
    digit_error = not re.search(r"\d", password)
    uppercase_error = not re.search(r"[A-Z]", password)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    # Score calculation
    score = 0
    if not length_error: score += 1
    if not digit_error: score += 1
    if not uppercase_error: score += 1
    if not special_char_error: score += 1

    # Feedback based on score
    if score == 4:
        return "Strong", "Your password is secure."
    elif score >= 2:
        return "Moderate", "Consider adding more variety (numbers/special chars)."
    else:
        return "Weak", "Password needs at least 8 chars, 1 digit, 1 uppercase, and 1 special char."

if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    strength, message = check_password_strength(pwd)
    print(f"Strength: {strength}\nFeedback: {message}")
