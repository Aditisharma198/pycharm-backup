tup=(5,4,7,8,6,2,5,7,9,8,8,8)
counter=0
for i in tup:
    if tup.count(i) > 1:
        counter=counter+1
print(i,'REPEATED',counter,'times')