# Fuzzy-Clustering
Algorithm of Fuzzy Clustering

## Key Concepts
### Membership Values (uiju_{ij}):
Represents the degree to which data point xix_i belongs to cluster jj.
uiju_{ij} ranges between 0 and 1.
For each data point ii, the sum of membership values over all clusters jj is 1: ∑j=1Cuij=1for all i\sum_{j=1}^{C} u_{ij} = 1 \quad \text{for all } i
### Fuzziness Coefficient (mm):
A parameter that controls the degree of fuzziness in the clustering process.
m>1m > 1 (often chosen around 2).
Higher values of mm result in fuzzier clusters, meaning the memberships will be more spread out.
### Cluster Centers (cjc_j):
The centroid or center of cluster jj computed as a weighted average of all data points, where weights are the membership values raised to the power mm.


## Objective Function
The algorithm minimizes the following objective function:

J=∑i=1N∑j=1Cuijm∥xi−cj∥2J = \sum_{i=1}^{N} \sum_{j=1}^{C} u_{ij}^m \| x_i — c_j \|²

where:

### NN is the number of data points.
### CC is the number of clusters.
### xix_i is the iith data point.
### cjc_j is the center of the jjth cluster.
### ∥xi−cj∥\| x_i — c_j \| denotes the Euclidean distance between xix_i and cjc_j.


## The FCM Algorithm: Step-by-Step
### Initialization:
Choose the number of clusters CC and the fuzziness coefficient mm.
Initialize the membership matrix U=[uij]U = [u_{ij}] randomly such that for every data point ii, ∑j=1Cuij=1\sum_{j=1}^{C} u_{ij} = 1.
### Update Cluster Centers:
Compute the center cjc_j of each cluster using: cj=∑i=1Nuijm xi∑i=1Nuijmc_j = \frac{\sum_{i=1}^{N} u_{ij}^m \, x_i}{\sum_{i=1}^{N} u_{ij}^m}
This formula computes a weighted average of the data points, where weights are the membership values raised to mm.
### Update Membership Values:
Update each membership value uiju_{ij} using: uij=1∑k=1C(∥xi−cj∥∥xi−ck∥)2m−1u_{ij} = \frac{1}{\sum_{k=1}^{C} \left(\frac{\| x_i — c_j \|}{\| x_i — c_k \|}\right)^{\frac{2}{m-1}}}
This formula assigns a higher membership value to clusters whose centers are closer to the data point.
### Convergence Check:
Repeat steps 2 and 3 until the changes in the membership matrix UU (or the cluster centers cjc_j) fall below a predefined threshold. This indicates that the algorithm has converged.
### Termination:
Once convergence is achieved, the final membership matrix and cluster centers represent the fuzzy clustering of the data.
