#!/usr/bin/env python
# coding: utf-8

# # 06-2 맷플롯립의 고급 기능 배우기

# <table class="tfo-notebook-buttons" align="left">
#   <td>
#     <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/06-2.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />주피터 노트북 뷰어로 보기</a>
#   </td>
#   <td>
#     <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/06-2.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />구글 코랩(Colab)에서 실행하기</a>
#   </td>
# </table>

# ## 실습 준비하기

# 이 노트북은 맷플롯립 그래프에 한글을 쓰기 위해 나눔 폰트를 사용합니다. 코랩의 경우 다음 셀에서 나눔 폰트를 직접 설치합니다.

# In[1]:


# 노트북이 코랩에서 실행 중인지 체크합니다.
'''
import sys
if 'google.colab' in sys.modules:
    get_ipython().system("echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections")
    # 나눔 폰트를 설치합니다.
    get_ipython().system('sudo apt-get -qq -y install fonts-nanum')
    import matplotlib.font_manager as fm
    font_files = fm.findSystemFonts(fontpaths=['/usr/share/fonts/truetype/nanum'])
    for fpath in font_files:
        fm.fontManager.addfont(fpath)
'''
#%%
import matplotlib.pyplot as plt

import matplotlib.font_manager as fm
from matplotlib import rc
# set the default font for Matplotlib to a font file located at./NanumBarunGothic.ttf"
font_path = "./NanumBarunGothic.ttf"

font_name = fm.FontProperties(fname=font_path).get_name()
print(font_name)
rc('font', family=font_name) 
plt.rcParams['font.family'] = 'NanumBarunGothic'

plt.plot([1, 4, 9, 16])
plt.title('간단한 선 그래프')
plt.show()


# 나눔바른고딕 폰트로 설정합니다.
plt.rc('font', family='NanumBarunGothic')

# 그래프 DPI 기본값을 변경합니다.
plt.rcParams['figure.dpi'] = 100


# In[3]:


import gdown

gdown.download('https://bit.ly/3pK7iuu', './data/ns_book7.csv', quiet=False)


# In[4]:


import pandas as pd

ns_book7 = pd.read_csv('ns_book7.csv', low_memory=False)
ns_book7.head()


# ## 하나의 피겨에 여러 개의 선 그래프 그리기

# In[5]:

# 상위 30개 출판사 true표시하여 boolean array출력
#%%
# 21875개의 출판사 별 책의 권 수 
pubs_count = ns_book7['출판사'].value_counts() 
#%%
# 상위 30개 출판
top30_pubs = ns_book7['출판사'].value_counts()[:30]
# 출판사 별 상위 30개에 해당하는 데이터는 True 그렇지 않으면 False
top30_pubs_idx = ns_book7['출판사'].isin(top30_pubs.index)


# In[6]:
# 상위 30위에 해당하는 '출판사', '발행년도', '대출건수' 열만 추출
# 행 :  상위 30위에 해당하는 출판사
# 열 : '출판사', '발행년도', '대출건수'
ns_book9 = ns_book7[top30_pubs_idx][['출판사', '발행년도', '대출건수']]
#%%
# 집계 : '출판사', '발행년도'별 총 대출건수
# groupby()를 활용하여 '출판사', '발행년도'열을 기준으로 행을 모은 후 sum()로 대출건수 열의 합을 구함
# 51886개의 데이터에서 886개로 축소되었다. 
ns_book9 = ns_book9.groupby(by=['출판사', '발행년도']).sum()

# In[7]:

# 
ns_book9 = ns_book9.reset_index()
ns_book9[ns_book9['출판사'] == '황금가지'].head() # 황금가지 출판사 선 그래프 
ns_book9[ns_book9['출판사'] == '비룡소'].head()

# In[8]:


line1 = ns_book9[ns_book9['출판사'] == '황금가지']
line2 = ns_book9[ns_book9['출판사'] == '비룡소']


# In[9]:

# 황금가지 : 파란색
# 비룡소 : 주황색
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(line1['발행년도'], line1['대출건수'])
ax.plot(line2['발행년도'], line2['대출건수'])
ax.set_title('년도별 대출건수')
fig.show()


# In[10]:

# ax.legend() 범례를 추가하고 plot함수에 label을 추가하면 두 선 그래프의 범례가 
# 오른쪽 위에 뜬다.
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(line1['발행년도'], line1['대출건수'], label='황금가지')
ax.plot(line2['발행년도'], line2['대출건수'], label='비룡소')
ax.set_title('년도별 대출건수')
ax.legend()
fig.show()


# In[11]:

