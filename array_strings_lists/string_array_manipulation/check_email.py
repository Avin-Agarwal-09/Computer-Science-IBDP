def valid_email(email):
    if "@" not in email or "." not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2 or not parts[0] or not parts[1]:
        return False
    if "." not in parts[1]:
        return False
    return True

email = "student123@school.edu"
print(valid_email(email.strip()))
