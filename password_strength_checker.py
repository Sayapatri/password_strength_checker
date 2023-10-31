import re

def is_password_strong(password):
    if len(password) < 8:
        return "Weak: Password is too short (minimum 8 characters)."
    if not any(c.isupper() for c in password) or not any(c.islower() for c in password):
        return "Weak: Use a mix of uppercase and lowercase characters."
    if not any(c.isdigit() for c in password):
        return "Weak: Include at least one digit."
    if not re.search(r'[!@#$%^&*()_+{}[\]:;<>,.?~\\\-]', password):
        return "Weak: Use at least one special character."
    return "Strong: Password meets security criteria"

user_password = input("Enter your password: ")
result = is_password_strong(user_password)
print("Password Strength:", result)
