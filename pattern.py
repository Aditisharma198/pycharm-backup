Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(1,6):
	print ("*"*i)

	
*
**
***
****
*****
>>> for i in range(6,1):
	print("*"*i)

	
>>> 
>>> for i in range(6,1,-1):
	print("*"*i)

	
******
*****
****
***
**
>>> for i in range(5,0,-1):
	print("*"*i)

	
*****
****
***
**
*
>>> for i in range(1,6):
	print(" "*(5-i)+"*"*i)

	
    *
   **
  ***
 ****
*****
>>> for i in range(1,6):
	print(" "*(5-i)+"*"*i+" "*(5-i))

	
    *    
   **   
  ***  
 **** 
*****
>>> for i in range(1,6):
	print(" "*i+"*"*i+" "*i)

	
 * 
  **  
   ***   
    ****    
     *****     
>>> for i in range(6,1,-1):
	print(" "*i+"*")

	
      *
     *
    *
   *
  *
>>> for i in range(6,1,-1):
	print(" "*i+"*"*(7-i))

	
      *
     **
    ***
   ****
  *****
>>> for i in range(1,6):
	print(" "*(5-i)+"*"*i)

	
    *
   **
  ***
 ****
*****
>>> for i in range(1,6):
	print(" "*(5-i)+"*"*i+" ")

	
    * 
   ** 
  *** 
 **** 
***** 
>>> for i in range(1,6):
	print(" "*(5-i)+"*"*i+" "*i)

	
    * 
   **  
  ***   
 ****    
*****     
>>> for i in range(1,6):
	print(" "*(5-i)+"*"*i+"_"*i)

	
    *_
   **__
  ***___
 ****____
*****_____
>>> for i in range(1,6):
	print(" "*(5-i)+("*"+" ")*i)

	
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
>>> for i in range(1,6):
	print(" "*(5-i)+"* "*i)

	
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
>>> for i in range(6,1,-1):
	print(" "*(5-i)+("*"+" ")*i)

	
* * * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
>>> for i in range(5,0,-1):
	print(" "*(5-i)+("*"+" ")*i)

	
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
>>> if (i<6):
	for i in range(1,6):
	print(" "*(5-i)+"* "*i)
	
SyntaxError: expected an indented block
>>> if (i<6):
	for i in range(1,6):
	    print(" "*(5-i)+"* "*i)
else:
	for i in range(5,0,-1):
	print(" "*(5-i)+("*"+" ")*i)
	
SyntaxError: expected an indented block
>>> if (i<6):
	for i in range(1,6):
	    print(" "*(5-i)+"* "*i)
else:
	for i in range(5,0,-1):
	    print(" "*(5-i)+("*"+" ")*i)

	    
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
>>> for i in range(1,10):
	if i<5:
		print(" "*(10-i)+"*"*i)
	else:
		print("*"*i+" "*(10-i))

		
         *
        **
       ***
      ****
*****     
******    
*******   
********  
********* 
>>> for i in range(1,10):
	if i<5:
		print(" "*(10-i)+"*"*i)
	else:
		print(" "*i+"*"*(10-i))

		
         *
        **
       ***
      ****
     *****
      ****
       ***
        **
         *
>>> for i in range(1,10):
	if i<5:
		print(" "*(10-i)+"* "*i)
	else:
		print(" "*i+"* "*(10-i))

		
         * 
        * * 
       * * * 
      * * * * 
     * * * * * 
      * * * * 
       * * * 
        * * 
         * 
>>> for i in range(1,10):
	if i<5:
		print("*"*(10-i)+" "*i)
	else:
		print("*"*i+" "*(10-i))

		
********* 
********  
*******   
******    
*****     
******    
*******   
********  
********* 
>>> for i in range(1,10,2):
	print(" "*(10-i)+"* "*i)

	
         * 
       * * * 
     * * * * * 
   * * * * * * * 
 * * * * * * * * * 

>>> for i in range(1,10,2):
	if i<9:
		print(" "*(10-i)+"* "*i)
	else:
		print(" "*i+"* "*(10-i))

		
         * 
       * * * 
     * * * * * 
   * * * * * * * 
         * 
>>> for i in range(1,10,2):
	if i<9:
		print(" "*(16-i)+"* "*i)
	else:
		print(" "*i+"* "*(16-i))

		
               * 
             * * * 
           * * * * * 
         * * * * * * * 
         * * * * * * * 
>>> for i in range(1,10,2):
	if i<5:
		print(" "*(10-i)+"* "*i)
	else:
		print(" "*i+"* "*(10-i))

		
         * 
       * * * 
     * * * * * 
       * * * 
         * 
>>> for i in range(1,10,2):
	if i<9:
		print(" "*(10-i)+"* "*i)
	else:
		print(" "*i+"* "*(10-i))

		
         * 
       * * * 
     * * * * * 
   * * * * * * * 
         * 
>>> for i in range(1,16,2):
	if i<16:
		print(" "*(16-i)+"* "*i)
	else:
		print(" "*i+"* "*(16-i))

		
               * 
             * * * 
           * * * * * 
         * * * * * * * 
       * * * * * * * * * 
     * * * * * * * * * * * 
   * * * * * * * * * * * * * 
 * * * * * * * * * * * * * * * 
>>> for i in range(1,10,2):
	if i<9:
		print(" "*(10-i)+"* "*i)
	else:
		print(" "*i+"* "*(10-i))

		
         * 
       * * * 
     * * * * * 
   * * * * * * * 
         * 
>>> for i in range(1,10,2):
	if i<11:
		print(" "*(10-i)+"* "*i)
	else:
		print(" "*i+"* "*(10-i))

		
         * 
       * * * 
     * * * * * 
   * * * * * * * 
 * * * * * * * * * 
>>> for i in range(1,11,2):
	if i<11:
		print(" "*(11-i)+"* "*i)
	else:
		print(" "*i+"* "*(11-i))

		
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
>>> for i in range(1,18,2):
	if i<9:
		print(" "*(10-i)+"* "*i)
	else:
		print(" "*i+"* "*(18-i))

		
         * 
       * * * 
     * * * * * 
   * * * * * * * 
         * * * * * * * * * 
           * * * * * * * 
             * * * * * 
               * * * 
                 * 
>>> for i in range(1,18,2):
	if i<9:
		print(" "*(18-i)+"* "*i)
	else:
		print(" "*i+"* "*(18-i))

		
                 * 
               * * * 
             * * * * * 
           * * * * * * * 
         * * * * * * * * * 
           * * * * * * * 
             * * * * * 
               * * * 
                 * 
>>> for i in range(1,6):
	print(" "*(5-i)+i)

	
Traceback (most recent call last):
  File "<pyshell#83>", line 2, in <module>
    print(" "*(5-i)+i)

TypeError: can only concatenate str (not "int") to str
>>> for i in range(1,6):
	print(" "*(5-i)+"i")

	
    i
   i
  i
 i
i
>>> for i in range(1,6):
	print(" "*(5-i)+(i))

	
Traceback (most recent call last):
  File "<pyshell#87>", line 2, in <module>
    print(" "*(5-i)+(i))
TypeError: can only concatenate str (not "int") to str
>>> for i in range(1,6):
	print(" "*(5-i),i)

	
     1
    2
   3
  4
 5
>>> for i in range(1,6):
	print(" "*(5-i),(i+" "))

	
Traceback (most recent call last):
  File "<pyshell#91>", line 2, in <module>
    print(" "*(5-i),(i+" "))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> for i in range(1,6):
	print(" "*(5-i),i,i)

	
     1 1
    2 2
   3 3
  4 4
 5 5
>>> for i in range(1,6):
	print(" "*(5-i),("*"+" ")*i)

	
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
>>> for i in range(1,6):
	print(" "*(5-i),(i+" ")*i)

	
Traceback (most recent call last):
  File "<pyshell#97>", line 2, in <module>
    print(" "*(5-i),(i+" ")*i)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> for i in range(1,6):
	print(" "*(5-i),(i," ")*i)

	
     (1, ' ')
    (2, ' ', 2, ' ')
   (3, ' ', 3, ' ', 3, ' ')
  (4, ' ', 4, ' ', 4, ' ', 4, ' ')
 (5, ' ', 5, ' ', 5, ' ', 5, ' ', 5, ' ')
>>> for i in range(1,6):
	print(" "*(5-i),(i)*i)

	
     1
    4
   9
  16
 25
>>> for i in range(1,6):
	print(" "*(5-i)+("*"+" ")*i)

	
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
>>> for i in range(1,6):
	for j in range(1,i+1):
		print(j,end="")
	print()

	
1
12
123
1234
12345
>>> for i in range(1,6):
	for j in range(1,i+1):
		print(" "*(5-i),j,end="")
	print()

	
     1
    1    2
   1   2   3
  1  2  3  4
 1 2 3 4 5
>>>  for i in range(1,6):
	for j in range(1,i+1):
		print(" "*(5-i),j)
	print()
	
SyntaxError: unexpected indent
>>> for i in range(1,6):
	for j in range(1,i+1):
		print(" "*(5-i),j)
	print()

	
     1

    1
    2

   1
   2
   3

  1
  2
  3
  4

 1
 2
 3
 4
 5

>>> for i in range(1,6):
	for j in range(1,i+1):
		print(" "*(5-i),j,end="")
	print()

	
     1
    1    2
   1   2   3
  1  2  3  4
 1 2 3 4 5
>>> for i in range(1,6):
	for j in range(1,i+1):
		print(" "*(5-j),j,end="")
	print()

	
     1
     1    2
     1    2   3
     1    2   3  4
     1    2   3  4 5
>>> for i in range(1,6):
	for j in range(1,i+1):
		print(j,end="")
	print(" "*(5-i))

	
1    
12   
123  
1234 
12345
>>> for i in range(1,6):
	for j in range(1,i+1):
		print(" ",j,end="")
	print(" "*(5-i))

	
  1    
  1  2   
  1  2  3  
  1  2  3  4 
  1  2  3  4  5
>>> for i in range(1,6):
	for j in range(1,i+1):
		print(" "*(5+i),j,end="")
	print()









	
