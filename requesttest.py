
# coding: utf-8

# In[10]:


import requests
res = requests.get('http://news.sina.com.cn/china/')
res.encoding = 'utf-8'
#print(res.text)


# In[9]:


from bs4 import BeautifulSoup
html_sample = ' <html>  <body>   <h1 id="title">Hello World</h1>  <a href="#" class="link"> This is link1</a>  <a href="# link2" class="link"> This is link2</a>  </body>  </html> ' 

soup = BeautifulSoup(html_sample,'html.parser')
print(soup.text)


# In[13]:


soup = BeautifulSoup(html_sample,'html.parser')
header = soup.select('h1')
print(header)
print(header[0])
print(header[0].text)


# In[18]:


soup = BeautifulSoup(html_sample,'html.parser')
alink = soup.select('a')
print(alink)
for link in alink:
    print(link.text)


# In[20]:


atitle = soup.select('#title')
print(atitle)


# In[23]:


alink = soup.select('.link')
for link in alink:
    print(link.text)


# In[28]:


print(alink)
for link in alink:
    print(link['href'])


# In[4]:


import requests
from bs4 import BeautifulSoup
res = requests.get('http://news.sina.com.cn/china/')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')


# In[9]:


for news in soup.select('.news-item'):
    if len(news.select('h2')) > 0:
        h2 = news.select('h2')[0].text
        a = news.select('a')[0]['href']
        time = news.select('.time')[0].text
        #print(time,h2,a)


# In[111]:


import requests
res = requests.get('http://news.sina.com.cn/c/nd/2018-01-27/doc-ifyqyqni3621012.shtml')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')
#print(soup)


# In[112]:


soup.select('.main-title')[0].text
soup.select('.source')[0].text
soup.select('.date')[0].text


# In[113]:


soup.select('.date-source')[0].text.replace("\n"," ")


# In[114]:


from datetime import datetime
timesource = soup.select('.date')[0].text.replace(" ","")
dt = datetime.strptime(timesource,'%Y年%m月%d日%H:%M')
print(dt)


# In[115]:


soup.select('.date-source a')[0].text


# In[61]:


from datetime import datetime
timesource = soup.select('.date')[0].text.replace(" ","")
dt = datetime.strptime(timesource,'%Y年%m月%d日%H:%M')
print(dt)


# In[109]:


article = []
for p in soup.select('.article p')[: -1]:
    article.append(p.text.strip())
#print(article)

#' \n   '.join(article) 


# In[107]:


#soup.select('#article')[0].text.strip()


# In[106]:


#' '.join([p.text.strip() for p in soup.select('#article p')[:-1]])


# In[117]:


soup.select('.show_author')[0].text.strip()


# In[130]:


import requests
comments = requests.get('http://comment5.news.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=comos-fyqyqni3621012&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3')

import json
jd = json.loads(comments.text)
jd['result']['count']['total']


# In[139]:


import re

newsurl = 'http://news.sina.com.cn/c/nd/2018-01-27/doc-ifyqyqni3621012.shtml'
m = re.search('doc-i(.*).shtml',newsurl)
newsid = m.group(1)


# In[140]:


commentURL = 'http://comment5.news.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=comos-{}&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3'

commentURL.format(newsid)


# In[148]:


import re
import json
def getCommentCounts(newsurl):
    m = re.search('doc-i(.*).shtml',newsurl)
    newsid = m.group(1)
    comments = requests.get(commentURL.format(newsid))
    jd = json.loads(comments.text)
    return jd['result']['count']['total']

    


# In[151]:


news = 'http://news.sina.com.cn/c/nd/2018-01-26/doc-ifyqzcxh0024159.shtml'

getCommentCounts(news)


# In[169]:


import requests
from bs4 import BeautifulSoup

def getNewsDetail(newsurl):
    result = {}
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    result['title'] = soup.select('.main-title')[0].text
    result['source'] = soup.select('.source')[0].text
    result['date'] = soup.select('.date')[0].text
    result['article'] = ' '.join([p.text.strip() for p in soup.select('#article p')[:-1]])
    result['editor'] = soup.select('.show_author')[0].text.strip()
    return result


# In[171]:


news = 'http://news.sina.com.cn/c/nd/2018-01-26/doc-ifyqzcxh0024159.shtml'
#getNewsDetail(news)


# In[ ]:


import requests
res = resquests.get('')


# In[173]:


import pandas
df = pandas.Daa

