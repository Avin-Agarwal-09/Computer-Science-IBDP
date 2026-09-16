"""Topic 10 - File handling.

Modes:  "r" read (error if missing)   "w" write (ERASES existing content)
        "a" append                    "x" create (error if it exists)

Always use `with open(...)` - it closes the file automatically, even if an
error is raised partway through. Lines read from a file keep their trailing
newline, so .strip() before converting to int.

This script writes its own sample data into examples/data/ so it runs anywhere.
"""

import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

SAMPLE_SCORES = """S001,82
S002,64
S003,47
S004,91
S005,55
S006,38
"""


def setup_sample_data():
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(os.path.join(DATA_DIR, "scores.txt"), "w") as file:
        file.write(SAMPLE_SCORES)


def path(filename):
    return os.path.join(DATA_DIR, filename)


def read_all_lines(filename):
    with open(path(filename), "r") as file:
        return [line.strip() for line in file if line.strip() != ""]


def count_lines(filename):
    count = 0
    with open(path(filename), "r") as file:
        for _ in file:
            count += 1
    return count


def read_scores(filename):
    """Parse 'id,score' records into a list of (id, score) pairs."""
    records = []
    for line in read_all_lines(filename):
        student_id, score = line.split(",")
        records.append((student_id, int(score)))
    return records


def split_by_grade(records):
    """Write three output files in one pass over the data."""
    with open(path("distinction.txt"), "w") as distinction, \
         open(path("pass.txt"), "w") as passed, \
         open(path("fail.txt"), "w") as failed:

        for student_id, score in records:
            if score >= 70:
                distinction.write(f"{student_id},{score}\n")
            elif score >= 50:
                passed.write(f"{student_id},{score}\n")
            else:
                failed.write(f"{student_id},{score}\n")


def write_summary(records, filename):
    scores = [score for _, score in records]
    average = sum(scores) / len(scores)

    with open(path(filename), "w") as file:
        file.write(f"Students: {len(scores)}\n")
        file.write(f"Highest:  {max(scores)}\n")
        file.write(f"Lowest:   {min(scores)}\n")
        file.write(f"Average:  {average:.1f}\n")


def append_line(filename, text):
    with open(path(filename), "a") as file:
        file.write(text + "\n")


def find_record(filename, student_id):
    """Search a file line by line without loading it all into memory."""
    with open(path(filename), "r") as file:
        for line in file:
            if line.startswith(student_id + ","):
                return line.strip()
    return None


def read_or_create(filename, default_text):
    """Handle a missing file instead of crashing."""
    try:
        with open(path(filename), "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        with open(path(filename), "w") as file:
            file.write(default_text)
        return default_text


def run_counter(filename):
    """A persistent counter: read the old value, add one, write it back."""
    try:
        with open(path(filename), "r") as file:
            runs = int(file.read().strip())
    except (FileNotFoundError, ValueError):
        runs = 0

    runs += 1
    with open(path(filename), "w") as file:
        file.write(str(runs))
    return runs


if __name__ == "__main__":
    setup_sample_data()

    records = read_scores("scores.txt")
    print("Records read:   ", len(records))
    print("Lines in file:  ", count_lines("scores.txt"))

    split_by_grade(records)
    print("Distinctions:   ", read_all_lines("distinction.txt"))
    print("Passes:         ", read_all_lines("pass.txt"))
    print("Fails:          ", read_all_lines("fail.txt"))

    write_summary(records, "summary.txt")
    print("\nSummary file:")
    for line in read_all_lines("summary.txt"):
        print("  ", line)

    append_line("scores.txt", "S007,73")
    print("\nAfter append:   ", len(read_scores("scores.txt")), "records")

    print("Find S004:      ", find_record("scores.txt", "S004"))
    print("Find S099:      ", find_record("scores.txt", "S099"))
    print("read_or_create: ", read_or_create("name.txt", "Avin"))
    print("Run number:     ", run_counter("runs.txt"))
