'''from collections import OrderedDict
dict = {'z': 345, 'a': 244, 'c': 7867, 'd':990}
dict1=OrderedDict(sorted(dict.items()))
print(dict1)
dict = {'z': 345, 'a': 244, 'c': 7867, 'd':990}
print(sorted(dict.items(),key = lambda kv: kv[1]))
print(dict.values())'''
from collections import Counter
my_dict = {'A': 67, 'B': 23, 'C': 45,
           'D': 56, 'E': 12, 'F': 69}

k = Counter(my_dict)
high = k.most_common(3)

print("Initial Dictionary:")
print(my_dict, "\n")

print("Dictionary with 3 highest values:")
print("Keys: Values")

for i in high:
    print(i[0], " :", i[1], " ")