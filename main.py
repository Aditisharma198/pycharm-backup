a=int(input("Enter value of a="))
b=int(input("Enter value of b="))
print('---------CALCULATOR---------')
print('Perform Operations:\n'
      '1-Addition\n'
      '2-Subtraction\n'
      '3-Multiplication\n'
      '4-Division\n'
      '5-Modulus\n'
      '6-floor Division\n')

op=int(input('Select Operation to be performed'))
if(op==1):
    print('result=',a+b)
elif(op==2):
    print('result=',a - b)

elif(op==3):
    print('result=',a * b)

elif(op==4):
    print('result=',a / b)

elif(op==5):
    print('result=',a % b)

elif(op==6):
    print('result=',a//b)

else:
    print("Operation chosen is incorrect")
