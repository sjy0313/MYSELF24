#!/usr/bin/env python
# coding: utf-8

# # 1. 환경 설정
# IMDB : 영화 리뷰 데이터 셋, 관객들이 영화에 남긴 리뷰(말뭉치)
# 목표 레이블: 1(긍정), 0(부정)
# 훈련 데이터: 25,000개
# 검증 데이터: 25,000개
# 단어 갯수  : 10,000개, 가장 많이 사용된 단어 10,000 선택  

#%%
# LSTM
"""
장단기 메모리(Long Short-Term Memory, LSTM)는 순환 신경망(RNN) 기법의 하나로 셀, 
입력 게이트, 출력 게이트, 망각 게이트를 이용해 기존 순환 신경망(RNN)의 문제인 
기울기 소멸 문제(vanishing gradient problem)를 방지하도록 개발된 모델
"""
#https://dgkim5360.tistory.com/entry/understanding-long-short-term-memory-lstm-kr

# LSTM은 RNN의 한 종류로서 긴 의존 기간을 필요로 하는 학습을 수행할 능력을 갖고 있다
'''
LSTM은 긴 의존 기간의 문제를 피하기 위해 명시적으로(explicitly) 설계되었다.
 긴 시간 동안의 정보를 기억하는 것은 모델의 기본적인 행동이어야지, 모델이 
 그것을 배우기 위해서 몸부림치지 않도록 한 것이다!'''

# 두 모델 모두 시계열 데이터를 다루는데 쓰이지만 다른점으로는: 
    #RNNs: 
        # - 시계열 정보 즉, 과거의 정보를 시간순으로 기억하는데에 적합한 모델
        # - recurrent units[네트워크 이전의 정보를 기억하고, 새로운 입력이 주어질 때 
        #이전 상태와 결합하여 출력을 생성할 수 있게함] 의 한layer는 비교적 간단한 구조를
        # 가져 장기데이터 즉, 시퀀스의 길이가 길어질 수 록 기울기 소실 묹제가 발생하는데
        # 이는 오랜시간 동안 반영된 정보가 소실되어 성능 저하를 일으킴. 
        # RNN은 또한 시퀀스의 길이에 따라 파라미터 수가 증가하는 경향이 있어
        # 과접합 문제가 발생할 수 있으며 이를 해결하기 위해 많은 데이터와 복잡한 모델구조가 필요
        # Long-term dependency(장기의존성)을 학습하는데 어려움이 있음-> 이는 시퀀스가 길어지면 이전의
        # 정보가 희석되어 장기적인 의존성 파악하는데 어려움 겪어.
        
        # rnn모델의 한계를 극복 위해 LSTM AND GRU 같은 변형모델 개발됨.
        #  RNN : https://doooob.tistory.com/158
      

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


#%%
# # 2. 데이터셋 준비

# IMDb 영화 리뷰 데이터셋
from tensorflow.keras import datasets
imdb = datasets.imdb

# index_from : 기본값 3
# 토큰값 : 0(패딩) ->시퀀스의 길이를 동일하게 맞추기 위해 사용 , 1(문장의 시작), 2(어휘 사전에 없는 단어)
# 기본적으로, IMDB 데이터셋은 각 리뷰를 단어의 시퀀스로 변환하고, 각 단어는 고유한 정수 인덱스에 매핑됩니다.

(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=10000, index_from=3)
#원래 데이터셋에 있는 각 단어 인덱스에 3이 더해집니다  이는 특별한 토큰들을 위한 공간을 만들기 위해서
# 이렇게 하면 모델이 텍스트 데이터를 더 잘 처리하고, 특별한 상황을 인식할 수 있게 도와줍니다.
(X_train2, y_train2), (X_test2, y_test2) = imdb.load_data(num_words=10000, index_from=0)

print(X_train.shape, y_train.shape, X_test.shape, y_test.shape) 
# (25000,) (25000,) (25000,) (25000,)

#%%

# 첫번째 리뷰 - 벡터
print(X_train[0])

# 각 요소의 타입
print("type: ", type(X_train[0])) # <class 'list'>

# # 첫번째 리뷰 - 벡터 길의 (원소 개수)
print("len: ",  len(X_train[0]))  # 218


# In[5]:

# 단어가 인코딩 인덱스
# 단어가 어떤 숫자 인덱스로 인코딩
# 단어와 숫자 인덱스는 딕셔너리 형태
# dict : { 단어: 숫자, ... }
word_index = imdb.get_word_index()
word_index

#%%
print(word_index['the'])  # 1
print(word_index['zeon']) # 23385

# In[6]:

# 첫번째 리뷰 디코딩
review_vector = X_train[0]

# {단어:인덱스} -> {인덱스:단어}
index_to_word = { value:key for key, value in word_index.items() }

#%%

