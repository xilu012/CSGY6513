import sys
import re

# Read the input text one line at a time
for line in sys.stdin:

    # Convert all letters to lowercase
    # so uppercase and lowercase words are counted together
    line = line.lower()

    # Find valid words in the line
    # This removes punctuation and numbers,
    # splits hyphenated words, and keeps internal apostrophes
    words = re.findall(r"[a-z]+(?:'[a-z]+)*", line)

    # Process each valid word
    for word in words:

        # Get the first letter of the word
        first_letter = word[0]

        # Output the starting letter with a count of 1
        print(f"{first_letter}\t1")
