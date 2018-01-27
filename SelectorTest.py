
# coding: utf-8

# In[17]:


import requests
from bs4 import BeautifulSoup
res = requests.get('http://news.qq.com/')
soup = BeautifulSoup(res.text,'html.parser')
alink = soup.select('.linkto')
for link in alink:
    print(link.text)
    

