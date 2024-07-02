import datetime

t = int(input())
for i in range(t):
    time = input()
    time = datetime.datetime.strptime(time, "%Y-%m-%d")
    time = time + datetime.timedelta(days=-1)
    print(str(time).split(" ")[0])
