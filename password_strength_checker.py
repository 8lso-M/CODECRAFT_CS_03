import getpass
import re

COMMON_PASSWORDS = {
    "123456",
    "password",
    "123456789",
    "12345678",
    "12345",
    "qwerty",
    "abc123",
    "football",
    "monkey",
    "letmein",
    "welcome",
    "admin",
    "iloveyou",
    "sunshine",
    "princess",
}


def check_password_strength(password):
    """Evaluate password strength and return a score with feedback."""
    if not password:
        return {
            "score": 0,
            "category": "Very Weak",
            "feedback": ["Password cannot be empty."],
        }

    length = len(password)
    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_symbol = bool(re.search(r"[^A-Za-z0-9]", password))
    has_space = " " in password
    types = sum([has_lower, has_upper, has_digit, has_symbol])

    score = 0
    feedback = []

    # Length points.
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1

    # Character variety.
    score += types

    # Penalties.
    if has_space:
        score -= 1
    if password.lower() in COMMON_PASSWORDS:
        score -= 2
    if len(set(password)) <= max(2, length // 3):
        score -= 1
    if re.search(r"(.)\1{2,}", password):
        score -= 1
    if re.search(r"(?:abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz|123|234|345|456|567|678|789|890)", password.lower()):
        score -= 1

    score = max(0, min(score, 5))

    if length < 8:
        feedback.append("Use at least 8 characters. Longer passwords are usually stronger.")
    elif length < 12:
        feedback.append("Use 12 or more characters for better security.")

    if not has_lower:
        feedback.append("Add lowercase letters.")
    if not has_upper:
        feedback.append("Add uppercase letters.")
    if not has_digit:
        feedback.append("Add digits.")
    if not has_symbol:
        feedback.append("Add symbols like !@#$%^&* to make it harder to guess.")
    if has_space:
        feedback.append("Avoid spaces in passwords for compatibility and consistency.")
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("This password is too common. Try a unique phrase instead.")
    if re.search(r"(.)\1{2,}", password):
        feedback.append("Avoid repeating the same character multiple times.")
    if re.search(r"(?:abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz|123|234|345|456|567|678|789|890)", password.lower()):
        feedback.append("Avoid obvious sequences like 'abc' or '123'.")

    if not feedback:
        feedback.append("Great password! It has good length and strong character variety.")

    categories = {
        0: "Very Weak",
        1: "Weak",
        2: "Weak",
        3: "Moderate",
        4: "Strong",
        5: "Very Strong",
    }

    return {
        "score": score,
        "category": categories[score],
        "feedback": feedback,
    }


def format_feedback(result):
    output = [f"Strength: {result['category']} ({result['score']}/5)", "Feedback:"]
    output.extend(f"- {item}" for item in result["feedback"])
    return "\n".join(output)


def main():
    print("--- PASSWORD STRENGTH CHECKER ---")
    password = getpass.getpass("Enter password to check: ")
    result = check_password_strength(password)
    print("\n" + format_feedback(result))


if __name__ == "__main__":
    main()