try:
    A = int(input())
    if A == 0:
        print("算术错误，您不能输入0")
    else:
        print(f"""20除以{A}的结果是: {20 / A:.2f}
没有出现异常""")
except:
    print("值错误，您必须输入数值")