# 상위 5개의 출판사 선택 , label=pub -> 5개출판사에 해당
# 선 그래프 5개 그리기 (중요)
fig, ax = plt.subplots(figsize=(8, 6))
for pub in top30_pubs.index[:5]:
    line = ns_book9[ns_book9['출판사'] == pub] 
    ax.plot(line['발행년도'], line['대출건수'], label=pub)
ax.set_title('년도별 대출건수')
ax.legend() # 범례 
ax.set_xlim(1985, 2025) # 그래프를 출력할 x축의 좌표 범위 지정 
fig.show()
# x,y축 동시에 설정 plt.axis([1985, 2025, 0, 13000])

# In[12]:
# pivot table(피벗 테이블) 
# 하나의 열을 2차원 배열로 바꾸는 것처럼 데이터 구조를 바꾸어줌.
# index, col
ns_book10 = ns_book9.pivot_table(index='출판사', columns='발행년도')
ns_book10.head()
# 발행 연도 별 대출건수

# In[13]:


ns_book10.columns[:10] 
'''
MultiIndex([('대출건수', 1947.0),
            ('대출건수', 1974.0),
            ('대출건수', 1975.0),
            ('대출건수', 1976.0),
            ('대출건수', 1977.0),
            ('대출건수', 1978.0),
            ('대출건수', 1979.0),
            ('대출건수', 1980.0),
            ('대출건수', 1981.0),
            ('대출건수', 1982.0)],
           names=[None, '발행년도'])
'''

# In[14]:


top10_pubs = top30_pubs.index[:10]
year_cols0= ns_book10.columns.get_level_values(0)
year_cols = ns_book10.columns.get_level_values(1)


# In[15]:
#
# 스택 영역 그래프(stacked area graph) 선그래프 위에 다른 선 그래프를 차례대로 
# 쌓는 것. 그래프 사이의 간격이 y축의 값이 된다. 
# 예시)
import matplotlib.pyplot as plt
import numpy as np

# data from https://allisonhorst.github.io/palmerpenguins/

species = (
    "Adelie\n $\\mu=$3700.66g",
    "Chinstrap\n $\\mu=$3733.09g",
    "Gentoo\n $\\mu=5076.02g$",
)
weight_counts = {
    "Below": np.array([70, 31, 58]),
    "Above": np.array([82, 37, 66]),
}
width = 0.5

fig, ax = plt.subplots()
bottom = np.zeros(3)
# key : boolean, value : weight_count
for boolean, weight_count in weight_counts.items():
    p = ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count

ax.set_title("Number of penguins with above average body mass")
ax.legend(loc="upper right")

plt.show()
#%%
# ns_book10 : 상위 10개 출판사 기준 발행년도(피벗)별 대출건수
# year_cols : 발행연도
# top10_pubs : 상위 10개 출판사
print(top10_pubs)
# 상위 10개 출판사 순위 : 문학동네, ... , 한울

#%%

# 폰트 출력이 안될 시(나눔바른고딕 다운로드 필요 없으면),
import matplotlib.font_manager as fm
from matplotlib import rc
# set the default font for Matplotlib to a font file located at./NanumBarunGothic.ttf"
font_path = "./NanumBarunGothic.ttf"

font_name = fm.FontProperties(fname=font_path).get_name()
print(font_name)
rc('font', family=font_name) 
#%%
# 스택영역 그래프(stacked area graph)
fig, ax = plt.subplots(figsize=(8, 6))
ax.stackplot(year_cols, ns_book10.loc[top10_pubs].fillna(0), labels=top10_pubs)
ax.set_title('년도별 대출건수')
#ax.legend(loc='upper left') # 범례 위치 실정 
ax.legend(loc='upper right')
ax.set_xlim(1985, 2025) #x축 범위 설정
fig.show()

#%%

#하나의 피겨에 여러 개의 막대 그래프 그리기

fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(line1['발행년도'], line1['대출건수'], label='황금가지')
ax.bar(line2['발행년도'], line2['대출건수'], label='비룡소')
ax.set_title('년도별 대출건수')
ax.legend() # 범례 추가 
fig.show()


# In[17]:


fig, ax = plt.subplots(figsize=(8, 6))
# 비교가능하게 line gragh x축 기준 +-0.2만큼 이동시킴, 막대 너비 0.4설정
ax.bar(line1['발행년도']-0.2, line1['대출건수'], width=0.4, label='황금가지')
ax.bar(line2['발행년도']+0.2, line2['대출건수'], width=0.4, label='비룡소')
ax.set_title('년도별 대출건수')
ax.legend()
fig.show()


# In[18]:

# 스택 막대 그래프
# bottom매서드를 사용하여 수동으로 막대를 쌓을 수 있다.
# height1을 bottom으로 정의하고 height2를 그 위에 쌓는다.

height1 = [5, 4, 7, 9, 8]
height2 = [3, 2, 4, 1, 2]

plt.bar(range(5), height1, width=0.5)
plt.bar(range(5), height2, bottom=height1, width=0.5)
plt.show()


# In[19]:

# height3 를 먼저 그리고 height1을 그린다.
# 리스트 내포를 사용하여 zip()를 활용하여 양쪽의 데이터를 하나 씩 엮어준다.
# 막대의 길이를 누적해서 그림. 
height3 = [a + b for a, b in zip(height1, height2)]

plt.bar(range(5), height3, width=0.5)
plt.bar(range(5), height1, width=0.5)
plt.show()


# ### 데이터값 누적하여 그리기

# In[20]:

# 상위 5개 출판사의 
ns10 = ns_book10.loc[top10_pubs[:5], ('대출건수',2013):('대출건수',2020)]


# In[21]:


ns_book10.loc[top10_pubs[:5], ('대출건수',2013):('대출건수',2020)].cumsum()


# In[22]:


ns_book12 = ns_book10.loc[top10_pubs].cumsum()


# In[23]:


fig, ax = plt.subplots(figsize=(8, 6))
for i in reversed(range(len(ns_book12))):
    bar = ns_book12.iloc[i]     # 행 추출
    label = ns_book12.index[i]  # 출판사 이름 추출
    ax.bar(year_cols, bar, label=label)
ax.set_title('년도별 대출건수')
ax.legend(loc='upper left')
ax.set_xlim(1985, 2025)
fig.show()


# ## 원 그래프 그리기

# In[24]:


data = top30_pubs[:10]
labels = top30_pubs.index[:10]


# In[25]:


fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(data, labels=labels)
ax.set_title('출판사 도서비율')
fig.show()


# In[26]:


plt.pie([10,9], labels=['A제품', 'B제품'], startangle=90)
plt.title('제품의 매출비율')
plt.show()


# In[27]:


fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(data, labels=labels, startangle=90,
       autopct='%.1f%%', explode=[0.1]+[0]*9)
ax.set_title('출판사 도서비율')
fig.show()


# ## 여러 종류의 그래프가 있는 서브플롯 그리기

# In[28]:


fig, axes = plt.subplots(2, 2, figsize=(20, 16))

# 산점도
ns_book8 = ns_book7[top30_pubs_idx].sample(1000, random_state=42)
sc = axes[0, 0].scatter(ns_book8['발행년도'], ns_book8['출판사'], 
                        linewidths=0.5, edgecolors='k', alpha=0.3,
                        s=ns_book8['대출건수'], c=ns_book8['대출건수'], cmap='jet')
axes[0, 0].set_title('출판사별 발행도서')
fig.colorbar(sc, ax=axes[0, 0])

# 스택 선 그래프
axes[0, 1].stackplot(year_cols, ns_book10.loc[top10_pubs].fillna(0), 
                     labels=top10_pubs)
axes[0, 1].set_title('년도별 대출건수')
axes[0, 1].legend(loc='upper left')
axes[0, 1].set_xlim(1985, 2025)

# 스택 막대 그래프
for i in reversed(range(len(ns_book12))):
    bar = ns_book12.iloc[i]     # 행 추출
    label = ns_book12.index[i]  # 출판사 이름 추출
    axes[1, 0].bar(year_cols, bar, label=label)
axes[1, 0].set_title('년도별 대출건수')
axes[1, 0].legend(loc='upper left')
axes[1, 0].set_xlim(1985, 2025)

# 원 그래프
axes[1, 1].pie(data, labels=labels, startangle=90,
               autopct='%.1f%%', explode=[0.1]+[0]*9)
axes[1, 1].set_title('출판사 도서비율')

fig.savefig('all_in_one.png')
fig.show()


# ## 판다스로 여러 개의 그래프 그리기

# ### 스택 영역 그래프 그리기

# In[29]:


ns_book11 = ns_book9.pivot_table(index='발행년도', columns='출판사', values='대출건수')
ns_book11.loc[2000:2005]


# In[30]:


import numpy as np

ns_book11 = ns_book7[top30_pubs_idx].pivot_table(
    index='발행년도', columns='출판사', 
    values='대출건수', aggfunc=np.sum)
ns_book11.loc[2000:2005]


# In[31]:


fig, ax = plt.subplots(figsize=(8, 6))
ns_book11[top10_pubs].plot.area(ax=ax, title='년도별 대출건수',
                                xlim=(1985, 2025))
ax.legend(loc='upper left')
fig.show()


# ### 스택 막대 그래프 그리기

# In[32]:


fig, ax = plt.subplots(figsize=(8, 6))
ns_book11.loc[1985:2025, top10_pubs].plot.bar(
    ax=ax, title='년도별 대출건수', stacked=True, width=0.8)
ax.legend(loc='upper left')
fig.show()

