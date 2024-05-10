#!/usr/bin/env python
# coding: utf-8

# PART 06 딥러닝 응용
# 이미지 분류: Fashion MNIST 의류 클래스 판별
"""
이미지갯수 : 60,000개
이미지크기 : 784 = 28 * 28
이미지종류 : 0~9까지
"""
# CNN 개념 이해 : 
#https://wikidocs.net/64066
# In[ ]:


# 라이브러리 설정
import pandas as pd
import numpy as np
import tensorflow as tf
import random

#%%
# 랜덤 시드 고정
SEED=12
random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)  

#%%

# # 2. 데이터셋 준비

# In[ ]:


# 데이콘 사이트에서 다운로드한 CSV파일을 읽어오기
drive_path = "./fashion_mnist/data/"
train = pd.read_csv(drive_path + "train.csv")
test = pd.read_csv(drive_path + "test.csv")
submission = pd.read_csv(drive_path + "sample_submission.csv")

print(train.shape, test.shape, submission.shape)   


# In[ ]:


# train 데이터 보기
# label, pixel1, ... pixel784
train.head()


# In[ ]:


# train 데이터를 28*28 이미지로 변환
train_images = train.loc[:, 'pixel1':].values.reshape(-1, 28, 28)
train_images.shape # (60000, 28, 28)


# In[ ]:


# 첫번째 이미지 출력
import matplotlib.pyplot as plt
plt.imshow(train_images[0]);

print("train_images.shape:", train_images.shape)

#%%

imglen = train_images.shape[0]
print("이미지 갯수: ", imglen)    

#%%

fig, axs = plt.subplots(8, 8, figsize=(12,12))
for i in range(8):
    for j in range(8):
        axs[i,j].imshow(train_images[i*8+j])
        axs[i,j].axis('off')
    
plt.show()    


# In[ ]:


