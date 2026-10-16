import re
import sys

for line in sys.stdin:
    for word in re.findall(r"[A-Za-z]+", line):
        word = word.lower()
        if word[0] in "aeiou":
            print(f"{word}\t1")
