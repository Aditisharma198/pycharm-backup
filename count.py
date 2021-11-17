count = 0
odd = 0

for value in range(50,101):
    if value % 2 == 0:
        count = count+1

    else:
        odd = odd+1

print("Number of Even Nos.", count)
print("Number of Odd Nos.", odd)