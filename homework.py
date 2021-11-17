#Check whether number is prime or not
'''n=int(input())
y=2
while(y<=n-1):
    if(n%y==0):
     print("N is not prime")
     break
    y+=1

    if(y>=n-1):
        print("N is prime")


#https://www.hackerrank.com/challenges/python-loops/problem
    n = int(input())
    for i in range(n):
        print(i*i)

#Make a program where you can pass any number of arguments and it will return avg of all of them.
def func(*n):
    print(sum(n)/len(n))
func(1,2,3,4,5,6,7,8,9)'''

#Write a function you will pass two number and operation name(Optional) and it will do the operation,
# If no operation is pass then do the addition. And return the result
import math

'''def func(x,y,op="Add"):
    if(op=="Add"):
        print(x+y)
    elif(op=="Sub"):
        print(x-y)
    elif(op=="Mul"):
        print(x*y)
    elif(op=="Div"):
        print(x/y)
    elif(op=="Mod"):
        print(x%y)
func(int(input()),int(input()))
#https://www.hackerrank.com/challenges/swap-case/problem:
def swap_case(s):
    c=""
    for i in s:
        if(i.isupper()==True):
            c+=i.lower()
        else:
            c+=i.upper()
    return c

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)'''

'''#given a input n, write program that prints sum of all even numbers from 1 to n.
n=int(input())
c=0
for i in range(1,n):
    if(i%2==0):
        c=c+i

print(c)

#table upto n
s=int(input())
for j in range(1,s+1):
    print('\n')
    for k in range(1,11):
     print('\n')
     print(j,"x",k,"=",j*k,end=" ")
#pattern
n=int(input())
while(n>=1):
    for i in range(1,n+1):
        print(i,end=" ")
    print("\n")
    n-=1'''
#perfect square
'''n=int(input())
y=1
while(y<n):
    if(y**2==n):
        print("Yes")
        break
    else:
        y+=1
        continue
else:
    print("No")'''

#alternate method
'''import math
n=int(input())
i=math.sqrt(n)
if(i-math.floor(i))==0:
    print("Yes")
else:
    print("No")


#WAP to print factorial of number
n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

n=int(input())
print(math.factorial(n))

#Fibonacci series
n=int(input())
a=0
b=1
c=0
if(n>0):
    print(a,b,end=" ")
    while(b<=n):
        c=a+b
        a=b
        b=c
        if(b<=n):
            print(b,end=" ")
#(split and join)replace all white spaces with dash
str="dancing in the ghetto"
sp=str.split()
print("-".join(sp))
#palindrome string
str=input().lower()
str1=str[::-1]
if(str==str1):
    print("String is palindrome")
else:
    print("String is not palindrome")
#pig latin
str=input().split(" ")
list=[]
for i in str:
    a=i[1:]+i[0]+"ay"
    list.append(a)
print(" ".join(list))
#count number of vowels and consonants in given string
str=input().lower()
cv=0
cc=0
vow=["a","e","i","o","u"]
for i in str:
    if(i in vow):
        cv+=1
    else:
        cc+=1
print(cv,cc)

#Print all lowercase characters from the given string.
str=input()
for i in str:
    if(i.islower()==True):
        print(i,end=",")'''

#Check if a given substring is present in the input string or not. Output 1 for yes and -1 for no.
str=input()
start=int(input())
end=int(input())
ss=str[start:end]
list=[]
list.append(ss)
if(ss in str):
    print("1")
else:
    print("-1")