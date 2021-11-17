'''for row in range(6):
    for col in range(7):
        if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
            print("*",end="")
        else:
            print(end=" ")
    print()'''

#Homework: H=print;input=month,day o/p:seaason J-M:winter, A-J:spring, Ju-S:summer,else:autumn
'''if month=march or day>19-->spring
    if mon-june or day>20--->summer
    sep, day>21 :autumn
    dec, day>20 :winterr
    print(season)'''

'''month=input()
day=int(input())
cal=["Jan","Feb","March","April","May","June","July","Aug","Sep","Oct","Nov","Dec"]
if(month==cal[0] or month==cal[1] or month==cal[2]):
    if(month==cal[2] and day>19):
        print("Spring")
    else:
        print("Winter")

elif(month==cal[3] or month==cal[4] or month==cal[5]):
    if(month==cal[5] and day>20):
        print("Summer")
    else:
        print("Spring")
elif(month==cal[6] or month==cal[7] or month==cal[8]):
    if(month==cal[8] and day>21):
        print("AUTUMN")
    else:
        print("SUMMER")
elif(month==cal[11] and day>20):
    print("WINTER")
else:
    print("AUTUMN")'''
str=""
for row in range(7):
    for col in range(7):
        if(col==0 or col==6) or (row==3) and (col>0 and col<6):
            str=str+"*"
        else:
            str=str+" "
    str=str+"\n"
print(str)

