import matplotlib.pyplot as plt
import numpy as np

acc = []
pre = []
rec = []

f = open('results.txt', 'r')
for line in f:
    words = line.strip().split(',')
    acc.append(float(words[0].split(' = ')[1]))
    pre.append(float(words[1].split(' = ')[1]))
    rec.append(float(words[2].split(' = ')[1]))
f.close()

plt.boxplot([acc, pre, rec], positions=[0,0.25,0.5])
plt.ylabel('percentage (%)')
plt.xticks([0,0.25,0.5],['accuracy', 'precision', 'recall'])
plt.xlim([-0.15,0.65])
plt.yticks(list(range(92,101)))
plt.title('classification results (100 iterations)')
plt.show()

print(np.median(acc), np.median(pre), np.median(rec))
