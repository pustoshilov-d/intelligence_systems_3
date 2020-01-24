from keras.layers import Input, Dense
from keras.models import Model
from sklearn.datasets import load_iris
import pandas as pd
import keras as K
from keras import Sequential
from keras import layers as la
from keras.utils import plot_model
from sklearn.datasets import fetch_20newsgroups
from keras.callbacks import EarlyStopping
from keras.callbacks import TensorBoard
import matplotlib.pyplot as plt
import random
from sklearn.utils import shuffle
import os
import h5py
from sklearn.model_selection import train_test_split
from datetime import datetime

os.environ["PATH"] += os.pathsep + 'D:\Programing\\bin\\'



iris = load_iris()


#X_train, X_test, y_train, y_test = train_test_split(iris["data"], iris["target"], test_size=0.33, shuffle=True)
#y_train = K.utils.to_categorical(y_train, 3)
#y_test = K.utils.to_categorical(y_test, 3)

#shuffle data
iris_set = pd.DataFrame(iris["data"]).join(pd.DataFrame(iris['target']), lsuffix='_left', rsuffix='_right')
iris_set = pd.DataFrame.reset_index(shuffle(iris_set))

print(iris_set)

X_train = iris_set.iloc[:,0:4]
y_train = iris_set.iloc[:,4]

y_train = K.utils.to_categorical(y_train)
print((X_train))
print(len(X_train))
print((y_train))
print(len(y_train))


inputs = Input(shape=(4,))
print(inputs)
output_1 = Dense(50, activation= 'relu')(inputs)
output_2 = Dense(50, activation= 'relu')(output_1)
predictions = Dense(3,activation= 'softmax')(output_2)

model = Model(inputs = inputs, outputs = predictions)

plot_model(model, to_file='model.png', show_shapes=True)

model.compile(optimizer='rmsprop',
              loss = 'categorical_crossentropy',
              metrics = ['accuracy'])

early_stopping=EarlyStopping(monitor='val_loss')

logdir = "logs\\" + datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = TensorBoard(log_dir=logdir, histogram_freq=1)

#tensorboard --logdir D:\Programing\Projects\Lisa\4.Keras\logs
#http://localhost:6006/

#history = model.fit(X_train, y_train, epochs=15, batch_size=20, callbacks=[early_stopping, tensorboard], validation_split=0.3, shuffle=True)
history = model.fit(X_train, y_train, epochs=30, batch_size=5, callbacks=[tensorboard_callback], validation_split=0.2)

#score = model.evaluate(X_test, y_test, batch_size=5)
#print(score)

print(history.history)


plt.plot(history.history['accuracy'], label = 'Аккуратность на обуч')
plt.plot(history.history['val_accuracy'], label = 'Аккуратность на трень')
plt.xlabel('Эпоха обучения')
plt.ylabel('Аккуратность')
plt.legend()
plt.show()

plt.plot(history.history['loss'], label = 'Ошибка на обуч')
plt.plot(history.history['val_loss'], label = 'Ошибка на трень')
plt.xlabel('Эпоха обучения')
plt.ylabel('Ошибка')
plt.legend()
plt.show()
