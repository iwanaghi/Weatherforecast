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


url = "https://api.darksky.net/forecast/7cefa5e6ef956bf1d81c5c2f827b7021/35.708162, 139.736018?units=si&lang=ja"
# In[]:

data = requests.get(url).json()

# In[]:

date = data['daily']['data'][0]['time']
high_temp_celsius = data['daily']['data'][0]['temperatureMax']
low_temp_celsius = data['daily']['data'][0]['temperatureMin']
weather = data['daily']['data'][0]['icon']
summary = data['daily']['data'][0]['summary']

date = str(datetime.datetime.fromtimestamp(date))
print(date)

tstr = date
tdatetime = datetime.datetime.strptime(tstr, '%Y-%m-%d %H:%M:%S')
tdate = datetime.date(tdatetime.year, tdatetime.month, tdatetime.day)
tyear = str(tdate.year)
tmonth = str(tdate.month)
tday = str(tdate.day + 1)
print(tyear)
print(tmonth)
print(tday)


print(high_temp_celsius)
print(low_temp_celsius)

high_temp_celsius_round = round(high_temp_celsius, 1)
low_temp_celsius_round = round(low_temp_celsius, 1)

high_temp_celsius_round = str(high_temp_celsius_round)
low_temp_celsius_round = str(low_temp_celsius_round)
print(high_temp_celsius_round)
print(low_temp_celsius_round)

a = weather
if "rain" in a:
    a = "雨"
else:
        print(a)

if "partly-cloudy" in a:
    a = "くもり時々晴れ"
else:
    print(a)

if "cloudy" in a:
    a = "くもり"
else:
    print(a)

if "clear-day" in a:
    a = "晴れ"
else:
    print(a)

if "snow" in a:
    a = "雪"
else:
    print(a)

if "wind" in a:
    a = "強風"
else:
    print(a)

summary = str(summary)

path = './record.txt'
f = sum(1 for line in open(path))
f_sen = linecache.getline(path, f)
print(f_sen)

l = ["pta","ptb","ptc","ptd","pte"]
pattern=random.choice(l)
print(pattern)

while pattern == f_sen:
    print(pattern)
    pattern = random.choice(l)
    print(pattern)

with open(path, mode='a') as g:
        g.write("\n" + pattern)


    # In[32]:
print(pattern)
path = "./pictures/"
place = "東京"

if pattern == "pta":
    name = "chiesasaki"
    if a == "雨":
        message = "あっ、おはようございます。佐々木千枝です。今日の天気をお伝えします。\n"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"です。最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度です…\n傘を忘れないでくださいね...！#ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic =  path + name + '/sc8.jpg'
    elif a == "晴れ":
        message = "おはようございます。佐々木千枝です。今日の天気をお伝えします。\n"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"です。最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度です…\nいい天気になりますように！#ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name +'/sc4.jpg'
    elif a == "雪":
        message = "おはようございます。佐々木千枝です。今日の天気をお伝えします。\n"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"です。最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度です…\nプロデューサーさん！雪ですよ！ #ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name + '/sc11.jpg'
    elif a == "くもり時々晴れ":
        message = "おはようございます。佐々木千枝です。今日の天気をお伝えします。\n"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"です。最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度です。\nよくわからない天気ですね...#ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name + '/sc11.jpg'
    else:
        message = "おはようございます。佐々木千枝です。今日の天気をお伝えします。\n"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"です。最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度です…\nプロデューサー、ちゃんと見てくれてるっスか？#ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name +'/sc10.jpg'
else:
    print(pattern)


    # In[29]:


if pattern == "ptb":
    name = "hinaaraki"
    if a == "雨":
            message = "おはようございますっス！荒木比奈がお伝えする今日の天気予報っス\n"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"っス！最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度っスよー。\n傘を忘れずに持っていくっスよ〜#ブルナポ朝の天気予報 #ブルナポ応援企画"
            print(message)
            pic = path + name + '/ah11.jpg'
    elif a == "晴れ":
            message = "おはようございますっス！荒木比奈がお伝えする今日の天気予報っス\n"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"っス！最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度っスよー。\nプロデューサー、いい天気っスね♪#ブルナポ朝の天気予報 #ブルナポ応援企画"
            print(message)
            pic = path + name + '/ah5.jpg'
    elif a == "強風":
            message = "おはようございますっス！荒木比奈がお伝えする今日の天気予報っス\n"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"っス！最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度っスよー。\n寒い日は自宅で創作活動に勤しむっス。#ブルナポ朝の天気予報 #ブルナポ応援企画"
            print(message)
            pic = path + name + '/ah8.jpg'
    elif a == "くもり時々晴れ":
            message = "おはようございますっス！荒木比奈がお伝えする今日の天気予報っス\n"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"っス！最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度っスよー。\n不安定な天気に注意っス。#ブルナポ朝の天気予報 #ブルナポ応援企画"
            print(message)
            pic = path + name + '/ah2.jpg'
    else:
            message = "おはようございますっス！荒木比奈がお伝えする今日の天気予報っス\n"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"っス！最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度っスよー。\nプロデューサー、ちゃんと見てくれてるっスか？#ブルナポ朝の天気予報 #ブルナポ応援企画"
            print(message)
            pic = path + name + '/ah1.jpg'
else:
    print(pattern)


    # In[19]:


