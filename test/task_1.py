from collections import Counter

line = input().split()
word_counts = Counter(line)

for word, count in sorted(word_counts.items()):
    print(f'{word}: {count}')
