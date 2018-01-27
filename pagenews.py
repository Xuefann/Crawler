
# coding: utf-8

# In[24]:


import requests
import json
res = requests.get('http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page=3&callback=newsloadercallback&_=1517039096948')

jd =json.loads(res.text.lstrip('  newsloadercallback(').rstrip(');'))

for nurl in jd['result']['data']:
    print (nurl['url'])


# In[27]:


url = 'http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}&callback=newsloadercallback&_=1517039096948'
news_total = []
for i in range(1,4):
    newsurl = url.format(i)
    newsary = parseListLinks(newsurl)
    news_total.extend(newsary)

