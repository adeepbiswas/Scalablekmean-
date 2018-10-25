import numpy as np
from kimp import distance_cy
from kimp import cost_cy
from kimp import distribution_cy
from kimp import sample_new_cy
from kimp import get_weight_cy
from kimp import weightedKMeans
def ScalableKMeansPlusPlus_cy(data, k, l, weighted=False, iter=5):
	centroids = data[np.random.choice(range(data.shape[0]),1), :]
	for i in range(iter):
		#Get the distance between data and centroids
		dist = distance_cy(data, centroids)
		#Calculate the cost of data with respect to the centroids
		norm_const = cost_cy(dist)
		#Calculate the distribution for sampling l new centers
		p = distribution_cy(dist,norm_const)
		#Sample the l new centers and append them to the original ones
		centroids = np.r_[centroids, sample_new_cy(data,p,l)]
	## reduce k*l to k using KMeans++
	dist = distance_cy(data, centroids)
	weights = get_weight_cy(dist,centroids)
	if weighted:
		initial = centroids[np.random.choice(range(len(weights)),k,replace=False),:]
		centers= weightedKMeans(centroids, k, weights, initial)
	else:
		centers= centroids[np.random.choice(len(weights), k, replace= False, p = weights),:]
	return centers
