def ready(stu):
    print("Teacher: Hi everyone, are you ready?")
    for i in range(len(stu)):
        print(stu[i], " ".join(["I'm ready!"] * (i + 1)), sep=": ")
    print("Teacher: OK! Let's start our exam.")


ready(input().split())
