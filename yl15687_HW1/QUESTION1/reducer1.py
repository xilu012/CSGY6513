import sys

top = []
current_word = None
count = 0

def keep_word(word, frequency):
    top.append((word, frequency))
    top.sort(key=lambda item: (-item[1], item[0]))
    del top[10:]

for line in sys.stdin:
    word, value = line.rstrip("\n").split("\t", 1)

    if word != current_word:
        if current_word is not None:
            keep_word(current_word, count)
        current_word = word
        count = 0

    count += int(value)

if current_word is not None:
    keep_word(current_word, count)

print("Word\tFrequency")
for word, frequency in top:
    print(f"{word}\t{frequency}")