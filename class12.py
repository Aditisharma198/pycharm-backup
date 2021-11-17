#exception handling
#try and except block not catchhhhhhhhhhhhhhh
x=int(input())
y=int(input())
try:
    if(x>y):
        print(x/y)
    else:
        print(y/x)
except Exception as a:                         #/ZeroDivisionError
    print(a)
else:
    print("No  exception occured")
finally:
    print("hello")
print("Hey")