#!/usr/bin/env python
# coding: utf-8

#%%

# DNN(Deep Neural Network)

#%%
# # 1. 환경 설정

# In[ ]:


# 라이브러리 설정
import pandas as pd
import numpy as np
import tensorflow as tf
import random

# 랜덤 시드 고정
SEED=12
random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)  


# # 2. 데이터셋 준비

# In[ ]:


# MLP( Multi-Layer )

# 데이콘 사이트에서 다운로드한 CSV파일을 읽어오기
#drive_path = "/gdrive/My Drive/"
train = pd.read_csv("dataset/train.csv")
test = pd.read_csv("dataset/test.csv")
submission = pd.read_csv("dataset/sample_submission.csv")

print(train.shape, test.shape, submission.shape)   
# (60000, 786) (10000, 785) (10000, 2)


# In[ ]:


# train 데이터 보기
train.head()


# In[ ]:
# 3차원 변환
# train 데이터를 28*28 이미지로 변환
# 컬럼 : 'pixel1':pixel784
train_images = train.loc[:, 'pixel1':].values.reshape(-1, 28, 28)
train_images.shape


# In[ ]:


# 첫번째 이미지 출력
# 원래 파이썬에서 세미컬럼 자동입력돼서 출력되는거임. 
import matplotlib.pyplot as plt
plt.imshow(train_images[0]);
plt.imshow(train_images[0], cmap='gray'); # 훈련을 위해 변환한 이미지
plt.imshow(train_images[0], cmap='gray_r'); # reverse

#%%
#shape 속성은 배열의 차원을 나타내는 튜플을 반환
# 튜플에서 가장 중요한 특징은 "값이 변하지 않는다" 라는 특징
# 리스트에서는 값을 변경할수 있지만, 튜플은 내부의 값을 변경하거나 삭제 할 수 없습니다.

imglen = train_images.shape[0]
print("이미지 갯수:", imglen) # 이미지 갯수: 60000
'''
# shape[x] test
import numpy as np

R = np.floor(10*np.random.random((2, 3)))      
# 10 이하의 숫자로 난수 생성해서 2*3 행렬 만들음
print(R)

print(R.shape[0]) # 2  행의 개수 
print(R.shape[1]) # 3  열의 개수

[[1. 7. 2.]
 [5. 0. 9.]]
'''

# In[ ]:


# 목표 레이블 
y_train = train.loc[:, 'label']
y_train.unique()

#%%

fig, axs = plt.subplot(8, 8, figsize=(12,12))
for i in range(8):
    for j in range(8): 
        axs[i,j].image(train_images[i+8+j])
        axs[i,j].axis('off')

plt.show()

# In[ ]:


# 숫자 레이블을 실제 레이블과 연결하여 확인
target_values = {0 : 'T-shirt/top', 
                 1 : 'Trouser', # 바지 
                 2: 'Pullover', # 스웨터
                 3: 'Dress', 
                 4: 'Coat', 
                 5: 'Sandal', 
                 6: 'Shirt', 
                 7: 'Sneaker', 
                 8: 'Bag', 
                 9: 'Ankle boot'} # 부츠 
print(y_train[0]) # 2 
print(target_values[y_train[0]]) # Pullover


# In[ ]:


# test 데이터를 28*28 이미지로 변환
test_images = test.loc[:, 'pixel1':].values.reshape(-1, 28, 28)
test_images.shape


# In[ ]:


# 500번째 test 이미지를 출력
plt.imshow(test_images[499]);


# # 2. 데이터 전처리 (Pre-processing)

# In[ ]:

# 정규화
#여기에서는 이미지 데이터를 정규화(normalization)하고 있습니다. 
#정규화는 데이터의 범위를 변경하여 학습을 더 잘 수행하도록 돕는 기술
# train_images와 test_images의 각 픽셀 값은 0에서 255 사이의 값을 갖습니다.
# 이 값을 255로 나누면 모든 픽셀 값이 0에서 1 사이의 값으로 스케일됩니다.
# 이미지 픽셀의 값(컬러) : 0~255
# 피처 스케일 맞추기 
# 픽셀이 0.0~ 1.0 범위로 축소

