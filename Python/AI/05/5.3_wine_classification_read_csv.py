#!/usr/bin/env python
# coding: utf-8

# # 분석환경 준비
# 입력층과 출력층 사이에 있는 모든 층을 은닉층이라고 함.
# 이 은닉층 사이에는 활성화함수(신경망 층의 선형 방정식의 계산 값에 적용하는 함수)가 존재
#  이진 분류일 경우 시그모이드 함수를 사용하고 다중 분류일 경우 소프트맥스 함수를 사용

# In[ ]:


# 필수 라이브러리
import pandas as pd
import numpy as np
import random
import tensorflow as tf

# 랜덤 시드 고정
SEED=12
random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)  
print("시드 고정: ", SEED)


# In[ ]:


# 구글 드라이브 마운트
# from google.colab import drive
# drive.mount('/gdrive')


# # 데이터 전처리

# In[ ]:


# 데이콘 사이트에서 다운로드한 CSV파일을 읽어오기
# drive_path = "/gdrive/My Drive/"
# drive_path = "./"

train = pd.read_csv( "wine_train.csv")
test = pd.read_csv("wine_test.csv")
submission = pd.read_csv("wine_sample_submission.csv")

print(train.shape, test.shape, submission.shape)
# (5497, 14) (1000, 13) (1000, 2)
#%%

# 칼럼(index) 삭제
train.drop("index", axis=1, inplace=True)
test.drop("index", axis=1, inplace=True)
submission.drop("index", axis=1, inplace=True)


# In[ ]:


train.head(2)


# In[ ]:


submission.head()


# In[ ]:

# while, red
train['type'].value_counts()
'''
type
white    4159
red      1338
Name: count, dtype: int64
'''

# In[ ]:

# type이 white이면 1, red이면 0
#np.where() 함수는 'type' 열의 각 원소가 'white'인지 아닌지를 확인하고, 
#조건에 따라 해당 위치에 1 또는 0을 반환합니다. 
#조건이 만족되면 1을 반환하고, 그렇지 않으면 0을 반환합니다

train['type'] = np.where(train['type']=='white', 1, 0).astype(int)
test['type'] = np.where(test['type']=='white', 1, 0).astype(int)
train['type'].value_counts()
# type
'''
1    4159
0    1338
Name: count, dtype: int64
 '''
# In[ ]:
# 타겟 : 정답
# quality : 3~9까지
train['quality'].value_counts()
'''quality
6    2416
5    1788
7     924
4     186
8     152
3      26
9       5
Name: count, dtype: int64'''
#%%
quality_counts = train['quality'].value_counts()
print(quality_counts.sort_index()) # 시리즈의 인덱스 정렬
'''
quality
3      26
4     186
5    1788
6    2416
7     924
8     152
9       5
Name: count, dtype: int64
'''
# In[ ]:

# 원핫 인코딩: 0,1
# 와인 3~9까지 7등급
# 0~6까지로 7등급으로 변환
# 케라스는 원-핫 인코딩을 수행하는 유용한 도구 to_categorical()를 지원
from tensorflow.keras.utils import to_categorical

y_train = to_categorical(train.loc[:, 'quality'] - 3)
y_train
'''
array([[0., 0., 1., ..., 0., 0., 0.],
       [0., 0., 1., ..., 0., 0., 0.],
       [0., 0., 1., ..., 0., 0., 0.],
       ...,
       [0., 0., 0., ..., 1., 0., 0.],
       [0., 0., 1., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.]])'''

print(type(y_train)) # <class 'numpy.ndarray'>
# In[ ]:


# 피처 선택
X_train = train.loc[:, 'fixed acidity':]
X_test = test.loc[:, 'fixed acidity':]

# 정규화
# 피처 스케일링
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
scaler.fit(X_train)
# 훈련(학습) 데이터 
X_train_scaled = scaler.fit_transform(X_train)

#%%
#이를 테스트 데이터셋에도 동일하게 적용하기 위해 scaler 다시 호출
# 최소/최대 스케일링 
scaler=MinMaxScaler()
scaler.fit(X_test)

# 테스트(검증) 데이터
X_test_scaled = scaler.fit_transform(X_test)

print(X_train_scaled.shape, y_train.shape)
print(X_test_scaled.shape)


# # 신경망 학습

# In[ ]:

print("X_train_scaled.shape: ", X_train_scaled.shape)  # (5497, 12)  

