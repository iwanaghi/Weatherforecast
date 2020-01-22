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
tdayo = str(tdateo.day + 1)
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

lo = ["ptd"]
pattern=random.choice(lo)
print(pattern)

while pattern == f_sen:
    print(pattern)
    pattern = random.choice(lo)

print(pattern)

with open(path, mode='a') as g:
    g.write("\n" + pattern)

# In[32]:
print(pattern)
path = "./pictures/"
place = "大阪"

if pattern == "pta":
    name = "chiesasaki"
    if b == "雨":
        message = "あっ、おはようございます。佐々木千枝です。今日の天気をお伝えします。\n"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"です。最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度です…\n傘を忘れないでくださいね...！#ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic =  path + name + '/sc8.jpg'
    elif b == "晴れ":
        message = "おはようございます。佐々木千枝です。今日の天気をお伝えします。\n"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"です。最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度です…\nいい天気になりますように！#ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name +'/sc4.jpg'
    elif b == "雪":
        message = "おはようございます。佐々木千枝です。今日の天気をお伝えします。\n"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"です。最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度です…\nプロデューサーさん！雪ですよ！ #ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name + '/sc11.jpg'
    elif b == "くもり時々晴れ":
        message = "おはようございます。佐々木千枝です。今日の天気をお伝えします。\n"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"です。最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度です。\nよくわからない天気ですね...#ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name + '/sc11.jpg'
    else:
        message = "おはようございます。佐々木千枝です。今日の天気をお伝えします。\n"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"です。最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度です…\nプロデューサー、ちゃんと見てくれてるっスか？#ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name +'/sc10.jpg'
else:
    print(pattern)


    # In[29]:


if pattern == "ptb":
    name = "hinaaraki"
    if b == "雨":
            message = "おはようございますっス！荒木比奈がお伝えする今日の天気予報っス\n"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"っス！最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度っスよー。\n傘を忘れずに持っていくっスよ〜#ブルナポ朝の天気予報 #ブルナポ応援企画"
            print(message)
            pic = path + name + '/ah4.jpg'
    elif b == "晴れ":
            message = "おはようございますっス！荒木比奈がお伝えする今日の天気予報っス\n"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"っス！最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度っスよー。\nプロデューサー、いい天気っスね♪#ブルナポ朝の天気予報 #ブルナポ応援企画"
            print(message)
            pic = path + name + '/ah5.jpg'
    elif b == "強風":
            message = "おはようございますっス！荒木比奈がお伝えする今日の天気予報っス\n"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"っス！最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度っスよー。\n寒い日は自宅で創作活動に勤しむっス。#ブルナポ朝の天気予報 #ブルナポ応援企画"
            print(message)
            pic = path + name + '/ah8.jpg'
    elif b == "くもり時々晴れ":
            message = "おはようございますっス！荒木比奈がお伝えする今日の天気予報っス\n"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"っス！最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度っスよー。\n不安定な天気に注意っス。#ブルナポ朝の天気予報 #ブルナポ応援企画"
            print(message)
            pic = path + name + '/ah2.jpg'
    else:
            message = "おはようございますっス！荒木比奈がお伝えする今日の天気予報っス\n"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"っス！最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度っスよー。\nプロデューサー、ちゃんと見てくれてるっスか？#ブルナポ朝の天気予報 #ブルナポ応援企画"
            print(message)
            pic = path + name + '/ah1.jpg'
else:
    print(pattern)


# In[19]:


if pattern == "ptc":
    name = "harunakamijo"
    if b == "雨":
        message = "おはようございますっ！。上条春菜です！今日の天気予報をお伝えしますっ！\n"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"です。最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度です！\nたとえ雨で濡れてもメガネは外しませんっ！#ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name + '/kh4.jpg'
    elif b == "晴れ":
        message = "おはようございますっ！。上条春菜です！\n"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"です。最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度です！\n今日も一日頑張りましょう！#ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name + '/kh3.jpg'
    elif b == "雪":
        message = "おはようございますっ！。上条春菜です！今日の天気予報をお伝えしますっ！\n"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"です。最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度です！\nささ、サンタ春菜からのプレゼント眼鏡をどうぞ！#ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name + '/kh5.jpg'
    elif b == "くもり時々晴れ":
        message = "おはようございますっ！。上条春菜です！今日の天気予報をお伝えしますっ！\n"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"です。最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度です！\n空が曇っていても私の眼鏡は曇りませんよ！#ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name + '/kh5.jpg'
    elif b == "強風":
        message = "おはようございますっ！。上条春菜です！今日の天気予報をお伝えしますっ！\n"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"です。最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度です！\n風が強い時は防塵メガネがおすすめですよ！#ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name + '/kh6.jpg'
    else:
        message = "おはようございますっ！。上条春菜です！今日の天気予報をお伝えしますっ！\n"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"です。最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度です！\n今日も頑張りましょう！#ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name + '/kh6.jpg'
else:
    print(pattern)


# In[56]:


if pattern == "ptd":
    name = "sarinamatsumoto"
    if b == "雨":
        message = "朝からごくろうさま♪松本沙理奈が今日の天気予報をお伝えするわよ！\n"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"！最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度よ♪\nプロデューサー、傘♡忘れてない？#ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name + '/ms16.jpg'
    elif b == "晴れ":
        message = "朝からごくろうさま♪松本沙理奈が今日の天気予報をお伝えするわよ！\n"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"！最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度よ♪\nプロデューサー、セクシーは年中無休よ！#ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name + '/ms16.jpg'
    elif a == "強風":
        message = "朝からごくろうさま♪今日の天気予報をお伝えするわよ！\n"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"！最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度よ♪\nプロデューサー、セクシーは年中無休よ！ #ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name + '/ms16.jpg'
    elif b == "くもり時々晴れ":
        message = "朝からごくろうさま♪今日の天気予報をお伝えするわよ！\n"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"！最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度よ♪\n船の上は解放的な気分にさせてくれるわ♪ #ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name + '/ms16.jpg'
    else:
        message = "朝からごくろうさま♪松本沙理奈が今日の天気予報をお伝えするわよ！\n"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"！最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度よ♪\nプロデューサー、セクシーは年中無休よ！ #ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name + '/ms16.jpg'
else:
    print(pattern)


# In[55]:


if pattern == "pte":
    name = "mizukikawashima"
    if b == "雨":
        message = "おはようございますっ♪川島瑞樹が今日の天気をお知らせするわよ！"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"、最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度よ♪\n雨の日はゆっくり休みたいわね...#ブルナポ朝の天気予報　#ブルナポ応援企画"
        print(message)
        pic = path + name + '/km8.jpg'
    elif b == "晴れ":
        message = "みんなおはようっ♪川島瑞樹が今日の天気をお伝えするわ！"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"、最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度になるわよ！\n日差しは女の天敵よね…わかるわ。#ブルナポ朝の天気予報　#ブルナポ応援企画"
        print(message)
        pic = path + name + '/km7.jpg'
    elif b == "強風":
        message = "おはようございますっ♪...おほん！\n川島瑞樹が今日の天気をお伝えします。"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"、最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度よ！\n今日も1日頑張りましょう♪　#ブルナポ朝の天気予報　#ブルナポ応援企画"
        print(message)
        pic = path + name + '/km15.jpg'
    elif b == "くもり時々晴れ":
        message = "おはようございますっ♪\n川島瑞樹が今日の天気をお知らせするわ！"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"、最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度よ！\nプロデューサー君、気温の変化には気をつけてね　#ブルナポ朝の天気予報　#ブルナポ応援企画"
        print(message)
        pic = path + name + '/km5.jpg'
    else:
        message = "おはようございますっ♪...おほん！\n川島瑞樹が今日の天気をお伝えします。"+tyearo+"年"+tmontho+"月"+tdayo+"日の"+place+"の天気は"+b+"、最高気温は"+high_temp_celsius_roundo+"度、最低気温は"+low_temp_celsius_roundo+"度になるでしょう\n\n...あらやだ、局アナの頃より調子いいかも…#ブルナポ朝の天気予報　#ブルナポ応援企画"
        print(message)
        pic = path + name + '/km4.jpg'
else:
    print("OK")

# In[37]:


# In[22]:


auth = tweepy.OAuthHandler(os.environ['API_key'],os.environ['API_secret'])
auth.set_access_token(os.environ['ACCESS_token'],os.environ['ACCESS_token_secret'])
api = tweepy.API(auth)


# In[23]:


api.update_with_media(filename = pic, status = message)



# In[ ]:
