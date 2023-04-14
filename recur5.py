def number(a, b):
    if a == b:
        print(a)
        return
    else:
        print(a, end="\n")
        return number(a+6, b)

number(1,25)
     
