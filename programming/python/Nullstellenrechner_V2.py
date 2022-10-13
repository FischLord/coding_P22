#Idee 
while True:
    a = float(input("a --> "))
    b = float(input("b --> "))
    c = float(input("c --> "))
    x = 0
    ns = []
    while not x >= 100:
        y = a*x**2+b*x+c
        if y == 0:
            ns.append(x)
        x = round(x,4) + round(.1,4)
        print(x,"|",y)
    x = 0
    while not x <= -100:
        y = a*x**2+b*x+c
        if y == 0:
            ns.append(x)
        x = round(x,4) - round(.1,4)
        print(x,"|",y)
    print(ns)