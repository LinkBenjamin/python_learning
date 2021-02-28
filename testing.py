def factorial(x):
    if x==1:
        return x
    else:
        return factorial(x-1) * x


def factorial2(x):
    y=0
    while x>1:
        y *= x
        x -= 1
        return y

val=int(input("Enter Value: "))
print("factorial = " + str(factorial(val)))
print("factorial2 = " + str(factorial(val)))