import sys
word = sys.stdin.readline().strip()
smallest = None
for i in range(1, len(word) - 1):
    for j in range(i + 1,len(word)):
        f = word[:i]
        s = word[i:j]
        t = word[j:]
        new_word = f[::-1] + s[::-1] + t[::-1]
        if smallest is None or new_word < smallest:
            smallest = new_word
print(smallest)
