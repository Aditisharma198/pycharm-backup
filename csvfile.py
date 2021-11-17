import requests
import bs4
import csv

res=requests.get('https://www.sport-histoire.fr/en/Geography/Currencies_countries_of_the_world.php')
#print(res)
soup=bs4.BeautifulSoup (res.content,'html.parser')
#print(soup.prettify())
#print(soup.title)
#print(soup.find_all('p'))
#print(soup.select('p'))
table=soup.find_all('table')[0]
rows = table.select('tbody > tr')
header=[th.text.rstrip() for th in rows[0].find_all('th')]
#title=[soup.title.text]
#print(title)

#sending text into csv file
#with open('first.csv','w') as file:
 #   writer=csv.writer(file)
#  writer.writerow(title)

with open('third.csv','w') as file2:
    writer=csv.writer(file2)
    writer.writerow(header[1:])
    for row in rows[1:]:
        data=[th.text.rstrip() for th in row.find_all('td')]
        writer.writerow(data)
