print("-------Swapping-------")
a=int(input("A's value to be swapped:"))
b=int(input("B's value to be swapped:"))
'''a=a+b
b=a-b
a=a-b'''
a=a^b
b=a^b
a=a^b
print('Value of A:',a)
print('Value of B:',b)