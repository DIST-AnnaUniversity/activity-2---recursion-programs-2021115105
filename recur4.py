def number(a, b):
    if a == b:
        print(a)
        return
    else:
        print(a, end="")
        return number(3*a/4, b)

number(7,189/64)
     
