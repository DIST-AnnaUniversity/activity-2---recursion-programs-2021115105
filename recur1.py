def number(a, b):
    if a == b:
        print(a)
        return
    else:
        print(a, end="\n")
        return number(a+2, b)

number(0, 10)
