import sys

# Store the total number of books borrowed by each student
counts = {}

# Read mapper output one line at a time
for line in sys.stdin:

    # Remove extra whitespace
    line = line.strip()

    # Skip empty lines
    if not line:
        continue

    # Split the StudentID and count
    student_id, value = line.split("\t", 1)

    # Add the count to the corresponding student
    counts[student_id] = counts.get(student_id, 0) + int(value)

# Find the maximum number of books borrowed
max_count = 0

for count in counts.values():
    if count > max_count:
        max_count = count

# Store all students who have the maximum count
top_students = []

for student_id, count in counts.items():
    if count == max_count:
        top_students.append(student_id)

# Sort tied students by StudentID
top_students.sort()

# Print the output header
print("StudentID\tBooksBorrowed")

# Print the student or students with the maximum count
for student_id in top_students:
    print(f"{student_id}\t{max_count}")