X_train = train_images / 255.
X_test = test_images / 255.
print("최소값:", X_train[0].min()) 
print("최대값:", X_train[0].max())
'''
최소값: 0.0
최대값: 1.0
'''

# In[ ]:

# CNN(합성곱 신경망) : 3채널(red, green, blue)
# 채널 차원 추가 : 컬러 채널 
# 차원 또는 축(axis)를 추가시키려면 np.expand_dim 함수를 사용한다
# axis=0 행축 추가 / axis=1 열축 추가 / axis=-1 이면 마지막 축 추가를 의미
print("변환 전:", X_train.shape, X_test.shape)
X_train = np.expand_dims(X_train, axis=-1)
X_test = np.expand_dims(X_test, axis=-1)
print("변환 후:", X_train.shape, X_test.shape)
'''
변환 전: (60000, 28, 28) (10000, 28, 28)
변환 후: (60000, 28, 28, 1) (10000, 28, 28, 1)
'''

# In[ ]:


# Train - Validation 데이터 구분
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val =  train_test_split(X_train, y_train, test_size=0.2, 
                                             stratify=y_train, 
                                             shuffle=True, random_state=SEED)
print("학습 데이터셋 크기: ", X_tr.shape, y_tr.shape)
print("검증 데이터셋 크기: ", X_val.shape, y_val.shape)
'''
학습 데이터셋 크기:  (48000, 28, 28, 1) (48000,)
검증 데이터셋 크기:  (12000, 28, 28, 1) (12000,)'''

# # 3. 모델 구축

# ### MLP 모델
# MLP(Multi-Layer Perceptron)

# In[ ]:
# Flatten (기존의 2차원 데이터를 1차원으로 축소)
# shape=[28, 28] 2d 배열 -> 1차원 배열로 평평하게 펼쳐줌, . 이는 이미지 데이터를 MLP의 첫 번째 Dense레이어에 입력으로 사용하기 위함


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
mlp_model = Sequential()
mlp_model.add(Flatten(input_shape=[28, 28]))
mlp_model.add(Dense(units=64, activation='relu')) # 은닉레이어 : 64뉴런 + 활성화 함수로는 ReLU(Rectified Linear Unit)를 사용
# ReLU는 음수를 0으로 만들고 양수는 그대로 유지하여 비선형성을 추가
mlp_model.add(Dense(units=10, activation='softmax'))
# 이어는 10개의 뉴런을 가지며, 활성화 함수로는 소프트맥스(softmax)를 사용합니다. 이 레이어는 각 클래스에 속할 확률을 출력하기 위해 사용
#loss: 'sparse_categorical_crossentropy' : onehot_encoding is no longer needed  다중 클래스 분류 문제에 적합(타겟 데이터가 정수 형태인 경우에 사용)
mlp_model.compile(optimizer='adam', 
                  loss='sparse_categorical_crossentropy', 
                  metrics=['acc']) # 모델은 정확도(acc)를 평가 지표로 사용

mlp_model.summary()
'''
Model: "sequential"
┌─────────────────────────────────┬────────────────────────┬───────────────┐
│ Layer (type)                    │ Output Shape           │       Param # │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ flatten (Flatten)               │ (None, 784)            │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense (Dense)                   │ (None, 64)             │        50,240 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_1 (Dense)                 │ (None, 10)             │           650 │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 50,890 (198.79 KB)
 Trainable params: 50,890 (198.79 KB)
 Non-trainable params: 0 (0.00 B)'''

# In[ ]:

# batch_size=64: 한 번의 배치에서 사용되는 샘플의 개수/ 여기서는 64개의 샘플을 한 번에 사용하여 경사 하강법을 수행합니다.
# epochs=20: 전체 데이터셋을 사용하여 학습하는 횟수입니다. 여기서는 20번의 에포크 동안 모델을 훈련합니다.
mlp_history = mlp_model.fit(X_tr, y_tr, batch_size=64, epochs=20,
                        validation_data=(X_val, y_val), # 모델이 훈련 중에 일반화 성능을 평가하는 데 사용
                        verbose=2)
