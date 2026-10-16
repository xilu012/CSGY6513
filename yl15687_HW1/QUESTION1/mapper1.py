import re
import sys

for line in sys.stdin:
    for word in re.findall(r"[A-Za-z]+", line):
        print(f"{word.lower()}\t1")