# 키가 없는 경우 '?' 처리
# q = index_to_word.get(1 - 3, '?')
# print(q)

#%%

# 인덱스로 디코딩된 데이터에서 인덱스 값을 꺼냄
# 인덱스 - 3을 하여 그 값으로 dict({인덱스:단어})에서 단어를 추출하여 리스트로 구성
# 리스트에서 각 단어를 하나씩 꺼내서 공백을 넣어 문자열로 구성
# 결과: 처음 입력한 영화 리뷰 데이터로 복원
# 문장의 맨 처음은 시작부호인 '?'로 시작
decoded_review = ' '.join([ index_to_word.get(idx - 3, '?') for idx in review_vector ])

print(decoded_review)

#%%

# dict에서 키값 찾기
dt = { 1:'a', 2:'b', 3:'c'}
# print(dt[0])   # dict에서 없는 키를 찾으면 종료 : KeyError: 0
print(dt.get(0)) # None
print(dt.get(-1, '없음')) # 키값이 없는 경우 디폴값을 지정 : '없음' 출력

#%%

# 숫자 벡터를 텍스트로 변환
def decode_review_vector(review_vector):
    index_to_word = {value:key for key, value in word_index.items()}
    decoded_review = ' '.join([index_to_word.get(idx - 3, '?') for idx in review_vector])
    return decoded_review

# 첫번째 리뷰 디코딩
decode_review_vector(X_train[0])


#%%

# 첫번째 리뷰의 정답 레이블 
y_train[0] # 1, 긍정


#%%
# 3. 데이터 전처리

# 각 리뷰의 단어 개수 분포
# 대부분 1000단어 미만, 100~250개의 단어로 구성된 리뷰
review_length = [len(review) for review in X_train]
sns.displot(review_length);


# In[9]:


# Padding
# 앞에 패딩(0)
max_words = 250
from tensorflow.keras.preprocessing import sequence
X_train_pad = sequence.pad_sequences(X_train, maxlen=max_words)
X_test_pad = sequence.pad_sequences(X_test, maxlen=max_words)

# 250 - 218 = 32개는 0으로 패딩 + 원래 데이터 
print(f"max_words({max_words}) - word({len(X_train[0])}) = {max_words - len(X_train[0])}")
print(X_train_pad[0]) 

#%%
# 4. 모델 학습

# 모델 정의
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.layers import Embedding, SimpleRNN, LSTM, GRU

def build_model(model_type='RNN'):
    model = Sequential()
    # Embedding
    # input_dim: 10000, 단어 사전의 크기
    # output_dim: 128, 출력 크기
    model.add(Embedding(input_dim=10000, output_dim=128))
    
    # RNN
    if model_type=='RNN':
        model.add(SimpleRNN(units=64, return_sequences=True)) 
        model.add(SimpleRNN(units=64)) 
    # LSTM
    elif model_type=='LSTM':
        model.add(LSTM(units=64, return_sequences=True)) 
        model.add(LSTM(units=64)) 
    # GRU
    elif model_type=='GRU':
        model.add(GRU(units=64, return_sequences=True)) 
        model.add(GRU(units=64))    

    # Dense Classifier
    model.add(Dense(units=32, activation='relu'))
    model.add(Dropout(rate=0.5))
    model.add(Dense(units=1, activation='sigmoid')) # 출력갯수 2개: 0, 1

    # Compile
    model.compile(optimizer='adam', 
                loss='binary_crossentropy', 
                metrics=['accuracy'])

    return model


# In[11]:


# embedding_1 (Embedding) (None, None, 128) 1280000   
# -> 1,280,000 = 어휘(10000) * output_dim(128)
# simple_rnn_2 (SimpleRNN) (None, None, 64) 12352    
# 12352 = 128 * 64 + 64 * 64 + 64

# In[13]:


# 20 epoch 까지 손실함수와 정확도를 그래프로 나타내는 함수

def plot_metrics(history, start=1, end=20):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    # Loss: 손실 함수
    axes[0].plot(range(start, end+1), history.history['loss'][start-1:end], 
                label='Train')
    axes[0].plot(range(start, end+1), history.history['val_loss'][start-1:end], 
                label='Validation')
    axes[0].set_title('Loss')
    axes[0].legend()
    # Accuraccy: 예측 정확도
    axes[1].plot(range(start, end+1), history.history['accuracy'][start-1:end], 
                label='Train')
    axes[1].plot(range(start, end+1), history.history['val_accuracy'][start-1:end], 
                label='Validation')
    axes[1].set_title('Accuracy')
    axes[1].legend()
plt.show()

#%%

# LSTM 모델 적용
lstm_model = build_model('LSTM')

lstm_history = lstm_model.fit(X_train_pad, y_train, batch_size=32, epochs=10,
                        validation_split=0.1, verbose=0) 

plot_metrics(history=lstm_history, start=1, end=10)   

#%%
# THE END