'''
Epoch 1/20
750/750 - 2s - 3ms/step - acc: 0.8033 - loss: 0.5704 - val_acc: 0.8404 - val_loss: 0.4563
...
Epoch 20/20
750/750 - 1s - 2ms/step - acc: 0.9185 - loss: 0.2228 - val_acc: 0.8817 - val_loss: 0.3467
'''


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
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

plot_loss_curve(history=mlp_history, total_epoch=20, start=1)                   

# 결과 : 과대적합
# 훈련 오차는 계속 감소하지만 검증 오차는 0.34 수준에서 횡보하는 추세
# 3번쨰 에포크 부터 훈련 오차가 검증 오차보다 낮아지기 시작하여 과대적합 발생
'''훈련 손실은 계속해서 감소하거나 안정화되는 반면 검증 손실은 어느 시점 이후로 다시 증가하는 경향이 있습니다. 
마찬가지로, 훈련 정확도는 계속해서 증가하지만 검증 정확도는 어느 시점 이후로 감소하거나 안정화됩니다.'''
#%%
mlp_model.evaluate(X_val, y_val) # [0.3466900587081909, 0.8816666603088379]
# loss: 0.3507 
# acc: 0.8811 
#%%
# ### CNN 활용


from tensorflow.keras.layers import Conv2D, MaxPooling2D
cnn_model = Sequential()
cnn_model.add(Conv2D(filters=16, kernel_size=(3, 3), # 필터(뉴런)
                    activation='relu', input_shape=[28, 28, 1])) # 커널크기
cnn_model.add(MaxPooling2D(pool_size=(2, 2)))
cnn_model.add(Flatten())
cnn_model.add(Dense(units=64, activation='relu'))
cnn_model.add(Dense(units=10, activation='softmax'))

cnn_model.compile(optimizer='adam', 
                  loss='sparse_categorical_crossentropy', 
                  metrics=['acc'])

cnn_model.summary()


# In[ ]:


cnn_history = cnn_model.fit(X_tr, y_tr, batch_size=64, epochs=20,
                        validation_data=(X_val, y_val),
                        verbose=2) 


# In[ ]:


plot_loss_curve(history=cnn_history, total_epoch=20, start=1)    


# In[ ]:

# 드롭아웃:
    # - 모델을 가볍게 해서 과대적합 해소를 위해서
    # - 지정된 비율 만큼 뉴런 가중치를 0으로 만듦.
from tensorflow.keras.layers import Dropout
def build_cnn():
    model = Sequential()
    model.add(Conv2D(filters=16, kernel_size=(3, 3),  # 필터(뉴런)
                     activation='relu', input_shape=[28, 28, 1])) # 커널크기(3*3)
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(units=64, activation='relu'))
    model.add(Dropout(rate=0.5))
    model.add(Dense(units=10, activation='softmax'))

    model.compile(optimizer='adam', 
                loss='sparse_categorical_crossentropy', # 원핫인코딩을 하지 않아도 됨. 
                #sparse data = 희귀데이터 / dense data = 밀집데이터 
                metrics=['acc'])

    return model

cnn_model = build_cnn()
cnn_model.summary()
'''
Model: "sequential_3"
┌─────────────────────────────────┬────────────────────────┬───────────────┐
│ Layer (type)                    │ Output Shape           │       Param # │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ conv2d_1 (Conv2D)               │ (None, 26, 26, 16)     │           160 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ max_pooling2d_1 (MaxPooling2D)  │ (None, 13, 13, 16)     │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ flatten_2 (Flatten)             │ (None, 2704)           │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_4 (Dense)                 │ (None, 64)             │       173,120 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dropout (Dropout)               │ (None, 64)             │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_5 (Dense)                 │ (None, 10)             │           650 │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 173,930 (679.41 KB)
 Trainable params: 173,930 (679.41 KB)
 Non-trainable params: 0 (0.00 B)'''

# In[ ]:


from tensorflow.keras.callbacks import EarlyStopping

early_stopping = EarlyStopping(monitor='val_loss',  patience=10)

cnn_history = cnn_model.fit(X_tr, y_tr, batch_size=64, epochs=20,
                        validation_data=(X_val, y_val),
                        callbacks=[early_stopping],
                        verbose=0) 


# In[ ]:


# 20 epoch 까지 손실함수와 정확도를 그래프로 나타내기
start=1
end = 20

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].plot(range(start, end+1), cnn_history.history['loss'][start-1:end], 
             label='Train')
axes[0].plot(range(start, end+1), cnn_history.history['val_loss'][start-1:end],  
             label='Validation')
axes[0].set_title('Loss')
axes[0].legend()

axes[1].plot(range(start, end+1), cnn_history.history['acc'][start-1:end], 
             label='Train')
axes[1].plot(range(start, end+1), cnn_history.history['val_acc'][start-1:end], 
             label='Validation')
axes[1].set_title('Accuracy')
axes[1].legend()
plt.show()


# In[ ]:


cnn_model.evaluate(X_val, y_val)
# [0.3075224459171295, 0.9110000133514404]

# In[ ]:


y_pred_proba = cnn_model.predict(X_test)
y_pred_classes = np.argmax(y_pred_proba, axis=-1)
y_pred_classes[:10]


# In[ ]:


submission['label'] = y_pred_classes
submission_filepath = 'mnist_cnn_submission1.csv'   
submission.to_csv(submission_filepath, index=False)


# In[ ]:


# 사용자 정의 콜백 함수
from tensorflow.keras.callbacks import Callback
# Callback 클래스를 상속 
# on_epoch_end 매서드 재정의 
#    - 매 에포크가 끝날 떄마다 실행
#    - 종료 조건을 체크 
#  self.model.stop_training의 속성값 : 91%보다 크면 종료
class my_callback(Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('val_acc') > 0.91): 
      self.model.stop_training = True
      print("\n")
      print("목표 정확도 달성: 검증 정확도 %.4f" % logs.get('val_acc'))

my_callback = my_callback()

# Best Model 저장
from tensorflow.keras.callbacks import ModelCheckpoint
# 훈련된 모델을 저장
best_model_path = "best_cnn_model.h5"
save_best_model = ModelCheckpoint(best_model_path, monitor='val_loss', 
                                  save_best_only=True, save_weights_only=False) 
#가중치만 저장가능 true 주면

# CNN 모델 학습
cnn_model = build_cnn()
cnn_history = cnn_model.fit(X_tr, y_tr, batch_size=64, epochs=100,
                        validation_data=(X_val, y_val),
                        callbacks=[my_callback, save_best_model],
                        verbose=2) 


# In[ ]:


from tensorflow.keras.models import load_model
# ModelCheckPoint에 저장해둔 모델을 로딩 
best_model = load_model("./dataset/best_cnn_model.h5")
best_model.summary()
'''
Model: "sequential_4"
┌─────────────────────────────────┬────────────────────────┬───────────────┐
│ Layer (type)                    │ Output Shape           │       Param # │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ conv2d_3 (Conv2D)               │ (None, 26, 26, 16)     │           160 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ max_pooling2d_3 (MaxPooling2D)  │ (None, 13, 13, 16)     │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ flatten_4 (Flatten)             │ (None, 2704)           │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_8 (Dense)                 │ (None, 64)             │       173,120 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dropout_1 (Dropout)             │ (None, 64)             │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_9 (Dense)                 │ (None, 10)             │           650 │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 173,932 (679.43 KB)
 Trainable params: 173,930 (679.41 KB)
 Non-trainable params: 0 (0.00 B)
 Optimizer params: 2 (12.00 B)'''

# In[ ]:


y_pred_proba = best_model.predict(X_test)
y_pred_classes = np.argmax(y_pred_proba, axis=-1)
submission['label'] = y_pred_classes
submission_filepath = 'mnist_cnn_submission2.csv'   
submission.to_csv(submission_filepath, index=False)

