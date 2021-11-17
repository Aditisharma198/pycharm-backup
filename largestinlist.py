def large(list1):
    max=list1[0]
    for i in list1:
        if i>max:
            max=i
    return max
list1 = [23,56,85,49,77]
print("Largest element",large(list1))