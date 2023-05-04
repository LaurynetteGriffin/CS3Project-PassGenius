def password_strengthener(password):
    # Check the length of the password
    if len(password) < 8:
        return "weak"

    # Check for uppercase, lowercase, digits and special characters
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True

    if has_uppercase and has_lowercase and has_digit and has_special:
        return "strong"
    else:
        return "medium"