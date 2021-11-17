def Sum(dict):
    sum = 0
    for i in dict.values():
        sum = sum + i

    return sum

dict = {'a': 500, 'b': 500, 'c': 200}
print("Sum :", Sum(dict))