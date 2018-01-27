
# coding: utf-8

# In[4]:


import re
import requests
import json
def getCommentCounts(newsurl):
    m = re.search('doc-i(.*).shtml',newsurl)
    newsid = m.group(1)
    comments = requests.get(commentURL.format(newsid))
    jd = json.loads(comments.text)
    return jd['result']['count']['total']


# In[6]:


news = 'http://news.sina.com.cn/c/nd/2018-01-26/doc-ifyqzcxh0024159.shtml'

getCommentCounts(news)

