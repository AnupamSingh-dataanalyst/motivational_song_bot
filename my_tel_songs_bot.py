#!/usr/bin/env python
# coding: utf-8

# In[4]:


import telebot
import random
from mymy import get_temp
from my_tel_key import *
bot = telebot.TeleBot(API_KEY)
print('done')


# In[2]:


songs=['Aa dekhe jara kisme kita hai dum…..',
 'Chale chalo….(Lagaan)',
 'Aashayein Aashayein…Kuch pane ki ho aas aas…(Iqbal)',
 'Aashayein khili dil mein..teri woh raftar ho, roke se bhi tu na ruke [slow]…(Iqbal)',
 'Allah ke bande hasde, allah ke bande…(Album by Kailash Kher)',
 'Apni to Pathshala…..(Rang de Basanti)',
 'Aye maalik tere bande hum…',
 'Aye shala abhi abhi hua yakein…..Ru ba ru…',
 'Aanewala pal jaanewala hai…..(Golmaal)-old',
 'Haan yahi rasta hai tune yahi jana hai…(Lakshya)',
 'Haan yahi sapan hai tera (lakshya)',
 'Har ghadi badal rahi hai…..(Kal Ho Na Ho)',
 'Haste haste kat jaye rastein…..(Khoon bhari maang)',
 'Hum honge kaamyaab……',
 'I am the best……..(Phir bhi dil hai Hindustani)',
 'Itni shakti humein dena data…',
 'Jit jayenge hum (meri jung)',
 'Jo soche jo chahe woh kar ke dikhade, hum woh hai jo do aur do paach bana de….',
 'Kandhon se milte hain kandhe…(Lakshya)',
 'Kisi ki muskarahton pe…jeena isi ka naam hai….',
 'Kiska hai ye tujhko intezaar main hoon na…(Main hoon na)',
 'Koi kahe kehta rahe….(Dil Chahta Hai)',
 'Mutthi mein asmaan…(Iqbal)',
 'Papa kehte hain bada naam karega…..(Q se Q tak)',
 'Rote hue aatein hai sab…….(Mukaddar ka sikander)',
 'Ruke ho kyon, jhuke ho kyon…jaan mein hai dum…',
 'Sochna kya jo bhi hoga dekha jayega…..(Ghaayal)',
 'Subah ho gayi mamu…(Munnabhai MBBS)',
 'Uparwala jab bhi deta, deta chappar phad ke…(Hera pheri)',
 'Woh sikander hi dosto kehlata hai….(Jo jeeta wahi sikender)',
 'Zindagi har kadam ek nayi jung hai…..(Meri Jung)',
 'Zindagi ke safar mein gujar jaatein hai jo sama…..(Aap ki kasam)',
 'Zindagi ki na toote ladi…..(Kranti)',
 'Zindgi ki yahi reet hai.. har ke baad hi jeet hai…(mr. India)']


# In[3]:


def motivate_me():
    random_song = random.choice(songs)
    return random_song


# In[7]:


motivate_me()


# In[12]:


@bot.message_handler(commands=['motivate'])
def motivate(message):
    motivate= motivate_me()
    bot.send_message(message.chat.id,motivate)
    
bot.polling()


# In[ ]:




