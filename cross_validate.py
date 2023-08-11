import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_predict
from sklearn.neural_network import MLPClassifier as MLP
from sklearn.metrics import accuracy_score, recall_score, precision_score
from sklearn.model_selection import train_test_split

df = pd.DataFrame(np.load('Xy.npy'))
X = df.drop(df.columns[-1], axis=1)
y = df[df.columns[-1]]

mlp = MLP()
yp = cross_val_predict(mlp, X, y, cv=5)
acc = accuracy_score(y,yp) * 100
pre = precision_score(y,yp) * 100
rec = recall_score(y,yp) * 100
print('acc = %.2f, prec = %.2f, rec = %.2f' % (acc, pre, rec))






