
# coding: utf-8

# In[2]:


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
    result['comment'] = getCommentCounts(newsurl)
    return result


# In[3]:


import re
import requests
import json
def getCommentCounts(newsurl):
    m = re.search('doc-i(.*).shtml',newsurl)
    newsid = m.group(1)
    commentURL = 'http://comment5.news.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=comos-{}&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3'
    comments = requests.get(commentURL.format(newsid))
    jd = json.loads(comments.text)
    return jd['result']['count']['total']


# In[4]:


news = 'http://news.sina.com.cn/c/nd/2018-01-27/doc-ifyqyqni3675657.shtml'
#getNewsDetail(news)


# In[5]:


import requests
import json
def parseListLinks(url):
    newsdetails = []
    res = requests.get(url)
    jd =json.loads(res.text.lstrip('  newsloadercallback(').rstrip(');'))
    for nurl in jd['result']['data']:
        newsdetails.append(getNewsDetail(nurl['url']))
    return newsdetails


# In[6]:


url = 'http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}&callback=newsloadercallback&_=1517039096948'
news_total = []
for i in range(1,3):
    newsurl = url.format(i)
    newsary = parseListLinks(newsurl)
    news_total.extend(newsary)
#print(news_total)


# In[7]:


len(news_total)


# In[8]:


import pandas
df = pandas.DataFrame(news_total)
df.head(10)


# In[10]:


df.to_excel('news.xlsx')

