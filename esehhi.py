'''def add(x,y,z):
  return x+y
print(add(3,4,5))
def sum(n):
  if n==1:
    return 1
  else:
    return n*sum(n-1)
print(sum(5))
class first:
  def fun(name,roll):
    print("Hello "+ name+" " + roll)

obj=first()
print(first.fun('Aditi','94'))'''
class first:
  def meth1(self):
    print("Method 1")

class second:
  def meth1(self):
    print("Method 2")

class third(first,second):
  def meth3(self):
    print("Method 3")

obj=third()
obj.meth1()
#obj.meth2()