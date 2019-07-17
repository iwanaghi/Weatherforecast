#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy
import requests
import datetime
import random
import linecache
import os


# In[2]:

urlo = "https://api.darksky.net/forecast/7cefa5e6ef956bf1d81c5c2f827b7021/34.6937, 135.5022?units=si&lang=ja"
data = requests.get(urlo).json()


# In[3]:


dateo = data['daily']['data'][0]['time']
high_temp_celsiuso = data['daily']['data'][0]['temperatureMax']
low_temp_celsiuso = data['daily']['data'][0]['temperatureMin']
weathero = data['daily']['data'][0]['icon']
summaryo = data['daily']['data'][0]['summary']


# In[4]:


dateo = str(datetime.datetime.fromtimestamp(dateo))
print(dateo)


# In[5]:


tstro = dateo
tdatetimeo = datetime.datetime.strptime(tstro, '%Y-%m-%d %H:%M:%S')
tdateo = datetime.date(tdatetimeo.year, tdatetimeo.month, tdatetimeo.day)
tyearo = str(tdateo.year)
tmontho = str(tdateo.month)
tdayo = str(tdateo.day)
print(tyearo)
print(tmontho)
print(tdayo)


# In[6]:


print(high_temp_celsiuso)
print(low_temp_celsiuso)


# In[7]:


high_temp_celsius_roundo = round(high_temp_celsiuso, 1)
low_temp_celsius_roundo = round(low_temp_celsiuso, 1)


# In[8]:


high_temp_celsius_roundo = str(high_temp_celsius_roundo)
low_temp_celsius_roundo = str(low_temp_celsius_roundo)
print(high_temp_celsius_roundo)
print(low_temp_celsius_roundo)


# In[9]:


b = weathero
if "rain" in b:
    b = "雨"
else:
    print(b)


# In[10]:


if "partly-cloudy" in b:
    b = "くもり時々晴れ"
else:
    print(b)


# In[11]:


if "clear-day" in b:
    b = "晴れ"
else:
    print(b)


# In[12]:


if "cloudy" in b:
    b = "くもり"
else:
    print(b)


# In[13]:


if "snow" in b:
    b = "雪"
else:
    print(b)


# In[14]:


if "wind" in b:
    b = "強風"
else:
    print(b)


# In[15]:


summaryo = str(summaryo)


# In[53]:

path = './record.txt'
f = sum(1 for line in open(path))
f_sen = linecache.getline(path, f)
print(f_sen)

lo = ["pta","ptb","ptc","ptd","pte"]
patterno=random.choice(lo)
print(patterno)

while patterno == f_sen:
    print(patterno)
    patterno = random.choice(lo)

print(patterno)

with open(path, mode='a') as g:
    g.write("\n" + patterno)




# In[22]:


auth = tweepy.OAuthHandler(os.environ['API_key'],os.environ['API_secret'])
auth.set_access_token(os.environ['ACCESS_token'],os.environ['ACCESS_token_secret'])
api = tweepy.API(auth)


# In[23]:


api.update_with_media(filename = pico, status = messageo)



# In[ ]:
