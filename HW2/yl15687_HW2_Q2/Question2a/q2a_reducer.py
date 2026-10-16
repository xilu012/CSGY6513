import sys

# Store the total borrow count for each book
counts = {}

# Read mapper output one line at a time
for line in sys.stdin:

    # Remove extra whitespace
    line = line.strip()

    # Skip empty lines
    if not line:
        continue

    # Split the book title and count
    book, value = line.split("\t", 1)

    # Add the count to the corresponding book
    counts[book] = counts.get(book, 0) + int(value)

# Sort by count from highest to lowest
# If counts are equal, sort alphabetically by book title
results = sorted(
    counts.items(),
    key=lambda x: (-x[1], x[0])
)

# Print the output header
print("Book\tCount")

# Print only the Top 5 books
for book, count in results[:5]:

    # Display the book title in title case
    print(f"{book.title()}\t{count}")