# 목표 레이블  : 정답
y_train = train.loc[:, 'label']
y_train_unique = y_train.unique()
print(y_train_unique) # [2 9 6 0 3 4 5 8 7 1]
print(sorted(y_train_unique)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(np.sort(y_train_unique)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# In[ ]:

# 숫자 레이블을 실제 레이블과 연결하여 확인
target_values = {0: 'T-shirt/top', 
                 1: 'Trouser', 
                 2: 'Pullover', 
                 3: 'Dress', 
                 4: 'Coat', 
                 5: 'Sandal', 
                 6: 'Shirt', 
                 7: 'Sneaker', 
                 8: 'Bag', 
                 9: 'Ankle boot'}
print(y_train[0]) # 2 
print(target_values[y_train[0]]) # Pullover

#%%

# test 데이터를 28*28 이미지로 변환
test_images = test.loc[:, 'pixel1':].values.reshape(-1, 28, 28)
test_images.shape # (10000, 28, 28)


# In[ ]:


# 500번째 test 이미지를 출력
plt.imshow(test_images[499]);


#%%

###############################################################################
# # 2. 데이터 전처리 (Pre-processing)
###############################################################################

# 정규화
# 피처 스케일 맞추기 
# 이미지 픽셀의 값(컬러) : 0~255
# 각각의 픽셀 값에 대해 255로 나누어주기
X_train = train_images / 255. 
X_test = test_images / 255.
print("최소값:", X_train[0].min()) # 0.0
print("최대값:", X_train[0].max()) # 1.0

#%%

print("최소값:", X_train.min()) # 0.0
print("최대값:", X_train.max()) # 1.0

#%%

# CNN(합성곱 신경망) : 3채널(Red, Green, Blue)
# 합성공 신명망(CNN)은 RGB 채널 값을 입력받은 것은 전제로 설계 됨

# 채널 차원 추가: 색상채널
# 차원 또는 축(axis)를 추가시키려면 np.expand_dim 함수를 사용한다. 
# axis=0 이면 행축 추가
# axis=1 이면 열축 추가
# axis=-1 이면 마지막 축 추가를 의미한다.
print("변환 전:", X_train.shape, X_test.shape) # (60000, 28, 28) (10000, 28, 28)
X_train = np.expand_dims(X_train, axis=-1)
X_test = np.expand_dims(X_test, axis=-1)
print("변환 후:", X_train.shape, X_test.shape) # (60000, 28, 28, 1) (10000, 28, 28, 1)


# In[ ]:

# 폴드아웃 교차검증
# Train - Validation 데이터 구분
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val =  train_test_split(X_train, y_train, test_size=0.2, 
                                             stratify=y_train, 
                                             shuffle=True, random_state=SEED)
print("학습 데이터셋 크기: ", X_tr.shape, y_tr.shape)
print("검증 데이터셋 크기: ", X_val.shape, y_val.shape)


#%%
# 3. 모델 구축
# MLP 모델

#%%
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense

# History 객체. 
# History.history 속성은 연속된 세대에 걸친 학습 손실 값과 측정항목 값,
# 그리고 (적용 가능한 경우) 검증 손실 값과 검증 측정항목 값의 기록입니다.

# 손실 함수 그래프
def plot_loss_curve(history, total_epoch=10, start=1):
    plt.figure(figsize=(5, 5))
    plt.plot(range(start, total_epoch + 1), 
             history.history['loss'][start-1:total_epoch], # 손실값
             label='Train')
    plt.plot(range(start, total_epoch + 1), 
             history.history['val_loss'][start-1:total_epoch], # 검증손실값
             label='Validation')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

#%%

#######################################################################
# CNN 활용

#%%
#모델을 컴파일하는 것은 모델이 학습 과정에서 사용할 몇 가지 추가적인 설
#정을 지정하는 과정입니다. 주요한 설정으로는 다음과 같습니다:
'''
옵티마이저(optimizer) 지정: 옵티마이저는 모델이 손실 함수를 최소화하기 위해 가중치를
업데이트하는 방법을 결정합니다. 예를 들어, Adam, RMSprop, SGD 등이 있습니다.
이 설정은 모델이 어떻게 학습될지에 직접적인 영향을 줍니다.
손실 함수(loss function) 지정: 손실 함수는 모델의 출력과 실제 값 사이의 차이를 측정합니다.
모델이 훈련 중에 이 손실을 최소화하도록 학습됩니다. 회귀 문제의 경우에는 
평균 제곱 오차(Mean Squared Error, MSE)를 주로 사용하고, 분류 문제의 경우에는 
교차 엔트로피(cross-entropy) 계열의 손실 함수를 사용합니다.
평가 지표(metrics) 설정: 훈련 및 평가 중에 모델의 성능을 평가하기 위한 지표를 지정합니다.
일반적으로 정확도(accuracy)를 사용하지만, 다른 지표도 가능합니다.   
'''  
    
from tensorflow.keras.layers import Conv2D, MaxPooling2D
cnn_model = Sequential()
cnn_model.add(Conv2D(filters=16,         # 필터(뉴런) 4*4 필터
                     kernel_size=(3, 3), # 커널(3*3) : 입력에 곱해지는 가중치( = hyperparameter)
                     # 결과의 크기를 알 수 있음.
                     activation='relu', 
                     input_shape=[28, 28, 1]))
cnn_model.add(MaxPooling2D(pool_size=(2, 2)))
 #pooling은 matrix 연산을 사용하지 않고 각 pixel에서 하나의 값을 뽑아내는 과정
 #pooling은 overfitting을 방지하기 위함
# https://hobinjeong.medium.com/cnn%EC%97%90%EC%84%9C-pooling%EC%9D%B4%EB%9E%80-c4e01aa83c83
# 
# https://miro.medium.com/v2/resize:fit:720/format:webp/1*O06nY1U7zoP4vE5AZEnxKA.gif
#이 층은 2x2 크기의 윈도우로 입력을 스캔하고,
# 각 윈도우에서 가장 큰 값을 선택하여 입력을 다운샘플링합니다.
cnn_model.add(Flatten())
cnn_model.add(Dense(units=64, activation='relu'))
cnn_model.add(Dense(units=10, activation='softmax'))
# 엮어줌. 
cnn_model.compile(optimizer='adam', #손실 함수로는 희소 카테고리 크로스 엔트로피를 사용하며,
                  # 정확도를 평가 지표로 사용
                  loss='sparse_categorical_crossentropy', 
                  metrics=['acc'])

cnn_model.summary()
'''
Model: "sequential_1"
┌─────────────────────────────────┬────────────────────────┬───────────────┐
│ Layer (type)                    │ Output Shape           │       Param # │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ conv2d (Conv2D)                 │ (None, 26, 26, 16)     │           160 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ max_pooling2d (MaxPooling2D)    │ (None, 13, 13, 16)     │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ flatten_1 (Flatten)             │ (None, 2704)           │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_2 (Dense)                 │ (None, 64)             │       173,120 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_3 (Dense)                 │ (None, 10)             │           650 │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 173,930 (679.41 KB)
 Trainable params: 173,930 (679.41 KB)
 Non-trainable params: 0 (0.00 B)'''

#%%

cnn_history = cnn_model.fit(X_tr, y_tr, batch_size=64, epochs=20,
                        validation_data=(X_val, y_val),
                        verbose=2) 

# Epoch 20/20
# 750/750 - 5s - 6ms/step - acc: 0.9759 - loss: 0.0747 - val_acc: 0.9016 - val_loss: 0.3902
#%%

plot_loss_curve(history=cnn_history, total_epoch=20, start=1)    
# 결과 : 
#MLP 모델보다 CNN모델의 정확도가 개선
#훈련 오차는 계속 감소하지만 검증 오차는 0.3수준에서 횡보하다가 상승 추세 