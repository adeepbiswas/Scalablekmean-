# scalable_kmeans
An attempt to implement scalable kmeans++ algorithm
Now we're going to parallelize scalable kmeans pp on the Hadoop platform..

In this work we acquire a parallel variant of the k-means++ introduction calculation and exactly exhibit its viable .The primary thought is that as opposed to testing a solitary point in each go of the k-means++ calculation, we test O(k) focuses in each round and rehash the procedure for around O(log n) rounds. Toward the finish of the calculation we are left with O(k log n) focuses that shape an answer that is inside a steady factor far from the ideal. We at that point recluster these O(k log n) focuses into k introductory places for the Lloyd's cycle. This introduction calculation, which we call k-means||, is very basic and fits simple parallel usage.
