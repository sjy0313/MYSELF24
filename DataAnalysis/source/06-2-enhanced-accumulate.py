# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:18:46 2024

@author: Shin
"""
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


# 나눔바른고딕 폰트로 설정합니다.
plt.rc('font', family='NanumBarunGothic')

# 그래프 DPI 기본값을 변경합니다.
plt.rcParams['figure.dpi'] = 100
#%%
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
for_pivot = ns_book7[top30_pubs_idx] # top30 출판사에 해당하는 데이터 중 
# True 인 데이터만 출력.  

# In[6]:
# 상위 30위에 해당하는 '출판사', '발행년도', '대출건수' 열만 추출
# 행 :  상위 30위에 해당하는 출판사
# 열 : '출판사', '발행년도', '대출건수'
ns_book9 = ns_book7[top30_pubs_idx][['출판사', '발행년도', '대출건수']]
#%%
# 집계 : '출판사', '발행년도'별 총 대출건수
# groupby()를 활용하여 '출판사', '발행년도'열을 기준으로 행을 모은 후 sum()로 대출건수 열의 합을 구함
# list안에 열의 이름을 지정.중복되는 연도와 출판사에 대해 sum()을 활용해 대출건수를 구한다.
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
#%%
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
# 하나의 열을 2차원 배열로 바꾸는 것처럼 데이터 구조를 바꾸는 방법
# y축에 넣을 2차원 배열을 만들고 
# 발행년도 열을 리스트 형태로 바꾸어준다.(x축에 넣을 리스트를 만듬.)
# index, columns에 df의 열을 지정해주면 끝 
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
# 열이 다단으로 구성됨. (대출건수, 발행연도)
# In[14]:

# 상위 10개의 출판사이름: x축에 놓을 발행년도의 리스트
top10_pubs = top30_pubs.index[:10]
# x축에 놓을 발행년도의 리스트
# get_level_values()는 판다스의 매서드로
#  multiIndex 일 경우 0이면 첫번 쨰 index에 해당.
# year_cols0= ns_book10.columns.get_level_values(0) # 대출건수 열
year_cols = ns_book10.columns.get_level_values(1) # 발행년도


#%%
# 데이터값 누적하여 그리기

# In[20]:

# 상위 5개 출판사의 2013~2020사이의 대출건수
# ns_book10 : 상위 30개 출판사의 발행년도 별 피봇 테이블 형태
# top10_pubs : 상위 10개 출판사
# 행 : 상위 5개 출판사
# 열 :  2013~2020사이의 대출건수
ns_book10 = ns_book9.pivot_table(index='출판사', columns='발행년도')  
ns10 = ns_book10.loc[top10_pubs[:5], ('대출건수',2013):('대출건수',2020)]


# In[21]:

# 발행 연도별 대출건수가 차례대로 누적됨 , 문학동네 + 믿음사의 대출권수가 합쳐져서 9138이 됨.
# cumsum()에 기본적으로 행을 따라 값을 누적(axis = 0)하는데 만약 열 방향으로 누적을 원한다면 axis = 1 지정.

ns10_cumsum = ns_book10.loc[top10_pubs[:5], ('대출건수',2013):('대출건수',2020)].cumsum()


# In[22]:
# 상위 출판사 부터 하위 출판사까지 대출건수로 누적
# 가장 하위 출판사가 가장 하위 출판사가 큰 값을 가지게 되어 
# df 전체에 cumsum()누적 매서드를 적용
# 누적값이 큰 순서부터 그리게 되면 그보다 작은 값이 덮어짐. 
# 그래프를 그릴 떄 덮어 쓰지 않고 보이도록 하기 위한 처리 
ns_book12 = ns_book10.loc[top10_pubs].cumsum() # 상위 10개 출판사 누적 대출건수
print(len(ns_book12)) # 10 
ns_book12.iloc[0] # 1행 출력. 
ns_book12.iloc[9] # 9행 출력 # 상위 10번 쨰 즉 마지막 출판사 행의 value 값
# In[23]:
# data stacked area graph 
# 마지막 행의 value값을 시작으로 누적을 해주어야 graph 정상출력.
# ns_book12.iloc[9] ~ ns_book12.iloc[0]
fig, ax = plt.subplots(figsize=(8, 6)) # 도화지 생성
# 인덱스의 역순으로 반복
# 가장 하위 출판사
for i in reversed(range(len(ns_book12))):
    bar = ns_book12.iloc[i]     # 행 추출
    label = ns_book12.index[i]  # 출판사 이름 추출
    ax.bar(year_cols, bar, label=label)
    #  출판사별로 각 연도의 대출 건수를 나타내는 막대 그래프를 그리며, 출판사 이름을 레이블로 표시
    print("출판사이름: ", label)
ax.set_title('년도별 대출건수')
ax.legend(loc='upper left')
ax.set_xlim(1985, 2025)
fig.show()
#%%
# 과정
fig, ax = plt.subplots(figsize=(8, 6))  # 도화지 생성
bar = ns_book12.iloc[0]
label = ns_book12.index[0]

ax.bar(year_cols, bar, label=label)
ax.set_title('년도별 대출건수')
ax.legend(loc='upper left')
ax.set_xlim(1985, 2025)

# Set y-axis ticks and labels
y_ticks = range(0, 50001, 10000)
ax.set_yticks(y_ticks)
ax.set_yticklabels([str(y) for y in y_ticks])
'''
ax.set_yticks(y_ticks): 이 코드는 y축 눈금의 위치를 설정합니다. 
y_ticks 변수에는 눈금을 배치할 위치가 포함되어 있습니다.
 이 경우 y_ticks는 0부터 50,000까지 10,000씩 증가하는 범위입니다. 따라서 
 이 코드는 그 특정 위치에 y축 눈금을 설정합니다.

ax.set_yticklabels([str(y) for y in y_ticks]): 이 코드는 y축 눈금의 라벨을 설정합니다. 
이 코드는 라벨의 목록을 입력으로 받습니다. 여기서는 리스트 컴프리헨션을 사용하여 
각 눈금 값을 문자열로 변환합니다. 즉, 이 코드는 해당하는 눈금 값에 대응하는 문자열로 y축 눈금 라벨을 설정합니다.

요약하면, 이 두 줄은 지정된 y_ticks 범위를 기반으로 y축 눈금의 위치와 라벨을 설정합니다.
 이를 통해 플롯에서 y축의 모양을 사용자 정의할 수 있습니다.
'''
plt.show()
# ## 원 그래프 그리기

# In[24]:


data = top30_pubs[:10]
labels = top30_pubs.index[:10]


# In[25]:

#pi-graph 그리기
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(data, labels=labels)
ax.set_title('출판사 도서비율')
fig.show()


# In[26]:

# startangle : 90(12시 방향부터 시작)
plt.pie([10,9], labels=['A제품', 'B제품'], startangle=90)
plt.title('제품의 매출비율')
plt.show()


# In[27]:

# autopct매서드는 파이썬 %연산자에 적용할 포멧팅 문자열을 전달 할 수 있다.
# (%d)를 전달하면 각 부채꼴의 비율이 정수로 표시
# 파이그래프에서 마지막에 퍼센트 기호를 추가하기 위해 % 한번 더
# %.1f%%

# .1f는 소수점 첫쨰 자리까지만 표시하라는 의미 
# 비율을 표시하는 부채꼴 강조
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(data, labels=labels, startangle=90,
       autopct='%.1f%%', explode=[0.1]+[0]*9)
ax.set_title('출판사 도서비율')
fig.show()

# explode : 첫 번쨰는 0.1, 나머지는 0인 파이썬 리스트
explode=[0.1]+[0]*9
print(explode) # [0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#%%

explode = [0.2,0,0,0,0,0.1,0,0,0,0]
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(data, labels=labels, startangle=90,
       autopct='%.1f%%', explode=explode)
ax.set_title('출판사 도서비율')
fig.show()


# ## 여러 종류의 그래프가 있는 서브플롯 그리기

# In[28]:
# 비교하여 설명할 떄는 이런 식으로 여러개의 그래프를 한 번에 띄어놓고 작성.
# subplots(nrows=1, ncols=1) # 기본값
# 2행 2열의 그래프 # 총 4개의 그래프 
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
# 위에 진행해 보았던 것 보다 간결해진 코딩
# ### 스택 영역 그래프 그리기

# In[29]:

# 연도별/출판사들의 대출건수 
ns_book11 = ns_book9.pivot_table(index='발행년도', columns='출판사', values='대출건수')
ns_book11.loc[2000:2005] # 2000~2005년 사이의 출판사별 대출건수
# 이전과 달리 pivot_table()매서드의 values매개변수에 집계할 열을 지정

# In[30]:


import numpy as np
#  aggfunc=np.sum : 집계(aggregation function 함수들의 집합)
# groupby() 매서드와 pivot_table()매서드는 값을 집계한다느 점에서 매우 비슷
# 만들어진 결과는 다르다. 
# ns_book9 df는 groupby()매서드로 집계한 결과이며
# ns_book10 = ns_book9.pivot_table(index='출판사', columns='발행년도')
# 출판사마다 발행년도 열에 하나의 값만 있으므로 ns_10d을 만들 떄 value매개변수 필요x
# 
ns_book11 = ns_book7[top30_pubs_idx].pivot_table(
    index='발행년도', columns='출판사', 
    values='대출건수', aggfunc=np.sum) 
ns_book11.loc[2000:2005]


# In[31]:
# df에서 plot.area()를 호출하여 스택 영역 그래프를 그릴 수 있다. 
# 서브플롯을 명시적으로 만든 경우 area()매서드의 
# ax매개변수에 matplotlib의 axes객체를 전달
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
