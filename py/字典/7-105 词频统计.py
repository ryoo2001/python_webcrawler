import sys

s = sys.stdin.read()
s = s[:s.find("#")]
for i in s:
    if i.isalnum() == False and i != "_":
        s = s.replace(i, "")
words1 = s.lower().split()
words2 = {}
for i in words1:
    i = i[:15]
    words2[i] = words2.get(i, 0) + 1
words3 = sorted(words2.items(), key=lambda x: (-x[1], x[0]))
print(len(words3))
num = int(len(words3) / 10)
for i in range(num):
    print(str(words3[i][1])+":"+str(words3[i][0]))