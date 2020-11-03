import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow.keras as keras

from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Input, Activation, add, Add, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.utils import to_categorical

from IPython.display import SVG
from tensorflow.python.keras.utils.vis_utils import model_to_dot

random_state = 42


# モデル作成
model = Sequential()

model.add(Conv2D(6, kernel_size=(5, 5), activation='relu',
                kernel_initializer='he_normal', input_shape=(28, 28, 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(16, kernel_size=(5, 5), activation='relu',
                kernel_initializer='he_normal'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(120, activation='relu',kernel_initializer='he_normal'))
model.add(Dense(84, activation='relu',kernel_initializer='he_normal'))
model.add(Dense(10, activation='softmax'))

model.compile(
    loss=keras.losses.categorical_crossentropy,
    optimizer='adam',
    metrics=['accuracy']
)


# モデルの表示
SVG(model_to_dot(model, show_shapes=True).create(prog='dot', format='svg'))

# 学習
early_stopping = EarlyStopping(patience=1, verbose=2)
model.fit(x=x_train, y=y_train, batch_size=128, epochs=100, verbose=2,
         validation_data=(x_valid, y_valid), callbacks=[early_stopping])

# スコアの表示
score = model.evaluate(x_valid, y_valid, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# 予測
classes = model.predict(x_test, batch_size=128)
# sub['Label'] = classes.argmax(axis=1)