if pattern == "ptc":
    name = "harunakamijo"
    if a == "雨":
            message = "おはようございますっ！。上条春菜です！今日の天気予報をお伝えしますっ！\n"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"です。最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度です！\nたとえ雨で濡れてもメガネは外しませんっ！#ブルナポ朝の天気予報 #ブルナポ応援企画"
            print(message)
            pic = path + name + '/kh4.jpg'
    elif a == "晴れ":
            message = "おはようございますっ！。上条春菜です！\n"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"です。最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度です！\n今日も1日頑張りましょう！！#ブルナポ朝の天気予報 #ブルナポ応援企画"
            print(message)
            pic = path + name + '/kh3.jpg'
    elif a == "雪":
            message = "おはようございますっ！。上条春菜です！今日の天気予報をお伝えしますっ！\n"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"です。最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度です！\nささ、サンタ春菜からのプレゼント眼鏡をどうぞ！#ブルナポ朝の天気予報 #ブルナポ応援企画"
            print(message)
            pic = path + name + '/kh5.jpg'
    elif a == "くもり時々晴れ":
            message = "おはようございますっ！。上条春菜です！今日の天気予報をお伝えしますっ！\n"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"です。最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度です！\n空が曇っていても私の眼鏡は曇りませんよ！#ブルナポ朝の天気予報 #ブルナポ応援企画"
            print(message)
            pic = path + name + '/kh5.jpg'
    elif a == "強風":
            message = "おはようございますっ！。上条春菜です！今日の天気予報をお伝えしますっ！\n"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"です。最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度です！\n風が強い時は防塵メガネがおすすめですよ！#ブルナポ朝の天気予報 #ブルナポ応援企画"
            print(message)
            pic = path + name + '/kh6.jpg'
    else:
            message = "おはようございますっ！。上条春菜です！今日の天気予報をお伝えしますっ！\n"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"です。最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度です！\nさぁプロデューサーさん！眼鏡装着！あれ…わたしだけ！？#ブルナポ朝の天気予報 #ブルナポ応援企画"
            print(message)
            pic = path + name + '/kh1.jpg'
else:
        print(pattern)


    # In[56]:


if pattern == "ptd":
    name = "sarinamatsumoto"
    if a == "雨":
        message = "朝からごくろうさま♪松本沙理奈が今日の天気予報をお伝えするわよ！\n"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"！最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度よ♪\nプロデューサー、傘♡忘れてない？#ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name + '/ms15.jpg'
    elif a == "晴れ":
        message = "朝からごくろうさま♪松本沙理奈が今日の天気予報をお伝えするわよ！\n"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"！最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度よ♪\nアイドルがお休みでもセクシーはお休みしないわ！ #ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name + '/ms15.jpg'
    elif a == "強風":
        message = "朝からごくろうさま♪今日の天気予報をお伝えするわよ！\n"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"！最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度よ♪\n風にも負けず、セクシーは年中無休よ！ #ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name + '/ms15.jpg'
    elif a == "くもり時々晴れ":
        message = "朝からごくろうさま♪今日の天気予報をお伝えするわよ！\n"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"！最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度よ♪\n風にも負けず、セクシーは年中無休よ！ #ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name + '/ms15.jpg'
    else:
        message = "朝からごくろうさま♪松本沙理奈が今日の天気予報をお伝えするわよ！\n"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"！最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度よ♪\n天気予報もセクシーにお届けするわ！ #ブルナポ朝の天気予報 #ブルナポ応援企画"
        print(message)
        pic = path + name + '/ms15.jpg'
else:
    print(pattern)


    # In[55]:


if pattern == "pte":
    name = "mizukikawashima"
    if a == "雨":
        message = "おはようございますっ♪川島瑞樹が今日の天気をお知らせするわよ！"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"、最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度よ♪\n雨の日はゆっくり休みたいわね...#ブルナポ朝の天気予報　#ブルナポ応援企画"
        print(message)
        pic = path + name + '/km8.jpg'
    elif a == "晴れ":
        message = "みんなおはようっ♪川島瑞樹が今日の天気をお伝えするわ！"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"、最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度になるわよ！\n日差しは女の天敵よね…わかるわ。#ブルナポ朝の天気予報　#ブルナポ応援企画"
        print(message)
        pic = path + name + '/km7.jpg'
    elif a == "強風":
        message = "おはようございますっ♪...おほん！\n川島瑞樹が今日の天気をお伝えします。"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"、最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度よ！\n今日も1日頑張りましょう♪　#ブルナポ朝の天気予報　#ブルナポ応援企画"
        print(message)
        pic = path + name + '/km15.jpg'
    elif a == "くもり時々晴れ":
        message = "おはようございますっ♪\n川島瑞樹が今日の天気をお知らせするわ！"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"、最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度よ！\nプロデューサー君、気温の変化には気をつけてね　#ブルナポ朝の天気予報　#ブルナポ応援企画"
        print(message)
        pic = path + name + '/km5.jpg'
    else:
        message = "おはようございますっ♪...おほん！\n川島瑞樹が今日の天気をお伝えします。"+tyear+"年"+tmonth+"月"+tday+"日の"+place+"の天気は"+a+"、最高気温は"+high_temp_celsius_round+"度、最低気温は"+low_temp_celsius_round+"度になるでしょう\n\n...あらやだ、局アナの頃より調子いいかも…#ブルナポ朝の天気予報　#ブルナポ応援企画"
        print(message)
        pic = path + name + '/km4.jpg'
else:
    print("OK")

    # In[37]:


    auth = tweepy.OAuthHandler(os.environ['API_key'],os.environ['API_secret'])
    auth.set_access_token(os.environ['ACCESS_token'],os.environ['ACCESS_token_secret'])
    api = tweepy.API(auth)


    # In[38]:


    api.update_with_media(filename = pic, status = message)

    # In[ ]:
