import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_predict
from sklearn.neural_network import MLPClassifier as MLP
from sklearn.metrics import accuracy_score, recall_score, precision_score
from sklearn.model_selection import train_test_split
import os, cv2, pickle, random
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

df = pd.DataFrame(np.load('Xy.npy'))
X = df.drop(df.columns[-1], axis=1)
y = df[df.columns[-1]]

mlp = MLP()
#mlp.fit(X,y)
#pickle.dump(mlp, open('mlp.dat','wb'))
mlp = pickle.load(open('mlp.dat', 'rb'))

#grab random image of round or facet
facet_files = os.listdir('facets/')
round_files = os.listdir('rounds/')
files = facet_files + round_files
random.shuffle(files)
for f in files:
    if '.tiff' not in f:
        continue
    image_num = int(f.split('_00')[1].rstrip('.tiff'))
    if image_num > 500:
        if 'facet' in f:
            f = 'facets/' + f
        else:
            f = 'rounds/' + f
        image = cv2.imread(f)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        if gray.shape[0] != 768:
            gray = gray.T

        pca = PCA(50)
        transform = pca.fit_transform(gray)
        xt = transform.flatten()
        yt = mlp.predict([xt])
        yt = 'facet' if yt[0] == 0 else 'round'
        print(f, yt)

        plt.imshow(image)
        plt.title(yt)
        plt.gca().get_xaxis().set_visible(False)
        plt.gca().get_yaxis().set_visible(False)
        plt.show()









