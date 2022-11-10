
def add(a,b):
    if a == b:
        return True
    else:
        return False

def hitInTheMiddle():
    global x,y
    x = int(input("x: "))
    y = int(input("y: "))


hitInTheMiddle()
while not add(x, y):
    hitInTheMiddle()
    print(x)
    print(y)

print("You hit in the middle!")


