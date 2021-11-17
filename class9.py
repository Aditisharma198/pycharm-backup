
''''#prime number
x=2
while(x<100):
    y=2
    while(y<=x-1):
        if(x%y==0):
            break
        y+=1

    if(y>=x-1):
        print(x)
    x+=1'''

x=2
while(x<100):
    y=2
    while(y<=x-1):
        if(x%y==0):
            break
        y+=1

    if(y>=x-1):
        print(x)
    x+=1

#Write a function you will pass two number and operation name(Optional) and it will do the operation, If no operation is pass then do the addition. And return the result
