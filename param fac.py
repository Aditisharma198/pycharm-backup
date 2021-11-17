def fact(*t):
    #num = int(input("Enter a number: "))
    factorial = 1
    for i in t:
        factorial = factorial * i
        print("The factorial is", factorial)

fact(4,3,5,6,7)
def factorial(*t):
    for i in t:
        if i < 0:
            return 0
        elif i == 0 or i == 1:
            return 1
        else:
            fact = 1
        while(i > 1):
            fact *= i
            i -= 1
        print(fact)