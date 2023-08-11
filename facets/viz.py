import matplotlib.pyplot as plt
import numpy as np
from skimage import color
from skimage import io

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Convolution2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils

def CNN_model():
    model = Sequential()
    model.add(Convolution2D(32, (5,5), border_mode='valid', input_shape=(4048,3036,3),activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(1, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

X = []
import os
facets = os.listdir('.')
for fName in facets[0:10]: 
    print(fName)
    if 'facet' not in fName: continue
    x = io.imread(fName)
#    plt.imshow(img, cmap='gray')
            
    r,c,z = np.shape(x)
    if r == 3036:
        x = x.T
    
    X.append(x)

model = CNN_model()
model.fit(X, np.ones((1, len(X))))