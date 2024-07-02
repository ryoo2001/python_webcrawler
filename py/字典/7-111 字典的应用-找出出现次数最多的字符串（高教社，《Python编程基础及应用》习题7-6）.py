words = []
while True:
    words1 = input()
    words2 = map(str, words1.split())
    if words1 == "q":
        break
    for i in words2:
        words.append(i)
words3 = {}
for i in words:
    words3[i] = words3.get(i, 0) + 1
px = sorted(words3.items(), key=lambda x: -x[1])
print(*px[0])