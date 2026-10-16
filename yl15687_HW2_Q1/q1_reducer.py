import sys

# Store letter counts
letter_counts = {}

# Read mapper output
for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    # Get the letter and its count
    letter, count = line.split("\t")
    count = int(count)

    # Add to the total
    if letter in letter_counts:
        letter_counts[letter] += count
    else:
        letter_counts[letter] = count

# Sort by count in descending order
sorted_letters = sorted(
    letter_counts.items(),
    key=lambda item: item[1],
    reverse=True
)

# Print the Top 5 results
print("Letter\tCount")

for letter, count in sorted_letters[:5]:
    print(f"{letter}\t{count}")

