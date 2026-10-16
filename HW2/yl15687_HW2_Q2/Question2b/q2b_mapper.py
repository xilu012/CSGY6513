import sys

# Read the input file one line at a time
for line in sys.stdin:

    # Remove leading and trailing whitespace
    line = line.strip()

    # Skip blank lines
    if not line:
        continue

    # Skip invalid lines without a comma
    if "," not in line:
        continue

    # Split only on the first comma
    student_id, book_title = line.split(",", 1)

    # Remove extra spaces around both fields
    student_id = student_id.strip()
    book_title = book_title.strip()

    # Ignore records with missing StudentID or BookTitle
    if not student_id or not book_title:
        continue

    # Output the StudentID with a count of 1
    print(f"{student_id}\t1")