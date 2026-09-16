"""Topic 1 - Sequence, selection and iteration.

The three control structures every program is built from:
  sequence  - statements run top to bottom
  selection - if / elif / else chooses a branch
  iteration - for / while repeat a block
"""


def classify_bmi(weight_kg, height_m):
    """Selection: an if/elif chain where every branch is reachable."""
    bmi = weight_kg / (height_m * height_m)

    if bmi < 18.5:
        category = "underweight"
    elif bmi < 25:
        category = "normal"
    elif bmi < 30:
        category = "overweight"
    else:
        category = "obese"

    return bmi, category


def sum_to_n(n):
    """Definite iteration: a for loop with a known number of repetitions."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def times_table(number, up_to):
    """Nested iteration is just a loop inside a loop."""
    rows = []
    for i in range(1, up_to + 1):
        rows.append(f"{number} x {i} = {number * i}")
    return rows


def count_attempts(correct_pin, attempts):
    """Indefinite iteration: a while loop that stops on a condition."""
    tries = 0
    while tries < len(attempts):
        if attempts[tries] == correct_pin:
            return tries + 1
        tries += 1
    return -1


if __name__ == "__main__":
    bmi, category = classify_bmi(70, 1.75)
    print(f"BMI {bmi:.1f} -> {category}")

    print("Sum 1..10 =", sum_to_n(10))

    for row in times_table(7, 5):
        print(row)

    print("PIN found on attempt:", count_attempts("1234", ["0000", "9999", "1234"]))
    print("PIN never found:", count_attempts("1234", ["0000", "9999"]))
