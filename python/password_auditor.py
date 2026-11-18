
import getpass
import string

def check_password(password):

    score = 0
    feedback = []

    # Check password length
    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Use at least 12 characters.")

    # Check uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Check lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Check numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add numbers.")

    # Check special characters
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add special characters.")

    print("\n--- PASSWORD AUDIT ---")
    print(f"Score: {score}/5")

    if score == 5:
        print("Result: Meets basic complexity checks.")
    elif score >= 3:
        print("Result: Needs improvement.")
    else:
        print("Result: Weak password.")

    if feedback:
        print("\nRecommendations:")
        for item in feedback:
            print(f"- {item}")


if __name__ == "__main__":
    password = getpass.getpass("Enter a test password: ")
    check_password(password)

#python3 password_auditor.py

