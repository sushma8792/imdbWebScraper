#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup 


# In[2]:



column=['Title','Year','Summary','Rating','Genre','Actors','Directors','Writers']


# In[3]:


import pandas as pd 

movie_db = pd.DataFrame()

mainlist=[]


# In[4]:




urls = ['https://www.imdb.com/title/tt2245084/?ref_=fn_al_tt_1',#Baymax
       'https://www.imdb.com/title/tt0351283/?ref_=tt_sims_tt_i_4',#Madagascar
       'https://www.imdb.com/title/tt9683478/',#the half of it
        'https://www.imdb.com/title/tt6710474/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=ea4e08e1-c8a3-47b5-ac3a-75026647c16e&pf_rd_r=GT07B094NDJXQRYRVFN8&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=moviemeter&ref_=chtmvm_tt_7'#everything everywhere all at once
        ,'https://www.imdb.com/title/tt0126029/?ref_=ls_mv_close',#Shrek
        'https://www.imdb.com/title/tt2953050/?ref_=adv_li_tt',#Encanto
        'https://www.imdb.com/title/tt8097030/?ref_=tt_sims_tt_i_1',#Turning Red
        'https://www.imdb.com/title/tt2948372/?ref_=tt_sims_tt_i_6',#Soul
        'https://www.imdb.com/title/tt2380307/?ref_=tt_sims_tt_i_1',#Coco
        'https://www.imdb.com/title/tt0910970/?ref_=tt_sims_tt_i_3'#wall-e
        'https://www.imdb.com/title/tt0198781/?ref_=tt_sims_tt_i_3',#Monsters Inc.
        'https://www.imdb.com/title/tt0382932/?ref_=tt_sims_tt_i_4' , #Ratatouille
        'https://www.imdb.com/title/tt2883512/?ref_=tt_sims_tt_i_1',#Chef
        'https://www.imdb.com/title/tt0114709/?ref_=tt_sims_tt_i_7',#toyStory
        'https://www.imdb.com/title/tt0266543/?ref_=tt_sims_tt_i_5',#FindingNemo
        'https://www.imdb.com/title/tt2277860/?ref_=tt_sims_tt_i_6',#finding dory
        'https://www.imdb.com/title/tt1772341/?ref_=tt_sims_tt_i_4',#Wreck-itRalph
        'https://www.imdb.com/title/tt2948356/?ref_=tt_sims_tt_i_4',#Zootopia
        'https://www.imdb.com/title/tt2948356/?ref_=tt_sims_tt_i_4',#Moana
        'https://www.imdb.com/title/tt0398286/?ref_=tt_sims_tt_i_3',#tangled
        'https://www.imdb.com/title/tt1217209/?ref_=tt_sims_tt_i_2',#Brave
        'https://www.imdb.com/title/tt0317219/?ref_=tt_sims_tt_i_10',#cars
        #add more movies here
       ]

for url in urls: 
    ls=[]
    response=requests.get(url)
    soup = BeautifulSoup(response.content ,"html.parser" )
    title= (soup.title).string
    ls.append(title)
    year= soup.find(class_="ipc-link ipc-link--baseAlt ipc-link--inherit-color sc-8c396aa2-1 WIUyh").string
    ls.append(year)
    summary=soup.find(class_="sc-16ede01-2 gXUyNh").string
    ls.append(summary)
    rating = soup.find(class_="sc-7ab21ed2-1 jGRxWM").string
    ls.append(rating)
    genre = soup.find_all(class_="ipc-inline-list__item ipc-chip__text")
    genrelist=[]
    for i in genre:
        genrelist.append(i.string)
    ls.append(genrelist)
    top_actors=soup.find_all(class_="sc-18baf029-1 gJhRzH")
    topActorList=[]
    for i in top_actors:
        topActorList.append(i.string)

    characterAs = soup.find_all(class_="sc-18baf029-4 iYNZoy")
    topCharacterList=[]
    for i in characterAs:
        topCharacterList.append(i.string)
    for i in range( len(topCharacterList)):
        topActorList[i] = topActorList[i] +' ' +topCharacterList[i]
    ls.append(topActorList)
    director=soup.find_all('a' , attrs={'class':'ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link'})
    directors=[]
    directors.append(director[0].string)
    directors.append(director[1].string)
    ls.append(directors)
    writers=[]
    for i in range(3):
        writers.append(director[2+i].string)
    ls.append(writers)
    mainlist.append(ls)
print(mainlist)



# In[6]:


movie_db=pd.DataFrame(mainlist,columns=column)


# In[7]:


movie_db=movie_db.sort_values(by='Rating', ascending=False)


# In[8]:


movie_db.reset_index(level=None, drop=True, inplace=False, col_level=0, col_fill="")


# In[9]:


import sys
get_ipython().system('{sys.executable} -m pip install openpyxl')


# In[11]:


# edit the name u want the data to be saved in. I have used ImdbDataset.xlsx
writer = pd.ExcelWriter('ImdbDataset.xlsx')
movie_db.to_excel(writer)
writer.save()


# In[ ]:




