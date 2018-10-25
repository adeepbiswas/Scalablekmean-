import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import kMeans
import kmeanspp
from sklearn.datasets.samples_generator import make_blobs
import time
start_time = time.time()
'''
x = np.random.randn(10)
y = np.random.randn(10)
Cluster = np.array([0, 1, 1, 1, 3, 2, 2, 3, 0, 2])    # Labels of cluster 0 to 3
centers = np.random.randn(3, 2) 
'''
'''
dataMat = np.mat(kMeans.loadDataSet('testSet.txt'))
x = dataMat[:,0]
y = dataMat[:,1]
'''

def importData():
    for i in range(0,1000000):
        for j in range(0,600):
            i = i + j
dataSet, _ = make_blobs(n_samples=100,centers=3,n_features=2,random_state=0)
dataSet = np.mat(dataSet)
importData()
centers,clusterAssgn = kMeans.kMeans(dataSet=dataSet,k=4,createCent = kmeanspp.createCent)
#centers,clusterAssgn = kMeans.kMeans(dataSet=dataMat,k=4)
x = dataSet[:,0]
y = dataSet[:,1]
x = np.array(x)
y = np.array(y)
Cluster = np.array(clusterAssgn[:,0])
print(centers)
print('cluster:',Cluster)
fig = plt.figure()
ax = fig.add_subplot(111)
scatter = ax.scatter(x,y,c=Cluster,s=50)
#scatter = plt.scatter(x,y)
#s parameter shows how big will be the plus symbol

centers = np.mat(centers) 
for ele in centers:
    i = ele[0,0]
    j = ele[0,1]
    ax.scatter(i,j,s=50,c='red',marker='+')
ax.set_xlabel('x')
ax.set_ylabel('y')
print("--- %s seconds ---" % (time.time() - start_time))
plt.show()


