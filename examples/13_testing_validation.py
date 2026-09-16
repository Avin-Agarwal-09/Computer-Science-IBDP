"""Topic 13 - Testing and validation.

Validation checks data is REASONABLE before you use it:
  range check    is it between sensible limits?
  type check     is it the right data type?
  length check   is it the right number of characters?
  format check   does it follow the required pattern?
  presence check is it there at all?

Test data comes in three kinds - a question almost always asks for all three:
  normal     clearly inside the accepted range        (age 25)
  boundary   exactly on the limit, and just past it   (age 0, 150, 151)
  erroneous  the wrong type or shape entirely         (age "abc")
"""


def validate_age(value):
    """Type check then range check. Order matters - cast before comparing."""
    try:
        age = int(value)
    except (ValueError, TypeError):
        return False, "Age must be a whole number"

    if age < 0 or age > 150:
        return False, "Age must be between 0 and 150"

    return True, "Valid"


def validate_email(email):
    if "@" not in email:
        return False, "Email must contain '@'"
    if "." not in email.split("@")[-1]:
        return False, "Email domain must contain '.'"
    if email.startswith("@") or email.endswith("@"):
        return False, "Email is missing a name or domain"
    return True, "Valid"


def validate_phone(phone):
    if not phone.isdigit():
        return False, "Phone must contain digits only"
    if len(phone) != 10:
        return False, "Phone must be exactly 10 digits"
    return True, "Valid"


def validate_password(password):
    """A presence check for each required character class."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters"

    has_upper = False
    has_lower = False
    has_digit = False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    if not has_upper:
        return False, "Password needs an uppercase letter"
    if not has_lower:
        return False, "Password needs a lowercase letter"
    if not has_digit:
        return False, "Password needs a digit"

    return True, "Valid"


def check_pin(correct_pin, attempts, max_attempts=3):
    """Limiting attempts stops brute-force guessing."""
    for i, attempt in enumerate(attempts):
        if i >= max_attempts:
            return False, "Account locked - too many attempts"
        if attempt == correct_pin:
            return True, f"Accepted on attempt {i + 1}"
    return False, "PIN not matched"


def run_tests(name, function, cases):
    """A test harness: run each case and compare against the expected result."""
    print(f"\n{name}")
    passed = 0

    for value, expected, kind in cases:
        actual, message = function(value)
        status = "PASS" if actual == expected else "FAIL"
        if actual == expected:
            passed += 1
        print(f"  [{status}] {kind:9} {str(value):24} -> {message}")

    print(f"  {passed}/{len(cases)} tests passed")


if __name__ == "__main__":
    run_tests("validate_age", validate_age, [
        (25, True, "normal"),
        (0, True, "boundary"),
        (150, True, "boundary"),
        (-1, False, "boundary"),
        (151, False, "boundary"),
        ("abc", False, "erroneous"),
        ("", False, "erroneous"),
    ])

    run_tests("validate_email", validate_email, [
        ("avin@school.edu", True, "normal"),
        ("a@b.co", True, "boundary"),
        ("avin.school.edu", False, "erroneous"),
        ("@school.edu", False, "boundary"),
        ("avin@school", False, "erroneous"),
    ])

    run_tests("validate_phone", validate_phone, [
        ("0412345678", True, "normal"),
        ("041234567", False, "boundary"),
        ("04123456789", False, "boundary"),
        ("0412 34567", False, "erroneous"),
    ])

    run_tests("validate_password", validate_password, [
        ("Passw0rdX", True, "normal"),
        ("Pass123", False, "boundary"),
        ("password1", False, "erroneous"),
        ("PASSWORD1", False, "erroneous"),
        ("PasswordX", False, "erroneous"),
    ])

    print("\ncheck_pin")
    print("  ", check_pin("1234", ["0000", "1234"]))
    print("  ", check_pin("1234", ["0000", "1111", "2222", "1234"]))
