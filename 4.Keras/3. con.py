import keras
from keras import backend as K
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization
from keras.callbacks import TensorBoard, EarlyStopping

import matplotlib.pyplot as plt
from keras.utils import plot_model
from datetime import datetime
import os

from keras.datasets import fashion_mnist, cifar10


batch_size = 150
num_classes = 10
epochs = 4
chanDim = -1
num_samples = 600


os.environ["PATH"] += os.pathsep + 'D:\Programing\\bin\\'
logdir = "logs\\3\\" + datetime.now().strftime("%Y%m%d-%H%M%S")


save_dir = os.path.join(os.getcwd(), 'saved_models')
model_name = 'mnist_CNN'

(x_train, y_train) , (x_test, y_test) = fashion_mnist.load_data()
x_train = x_train[:num_samples]
y_train = y_train[:num_samples]
x_test = x_test[:num_samples]
y_test = y_test[:num_samples]

print(x_train.shape)
print(x_train[0], y_train[0])
print(x_test[0], y_test[0])

if K.image_data_format() == "channels_first":
    x_train = x_train.reshape((x_train.shape[0], 1, 28, 28))
    x_test = x_test.reshape((x_test.shape[0], 1, 28, 28))
else:
    x_train = x_train.reshape((x_train.shape[0], 28, 28, 1))
    x_test = x_test.reshape((x_test.shape[0], 28, 28, 1))

# if K.image_data_format() == "channels_first":
# 			inputShape = (depth, height, width)
# 			chanDim = 1

y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)

model = Sequential([
    Conv2D(32,(3,3), padding='same',input_shape=x_train.shape[1:]),
    Activation('relu'),
    BatchNormalization(axis=chanDim),

    Conv2D(32,(3,3), padding='same'),
    Activation('relu'),
    BatchNormalization(axis=chanDim),
    MaxPooling2D(pool_size=(2,2)),
    Dropout(0.25),

    Flatten(),

    Dense(128),
    BatchNormalization(),
    Dropout(0.25),

    Dense(num_classes),
    Activation('softmax')
])


plot_model(model, to_file='model.png', show_shapes=True)

model.compile(loss='categorical_crossentropy',
              optimizer=keras.optimizers.Adam(),
              metrics=['accuracy'])

tensorboard_callback = TensorBoard(log_dir=logdir, histogram_freq=1)
early_stopping=EarlyStopping(monitor='val_loss')

history = model.fit(x_train,y_train,epochs=epochs,batch_size=batch_size, verbose=1,callbacks=[tensorboard_callback,early_stopping], validation_split=0.2, use_multiprocessing = True)
#tensorboard --logdir D:\Programing\Projects\Lisa\4.Keras\logs\3

score = model.evaluate(x_test,y_test)
print(score)

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