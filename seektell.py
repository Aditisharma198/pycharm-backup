f = open("aditi.txt")
print(f.tell()) #tells the position of file header or pointer
print(f.readline())
f.seek(11) #prints from the character number passed
print(f.tell())
print(f.readline())
print(f.tell())