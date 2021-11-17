import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#x=[1,15,6,18,19]
#y=[10,6,15,12,8]
#fruit=['A','B','C','D','E']
#fs=[100,106,115,120,80]
#col=['red','green','pink','blue','yellow']
#plt.scatter(x,y)
#plt.scatter(x,y,color=col,s=60)
#plt.bar(fruit,fs)
#plt.barh(fruit,fs,color=col,height=0.3)

#x=np.random.normal(150,7,200)
#print(x)
#plt.hist(x)

fs=[10,20,30,40,50]
flabel=['A','B','C','D','E']
expl=[0,0,0,0.3,0]
plt.subplot(1,2,1)
plt.pie(fs,labels=flabel)
plt.legend()
plt.subplot(1,2,2)
plt.pie(fs,labels=flabel,startangle=90,explode=expl,shadow=True,autopct='%1.2f%%')
plt.show()