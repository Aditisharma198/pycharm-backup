def prime(*t):
    for i in t:
        if i%1==0 and i%2!=0:
            print(i,"is prime")
        else:
            print(i,"is not prime")
prime(3,4,5,6,7,8)
def isprime(*t)-> int:
    count = 0
    for i in t:
         for x in range(2, int(i/2)+1):
            if (i % x) == 0:
                # print(i, "is not a prime number")
                break
            else:
                # print(i, "is a prime number")
                count+=1
    return(count)
