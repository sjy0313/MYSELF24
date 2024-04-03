# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:51:45 2024

@author: Shin

"""
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 100


# In[2]:


plt.plot([1, 4, 9, 16])
plt.title('simple line graph')
plt.show()


# In[3]:


fig, ax = plt.subplots()
ax.plot([1, 4, 9, 16])
ax.set_title('simple line graph')
fig.show()
#%%


import matplotlib.pyplot as plt
# 01 : 지정된 폴더에서 설치된 폰트 꺼내서 matplotlip 그래프에 적용
import matplotlib.font_manager as fm
from matplotlib import rc
# set the default font for Matplotlib to a font file located at./NanumBarunGothic.ttf"
font_path = "./NanumBarunGothic.ttf"

font_name = fm.FontProperties(fname=font_path).get_name()
print(font_name)
rc('font', family=font_name) 
# 02 : windows > fonts 폴더에서 폰트 꺼내서 적용하기
# font_files = fm.findSystemFonts(fontpaths=['C:/Windows/Fonts'])
font_files = fm.findSystemFonts(fontpaths=['C:/Users/Shin/AppData/Local/Microsoft/Windows/Fonts'])
for fpath in font_files:
        print(fpath)
        fm.fontManager.addfont(fpath)

#%%

#plt.rcParams['font.family'] = 'NanumGothic'
#plt.rcParams['font.family'] = 'NanumSquare'
plt.rcParams['font.family'] = 'NanumBarunGothic'

plt.plot([1, 4, 9, 16])
plt.title('간단한 선 그래프')
plt.show()