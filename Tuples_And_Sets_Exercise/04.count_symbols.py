occurrences = {}

for letter in input():
    if letter not in occurrences:
        occurrences[letter] = 0

    occurrences[letter] += 1

for letter, times in sorted(occurrences.items()):
    print(f"{letter}: {times} time/s")
