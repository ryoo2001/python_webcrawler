def e(error):
    a, b, c = 0, 1, 0
    while error <= 1 / b:
        a += 1 / b
        c += 1
        b *= c
    return a + 1 / b


print(e(float(input())))
