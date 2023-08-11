from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import cv2
import numpy as np
import os

image = cv2.imread('facet_00006.tiff')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.figure()
plt.rcParams['axes.titlesize'] = 10
n = 1
for i in [5, 10, 25, 50]:
    pca = PCA(i)
    image_t = pca.fit_transform(image)
    image_pca = pca.inverse_transform(image_t)
    ax = plt.subplot(2,2,n)
    plt.imshow(image_pca, cmap="gray")
    plt.axis('off')
    ax.title.set_text('%d principal components' % i)
    n += 1

plt.tight_layout()
plt.show()

