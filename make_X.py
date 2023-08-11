import numpy as np

facets = np.load('facets/facets.npy')
rounds = np.load('rounds/rounds.npy')

facets = np.hstack((facets, np.ones((facets.shape[0],1))))
facets = facets[0:500,:]

rounds = np.hstack((rounds, np.zeros((rounds.shape[0],1))))
rounds = rounds[0:500,:]
print(facets.shape)
print(rounds.shape)

X = np.concatenate((facets, rounds), axis=0)
print(X.shape)

np.save('Xy.npy', X)
