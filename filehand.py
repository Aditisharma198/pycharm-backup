f = open("aditi.txt" , "rt")
'''returns the pointer thats why need to crate a file pointer'''
#content = f.read() #content = f.read(3)
#print(content)

    #for line in content: #line by line every content
        #print(line)

#print(f.readline())
#print(f.readline())
print(f.readlines()) #returns line in list format
#for line in f:  # line by line
     #print(line,end="")
f.close()