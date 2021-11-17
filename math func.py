Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import turtle
  File "C:\Users\User\AppData\Local\Programs\Python\Python38-32\turtle.py", line 3, in <module>
    turtle.forward(100)
AttributeError: partially initialized module 'turtle' has no attribute 'forward' (most likely due to a circular import)
>>> import turtle
>>> for i in range(5):
	turtle.forward(100)
	turtle.right(90)
	if i==4:
		turtle.right(45)
		turtle.forward(140)
		turtle.left(45)
		turtle.forward(100)
		turtle.forward(140)

		
>>> for i in range(5):
	turtle.forward(100)
	turtle.right(90)
	if i==4:
		turtle.right(45)
		turtle.forward(140)

		
Traceback (most recent call last):
  File "<pyshell#5>", line 2, in <module>
    turtle.forward(100)
  File "<string>", line 5, in forward
turtle.Terminator
>>> 
KeyboardInterrupt
>>> for i in range(5):
	turtle.forward(100)
	turtle.right(90)
	if i==4:
		turtle.right(45)
		turtle.forward(140)

		
>>> for i in range(5):
	turtle.forward(100)
	turtle.right(90)
	if i==4:
		turtle.right(45)
		turtle.forward(140)
		turtle.left(45)
		turtle.forward(100)
		turtle.left(135)
		turtle.forward(140)

		
>>> for i in range(5):
	turtle.forward(100)
	turtle.right(90)
	if i==4:
		turtle.right(45)
		turtle.forward(140)
		turtle.left(135)
		turtle.forward(100)
		turtle.left(135)
		turtle.forward(140)

		
>>> for i in range(5):
	turtle.forward(100)
	turtle.right(90)
	if i==4:
		turtle.right(45)
		turtle.forward(140)
		turtle.left(135)
		turtle.forward(100)
		turtle.left(135)
		turtle.forward(140)

		
>>> turtle.reset()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    turtle.reset()
  File "<string>", line 5, in reset
turtle.Terminator
>>> for i in range(5):
	turtle.forward(100)
	turtle.right(90)
	if i==4:
		turtle.right(45)
		turtle.forward(140)
		turtle.left(135)
		turtle.forward(100)
		turtle.left(135)
		turtle.forward(140)

		
>>> Exception ignored in: <function Image.__del__ at 0x03359340>
Traceback (most recent call last):
  File "C:\Users\User\AppData\Local\Programs\Python\Python38-32\lib\tkinter\__init__.py", line 4014, in __del__
    self.tk.call('image', 'delete', self.name)
RuntimeError: main thread is not in main loop

============================================================================ RESTART: Shell ===========================================================================
>>> abs(-7)
7
>>> x=3-4i
SyntaxError: invalid syntax
>>> x=(3-4i)
SyntaxError: invalid syntax
>>> x=3-4j
>>> abs(x)
5.0
>>> divmod(8,9)
(0, 8)
>>> divmod(8.0,9.5)
(0.0, 8.0)
>>> round(3.456)
3
>>> round(3.456,2)
3.46
>>> pow(4,3)
64
>>> complex(4,2)
(4+2j)
>>> complex(2+3j,9+8j)
(-6+12j)
>>> x=input()
4
>>> complex("8+9j")
(8+9j)
>>> 