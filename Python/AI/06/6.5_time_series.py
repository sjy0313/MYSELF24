#!/usr/bin/env python
# coding: utf-8

# # 1. 환경 설정

# In[1]:


# 라이브러리 설정
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns
import random

# 랜덤 시드 고정
SEED=12
random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)  

# 구글 드라이브 폴더 마운트
from google.colab import drive, files
drive.mount('/gdrive')


# # 2. 데이터셋 준비

# In[2]:


# 전력거래소 전력거래가격(SMP) 데이터 다운로드 (2018.1.1. ~ 2020.3.31)
# http://epsis.kpx.or.kr/epsisnew/selectEkmaSmpShdChart.do?menuId=040202

drive_path = "/gdrive/My Drive/"
smp = pd.read_csv(drive_path + "smp/smp.csv")

# 날짜 데이터를 time series 형식으로 변환
smp['date'] = pd.to_datetime(smp['date'])
smp['day_of_week'] = smp['date'].dt.dayofweek

print(smp.shape)   
smp.head()


# In[3]:


# Onehot Encoding
smp['day_of_week'] = smp['day_of_week'].astype('category')
smp = pd.get_dummies(smp, columns = ['day_of_week'], prefix='W', drop_first=True)

smp.head()


# In[4]:


# 그래프 그리기
fig, axes = plt.subplots(4, 1, figsize=(20, 20))

axes[0].plot(smp['date'], smp['smp_max'])
axes[0].set_title('smp_max')

axes[1].plot(smp['date'], smp['smp_mean'])
axes[1].set_title('smp_mean')

axes[2].plot(smp['date'], smp['smp_min'])
axes[2].set_title('smp_min')

axes[3].plot(smp['date'], smp['smp_max'], label='smp_max')
axes[3].plot(smp['date'], smp['smp_mean'], label='smp_mean')
axes[3].plot(smp['date'], smp['smp_min'], label='smp_min')
axes[3].set_title('SMP')
axes[3].legend()

plt.show()


# # 3. 모델 학습

# In[5]:


# Settings
train_split_idx = 729   # 2020.1.1. 행 인덱스 번호  
window_size = 10   # 과거 10일 동안의 시계열 데이터를 학습 데이터로 사용
future = 3     # 3일 이후의 타겟을 예측

# Features 
X_train = smp.iloc[:train_split_idx - window_size - future, 0:]   

# Targets
y_train = smp.iloc[window_size + future :train_split_idx, [3]]  # 'smp_mean' 열

print(X_train.shape, y_train.shape)


# In[6]:


X_train.head(15)


# In[7]:


y_train.head(5)


# In[8]:


# X_test
test_start = train_split_idx - window_size - future  # 테스트 데이터의 시작 행  
test_end = smp.shape[0] - window_size - future
X_test = smp.iloc[test_start:test_end, 0:]

# y_test
# label_start =  + future # 테스트 데이터의 첫 번째 타겟 데이터 위치 
y_test = smp.iloc[train_split_idx:, [3]]  # 'smp_mean' 열 선택

print(X_test.shape, y_test.shape)


# In[9]:


X_test.head(15)


# In[10]:


y_test.head(5)


# In[11]:


# Feature Scaling
X_train_scaled = X_train.loc[:, 'smp_max':]
X_test_scaled = X_test.loc[:, 'smp_max':]

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
scaler.fit(X_train_scaled.values)
X_train_scaled.loc[:, :] = scaler.transform(X_train_scaled.values)
X_test_scaled.loc[:, :] = scaler.transform(X_test_scaled.values)


# In[12]:


# Mini Batch 크기로 시계열을 변환
from tensorflow.keras.preprocessing import timeseries_dataset_from_array
train_data = timeseries_dataset_from_array( 
    X_train_scaled, y_train, sequence_length=window_size, batch_size=16)
test_data = timeseries_dataset_from_array( 
    X_test_scaled, y_test, sequence_length=window_size, batch_size=16)

print(train_data)
print(test_data)


# In[13]:


for batch in test_data.take(1):
    inputs, targets = batch

print("Input:", inputs.numpy().shape)
print("Target:", targets.numpy().shape)


# In[14]:


inputs[0]


# In[15]:


targets[0]


# In[19]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, LSTM, Dense

model = Sequential()
model.add(Input(shape=[10, 9]))

model.add(LSTM(units=32, return_sequences=False)) 
model.add(Dense(units=1, activation='linear'))

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

model.summary()


# In[20]:


# 모델 훈련
history = model.fit(train_data, epochs=500, 
                    validation_data=test_data, 
                    verbose=0)

# 손실 함수 그래프
def plot_loss_curve(history, total_epoch=10, start=1):
    plt.figure(figsize=(5, 5))
    plt.plot(range(start, total_epoch + 1), 
             history.history['loss'][start-1:total_epoch], 
             label='Train')
    plt.plot(range(start, total_epoch + 1), 
             history.history['val_loss'][start-1:total_epoch], 
             label='Validation')
    plt.xlabel('Epochs')
    plt.ylabel('mse')
    plt.legend()
    plt.show()

plot_loss_curve(history=history, 
                total_epoch=len(history.history['loss']), start=1)                   


# In[21]:


y_pred = model.predict(test_data)
y_pred.shape


# In[22]:


plt.figure(figsize=(20, 10))
plt.plot(range(len(y_pred)), y_test[:-(window_size-1)], marker='o', label='y_test')
plt.plot(range(len(y_pred)), y_pred, marker='x', label='y_pred')
plt.legend()
plt.show()


# In[ ]:




