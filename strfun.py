Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> str=""
>>> str="abcd"
>>> str1="dcfe"
>>> str2="ghji"
>>> str.upper()
'ABCD'
>>> str1.lower()
'dcfe'
>>> len(str2)
4
>>> str2="HEllo, my name is aditi"
>>> str2.split()
['HEllo,', 'my', 'name', 'is', 'aditi']
>>> str2.split(" ")
['HEllo,', 'my', 'name', 'is', 'aditi']
>>> str2.split(",")
['HEllo', ' my name is aditi']
>>> str2.split(" ",3)
['HEllo,', 'my', 'name', 'is aditi']
>>> x=input()
a,b,b,d
>>> x.split(",")
['a', 'b', 'b', 'd']
>>> x=input().split(" ")
t y r s
>>> print(x)
['t', 'y', 'r', 's']
>>> str="Om shanti om"
>>> str.strip()
'Om shanti om'
>>> str.strip("om")
'Om shanti '
>>> str.strip("Om")
' shanti o'
>>> str.lstrip()
'Om shanti om'
>>> str.lstrip("Om")
' shanti om'
>>> str.rstrip("om")
'Om shanti '
>>> reversed(str2)
<reversed object at 0x03E35A18>
>>> list(reversed(str2))
['i', 't', 'i', 'd', 'a', ' ', 's', 'i', ' ', 'e', 'm', 'a', 'n', ' ', 'y', 'm', ' ', ',', 'o', 'l', 'l', 'E', 'H']
>>> str2[::-1]
'itida si eman ym ,ollEH'
>>> str.center(20)
'    Om shanti om    '
>>> str.center(30,"#")
'#########Om shanti om#########'
>>> str2.find("m")
7
>>> str2.find("x")
-1
>>> str2.find("aditi")
18
>>> str2.find("name",7,len(str-1))
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    str2.find("name",7,len(str-1))
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> str2.find("name",7,len(str)-1)
-1
>>> str2.isalnum()
False
>>> str2.isdecimal()
False
>>> str.count()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    str.count()
TypeError: count() takes at least 1 argument (0 given)
>>> str.count("a")
1
>>> str.count("om")
1
>>> str.isdigit()
False
>>> a="hey"
>>> b="hello"
>>> c="hye"
>>> d="arnav aditi"
>>> a.join(b)
'hheyeheylheylheyo'
>>> ""
''
3
>>> "#".join(a)
'h#e#y'
>>> 