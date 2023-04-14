def number(a, b):
    if a == b:
        print(a)
        return
    else:
        print(a, end="")
        return number(a+3, b)

number(0, 15)
     
