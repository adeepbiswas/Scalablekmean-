import numpy as np
from kMeans import kMeansParallel
from kmeanspp import createCent
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
import time
start_time = time.time()
## Simulate data
k = 20
n = 10000
d = 15

def clust():
	centroids1 =output_kpp["Centroids"]
	labels1 = output_kpp["Labels"]
	for i,color in enumerate(colors,start =1):
		plt.scatter(data[labels1==i, :][:,0], data[labels1==i, :][:,1], color=color)
	for j in range(k):
		plt.scatter(centroids1[j,0],centroids1[j,1],color = 'w',marker='x')
	plt.show()

10## simulate k centers from 15-dimensional spherical Gaussian distribution
mean = np.hstack(np.zeros((d,1)))
cov = np.diag(np.array([1,10,100]*5))
centers = np.random.multivariate_normal(mean, cov, k)
## Simulate n data
for i in range(k):
	mean = centers[i]
	if i == 0:
		data = np.random.multivariate_normal(mean, np.diag(np.ones(d)), int(n/k+n%k))
		trueLabels = np.repeat(i,int(n/k+n%k))
	else:
		data = np.append(data, np.random.multivariate_normal(mean, np.diag(np.ones(d)),int(n/k)), axis = 0)
		trueLabels = np.append(trueLabels,np.repeat(i,int(n/k)))
centroids_initial = createCent(data, 20)

output_kpp = kMeansParallel(data, k, centroids_initial)
print("--- %s seconds ---" % (output_kpp - start_time))
cmap = plt.get_cmap('gnuplot')
colors = [cmap(i) for i in np.linspace(0, 1, k)]

