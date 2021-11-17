import requests
from bs4 import BeautifulSoup

res=requests.get('https://www.geeksforgeeks.org/data-structures/')
soup=BeautifulSoup(res.content,'html.parser')

#aa=soup.find('div',class_='wrapper')
#print(aa)
#a=aa.find_all('div')
#for i in aa:
    #print(i.prettify())
head=soup.find('h1',string='Data Structures')
print(head)