#%%

# 심층 신경망 모델
from tensorflow.keras import Sequential             # 케라스의 신경망 모델 클레스
from tensorflow.keras.layers import Dense, Dropout  # 밀집층을 만드는 클래스

# 활성함수(softmax) : 0~1사의 값으로 다중분류에 사용, 전체를 더하면 1.0(100%)
def build_model(train_data, train_target): 
    model = Sequential() # 모델
    

   # 128: 이 층에 있는 뉴런의 수를 나타냅니다. 즉, 이 층은 128개의 뉴런을 가진 전결합 층입니다. 
   #이 값은 보통 모델의 복잡성을 결정하는 하이퍼파라미터로 조정됩니다. 더 많은 뉴런은 모델의 표현력을 높일 수 있지만,
   #더 많은 계산을 필요로 하고 과적합의 위험이 있습니다.
   
   
   # 입력 신호의 총합을 출력 신호로 변환하는 함수를 일반적으로 활성화 함수라고 합니다.
   #activation='tanh' : 활성화 함수로 하이퍼볼릭 탄젠트(tanh) 함수를 사용한다는 의미
   
    model.add(Dense(128, activation='tanh', input_dim=train_data.shape[1])) # 입력:  12   
    model.add(Dropout(0.2)) # 은닉층 레이어 간의 연결은 제거(20%), 과적합 방지를 위함(20개 정도의 연결망을 끊어버림)
    
    model.add(Dense(64, activation='tanh'))
    model.add(Dropout(0.2))
    
    model.add(Dense(32, activation='tanh'))
    model.add(Dense(train_target.shape[1], activation='softmax')) # 다중분류(확률) : 출력(7)
    
    # shape[1] : 7개 열
# 다중분류 할 시에는 softmax 활용(소프트맥스 함수는 출력층에서 사용되는 함수)
    # RMSprop(Root Mean Square Propagation)
    # 기울기 갱신 지수 가중 이동 평균 학습률 조정
    # 현재 기울기를 해당 이동 평균의 제곱근 나누어...
    # mse : mean squared error -> 손실함수로써 쓰임
    # mae : 평균절대오차(mean absolute error) : 회귀지표로서 쓰임
    
    # metrics(측정항목) : 정확도와 평균절대오차
    
    #즉  - 예측한 값을 실제 값과 빼고 제곱한 값을 평균 내준값(MSE) 방식으로 손실함수에 넣어

#손실점수를 내어 - 옵티마이져를 사용하여  가중치 업데이트해서 값을 내주고  
#훈련하는 동안 모니터링으로 metric 함수를 사용하는데 (MAE)평균 절대 오차로 (실제값과 측정값의 차이를 절대값 내주는 것)  예측값을 측정함

# 손실함수(머신러닝 혹은 딥러닝 모델의 출력값과 사용자가 원하는 출력값의 오차를 의미)
#손실함수는 정답(y)와 예측(^y)를 입력으로 받아 실숫값 점수를 만드는데, 이 점수가 높을수록 모델이 안좋은 것
# MSE는 정답과 예측사이의 차이가 커질수록 오차 n으로 나눈값도 커지므로 모델의 성능이 떨어짐을 알 수 있음
   
    model.compile(optimizer='RMSprop', loss='categorical_crossentropy', 
                metrics=['acc', 'mae']) 

    return model

model = build_model(X_train_scaled, y_train)
model.summary()


# param : 복잡도 

'''
Model: "sequential"
┌─────────────────────────────────┬────────────────────────┬───────────────┐
│ Layer (type)                    │ Output Shape           │       Param # │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense (Dense)                   │ (None, 128)            │         1,664 │ # 입력(12) * 128 + 128
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dropout (Dropout)               │ (None, 128)            │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_1 (Dense)                 │ (None, 64)             │         8,256 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dropout_1 (Dropout)             │ (None, 64)             │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_2 (Dense)                 │ (None, 32)             │         2,080 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_3 (Dense)                 │ (None, 7)              │           231 │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 12,231 (47.78 KB)
 Trainable params: 12,231 (47.78 KB)
 Non-trainable params: 0 (0.00 B)
 
'''
#%%
# option 임. 
# 콜백함수 :  Early Stopping 기법
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import EarlyStopping

X_tr, X_val, y_tr, y_val = train_test_split(X_train_scaled, y_train, test_size=0.15, 
                                            shuffle=True, random_state=SEED)

# 검증손실
# patience 매개변수는 성능 향상을 체크할 에포크 횟수입니다  
# 주어진 에포크 동안 연속하여 검증 데이터에 대한 손신함수가 줄어들지 않으면 학습을 종료한다.
# batch size : 하나의 소그룹에 속하는 데이터 수를 의미
# 전체 트레이닝 셋을 작게 나누는 이유는 트레이닝 데이터를 통째로 신경망에 넣으면 
#비효율적이 리소스 사용으로 학습 시간이 오래 걸리기 때문
#epoch : 전체 트레이닝 셋이 신경망을 통과한 횟수 의미
early_stopping = EarlyStopping(monitor='val_loss',  patience=10)
history = model.fit(X_tr, y_tr, batch_size=64, epochs=200,
                    validation_data=(X_val, y_val),
                    callbacks=[early_stopping],                    
                    verbose=2)


# In[ ]:


# 평가: 테스트 데이터
model.evaluate(X_val, y_val)
# [1.023134708404541, 0.5648484826087952, 0.1610509306192398]
#%%


# In[ ]:


# test 데이터에 대한 예측값 정리
y_pred_proba = model.predict(X_test_scaled)
y_pred_proba[:5]


#%%

# 학습 데이터에 대한 예측값
y_train_pred_proba = model.predict(X_tr)

# np.argmax() : 배열에서 가장 큰 값이 있는 원소의 인덱스
# axis : -1,
# -배열의 마지막 축
# -2차원이면 각 행에 대해서
# -1차원이면 열에 대해서
# 3을 더한이유  : 정답에서 -3을 했기 때문에 다시 3을 더해줌. 
y_train_pred_label = np.argmax(y_train_pred_proba, axis=-1) + 3

loss, acc, mae = model.evaluate(X_tr, y_tr)
print("loss:", loss)
print("accuracy:", acc)
print("mae:", mae)
'''
loss: 1.0009278059005737
accuracy: 0.5734161138534546
mae: 0.16018158197402954
'''

# In[ ]:


y_pred_label = np.argmax(y_pred_proba, axis=-1) + 3
y_pred_label[:5] # array([6, 5, 5, 6, 7], dtype=int64)



# In[ ]:


# 제출양식에 맞게 정리
submission['quality'] = y_pred_label.astype(int)
submission.head()
'''  quality
0        6
1        5
2        5
3        6
4        7'''

# In[ ]:


# 제출파일 저장    
submission.to_csv("wine_dnn_001.csv", index=False)   


# In[ ]:
# 딥러닝에서 에포그(epoch)는 전체 트레이닝 셋이 신경망을 통과한 횟수를 의미 
# if 1-epoch : 전체 트레이닝 셋이 하나의 신경망에 적용되어 순전파와 역전파를 통해 신경망을 한 번 통과했다는 것을 의미

import matplotlib.pyplot as plt

# 훈련손실, 검증손실 비교 그래프
def plot_loss_curve(hist, total_epoch=10, start=1):
    histlen = len(hist.history['loss'])
    print('총 에포크 횟수:', histlen)
    
    total_epoch = total_epoch if total_epoch < histlen else histlen
    
    plt.figure(figsize=(5, 5))
    plt.plot(range(start, total_epoch + 1), 
             hist.history['loss'][start-1:total_epoch], # 훈련손실
             label='Train')
    plt.plot(range(start, total_epoch + 1), 
             hist.history['val_loss'][start-1:total_epoch], # 검증손실
             label='Validation')
    plt.xlabel('Epochs')
    plt.ylabel('mae')
    plt.legend()
    plt.show()
    
    #%%

    #
    plot_loss_curve(history, total_epoch=200, start=1)


    #%%

    # 손실과 정확도

    def plot_acc_curve(hist):
        fig, ax1 = plt.subplots(figsize=(6,4))
        ax1.plot(hist.history['loss'], 'r-', label='loss') # 손실
        ax1.set_ylabel('loss')
        ax1.set_xlabel("Epochs")
        ax1.legend()
        
        ax2 = ax1.twinx()
        ax2.plot(hist.history['val_acc'], 'b-', label='acc') # 정확도
        ax2.set_ylabel('acc')
        ax2.legend()
        plt.show()
        
    #%%    

    plot_acc_curve(history)
        
