#!/usr/bin/env python
# coding: utf-8

# # 1. 환경 설정
# 전이 학습(Transfer Learning): 사전 학습 모델 활용
# 사전 학습(pre-trained) 모델의 검증된 아키텍처와 가중치를 그대로 가져오고,
# 일부 새로운 층을 추가하거나 가중치를 조정하는 방식으로 학습하는 것을 전이 학습이라고 한다.

# In[1]:
# 1. 환경 설정 

# 라이브러리 설정
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import random

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Reshape
from tensorflow.keras.layers import BatchNormalization

# 랜덤 시드 고정
SEED=12
random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)  


# # 2. 데이터셋 준비

# In[2]:


# CIFAR10 이미지 데이터셋
from tensorflow.keras import datasets
cifar10 = datasets.cifar10
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# 피처 스케일링
# 0~1 범위로 정규화
X_train = X_train / 255.
X_test = X_test / 255.

print(X_train.shape, y_train.shape, X_test.shape, y_test.shape) 
# (50000, 32, 32, 3) (50000, 1) (10000, 32, 32, 3) (10000, 1)
# 마지막 3은 (3채널) RGB / 흑백이미지일 경우 채널 1 
# 한장의 사진은 32*32 평면 3장(채널[컬러] 별) 이 합쳐진 것. 
print(X_train[0])
size = X_train[0].shape
print(size) # (32, 32, 3)
# In[ ]:


# Train 이미지 출력하기
# 20개 훈련 데이터 
plt.figure(figsize=(10, 8))
for i in range(20):
    plt.subplot(4, 5, i + 1), 
    plt.imshow(X_train[i])
    plt.axis('off')
plt.show()


# # 3. 모델 구축

# In[ ]:
# CNN 모델은 이미지를 식별하는데 있어서 필터를 지정해주고 가장 큰 값을 가지는 즉
# 큰 특징들을 뽑아 이미지를 구분지음. 

def build_cnn():
    model = Sequential()
    model.add(Conv2D(filters=32, kernel_size=(5, 5), strides=(2, 2),
                     activation='relu', input_shape=[32, 32, 3]))
    model.add(BatchNormalization()) # 내부에서 정규화
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(filters=64, kernel_size=(5, 5), strides=(2, 2),
                     activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(units=64, activation='relu'))
    model.add(Dropout(rate=0.5))
    model.add(Dense(units=32, activation='relu'))
    model.add(Dropout(rate=0.5))
    model.add(Dense(units=10, activation='softmax'))

    model.compile(optimizer='adam', 
                 loss='sparse_categorical_crossentropy', 
                 metrics=['accuracy'])

    return model

cnn_model = build_cnn()
cnn_model.summary()

'''
Model: "sequential_1"
┌─────────────────────────────────┬────────────────────────┬───────────────┐
│ Layer (type)                    │ Output Shape           │       Param # │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ conv2d_2 (Conv2D)               │ (None, 14, 14, 32)     │         2,432 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ batch_normalization_2           │ (None, 14, 14, 32)     │           128 │
│ (BatchNormalization)            │                        │               │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ max_pooling2d_2 (MaxPooling2D)  │ (None, 7, 7, 32)       │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ conv2d_3 (Conv2D)               │ (None, 2, 2, 64)       │        51,264 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ batch_normalization_3           │ (None, 2, 2, 64)       │           256 │
│ (BatchNormalization)            │                        │               │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ max_pooling2d_3 (MaxPooling2D)  │ (None, 1, 1, 64)       │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ flatten_1 (Flatten)             │ (None, 64)             │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_3 (Dense)                 │ (None, 64)             │         4,160 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dropout_2 (Dropout)             │ (None, 64)             │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_4 (Dense)                 │ (None, 32)             │         2,080 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dropout_3 (Dropout)             │ (None, 32)             │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_5 (Dense)                 │ (None, 10)             │           330 │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 60,650 (236.91 KB)
 Trainable params: 60,458 (236.16 KB)
 Non-trainable params: 192 (768.00 B)'''



# In[ ]:


# 모델 학습
cnn_history = cnn_model.fit(X_train, y_train, batch_size=256, epochs=20,
                        validation_split=0.1, verbose=0) 

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

# 그래프 그리기
plot_metrics(history=cnn_history, start=1, end=20)    


# # 4. 전이 학습

# In[ ]:


# Pre-trained 모델 가져오기 (VGG16)
# include_top : False 모델의 분류기 역할을 하는 부분 제외
# weights : 'imagenet', ImageNet 데이터로 학습한 가중치 
from tensorflow.keras.applications import ResNet50
cnn_base = ResNet50(include_top=False, weights='imagenet', 
                 input_shape=[32, 32, 3],classes=10)  


# In[ ]:
# 이진 분류에 쓰이는 활성화함수는 sigmoid function -> generalization(일반화) -> 다중분류에 쓰이는 Softmax function
# ReLu function -> input<=0 일 떄 항상 0을 출력하고 input>0 이면 input 과 동일한 output을 출력.

# Transfer 모델 생성
def build_transfer():
    transfer_model = Sequential()
    transfer_model.add(cnn_base) 
    transfer_model.add(Flatten()) 

    transfer_model.add(Dense(units=64, activation='relu'))
    transfer_model.add(Dropout(rate=0.5))
    transfer_model.add(Dense(units=32, activation='relu'))
    transfer_model.add(Dropout(rate=0.5))
    transfer_model.add(Dense(units=10, activation='softmax'))

    transfer_model.compile(optimizer='adam', 
                    loss='sparse_categorical_crossentropy', 
                    metrics=['accuracy'])


    return transfer_model

transfer_model = build_transfer()
transfer_model.summary()
'''
Model: "sequential_2"
┌─────────────────────────────────┬────────────────────────┬───────────────┐
│ Layer (type)                    │ Output Shape           │       Param # │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ resnet50 (Functional)           │ ?                      │    23,587,712 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ flatten_2 (Flatten)             │ ?                      │   0 (unbuilt) │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_6 (Dense)                 │ ?                      │   0 (unbuilt) │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dropout_4 (Dropout)             │ ?                      │   0 (unbuilt) │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_7 (Dense)                 │ ?                      │   0 (unbuilt) │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dropout_5 (Dropout)             │ ?                      │   0 (unbuilt) │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_8 (Dense)                 │ ?                      │   0 (unbuilt) │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 23,587,712 (89.98 MB)
 Trainable params: 23,534,592 (89.78 MB)
 Non-trainable params: 53,120 (207.50 KB)'''

# In[ ]:


tm_history = transfer_model.fit(X_train, y_train, batch_size=256, epochs=20,
                        validation_split=0.1, verbose=0) 

plot_metrics(history=tm_history, start=1, end=20)   


# In[ ]:




