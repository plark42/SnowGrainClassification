from sklearn.decomposition import PCA
import cv2
import numpy as np
import os

X = []
files = os.listdir()
for f in files:
    if '.tiff' in f:
        image = cv2.imread(f)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        if image.shape[0] != 768: 
            image = image.T
        pca = PCA(50)
        image_t = pca.fit_transform(image)
        image_t = image_t.flatten()
        X.append(image_t)
        print(len(X), 'of', len(files))

X = np.array(X)
np.save('facets.npy', X)

