counts = {}

for i in range(5):
    word = input("Enter a word: ").strip().lower()
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts) 