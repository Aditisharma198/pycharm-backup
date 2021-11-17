import requests
from bs4 import BeautifulSoup
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
res=requests.get('https://svvv.edu.in')
soup=BeautifulSoup(res.content,'html.parser')
text=soup.get_text(strip=True)
text1='I am student of SVVV. Currently in third year. How are you?'

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
wd=word_tokenize(text1)
#print(sent_tokenize(text1))
print(wd)
print(nltk.pos_tag(wd))
'''tokens=[t for t in text.split()]
freq=nltk.FreqDist(tokens)

for key,val in freq.items():
   print(str(key) +':' + str(val))

freq.plot(10,cumulative=False)'''
'''
from nltk.corpus import stopwords
clean_tokens=tokens[:]
sw=stopwords.words('english')
for token in tokens:
     if token in sw:
         clean_tokens.remove(token)
freq1=nltk.FreqDist(clean_tokens)
for key,val in freq1.items():
    print(str(key) +':'+ str(val))

freq1.plot(10,cumulative=False)'''
#print(tokens)