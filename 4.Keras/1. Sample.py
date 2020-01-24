import keras
from keras import Sequential
from keras import layers as la
from keras.utils import plot_model
from sklearn.datasets import fetch_20newsgroups
from keras.callbacks import EarlyStopping
from keras.callbacks import TensorBoard

import os

os.environ["PATH"] += os.pathsep + 'D:\Programing\\bin\\'

#датасет новостной рассылки

newsgroups_train = fetch_20newsgroups(subset='train')
newsgroups_test = fetch_20newsgroups(subset='test')

max_words = 1000
num_classes = 20
batch_size = 500
epochs= 10


tokenizer = keras.preprocessing.text.Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(newsgroups_train["data"])  # теперь токенизатор знает словарь для этого корпуса текстов

x_train = tokenizer.texts_to_matrix(newsgroups_train["data"], mode='binary')
x_test = tokenizer.texts_to_matrix(newsgroups_test["data"], mode='binary')


y_train = keras.utils.to_categorical(newsgroups_train["target"], num_classes)
y_test = keras.utils.to_categorical(newsgroups_test["target"], num_classes)


model = Sequential([
          la.Dense(512, input_shape=(max_words,)),
          la.Activation('relu'),
          la.Dropout(0.5),
          la.Dense(num_classes),
          la.Activation('softmax')
        ])


plot_model(model, to_file='model.png', show_shapes=True)


model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

early_stopping=EarlyStopping(monitor='val_loss')
tensorboard=TensorBoard(log_dir='.\\logs', write_graph=True)

history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_split=0.1,
                    callbacks=[early_stopping, tensorboard])

score = model.evaluate(x_test, y_test, batch_size=batch_size)

