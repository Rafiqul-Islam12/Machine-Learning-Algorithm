# K-Means Clustering

***K-Means is an `unsupervised` machine learning algorithm used to partition a dataset into `K distinct`, non-overlapping clusters.***
- ***Each data point belongs to `exactly one cluster`***
- ***Each cluster is represented by its `centroid` (mean point)***

<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Cluster%20Analysis/image/img01.png" width=600>
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Cluster%20Analysis/image/img02.png" width=550>

---
- ***`K` → Number of clusters (chosen in advance)***
- ***`Means` → Each cluster is represented by the mean of its data points***
---

### How K-Means Clustering Works?
***1. `Initialization:` Choose the number of clusters k***   
*The first step in k-means is to pick the number of clusters, k.*

***2. Assignment: Select k random points from the data as centroids***   
*For each data point in the dataset, calculate the distance between that point and each of the K centroids. Assign the data point to the cluster whose centroid is closest to it. This step effectively forms K clusters.*    
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Cluster%20Analysis/image/img03.png" width=580>    

***3. Update centroids: Assign all the points to the closest cluster centroid***    
*Once all data points have been assigned to clusters, recalculate the centroids of the clusters by taking the mean of all data points assigned to each cluster.*

***4. Repeat: Recompute the centroids of newly formed clusters***    
*Repeat steps 2 and 3 until convergence. Convergence occurs when the centroids no longer change significantly or when a specified number of iterations is reached.*   

***5. Final Result***
*Once convergence is achieved, the algorithm outputs the final cluster centroids and the assignment of each data point to a cluster.*    

---
### ***Stopping Criteria for K-Means Clustering***
- ***Centroids of newly formed clusters do not change***
- ***Points remain in the same cluster***
- ***Maximum number of iterations is reached***
---
### *Visual Representation*
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Cluster%20Analysis/image/img04.png" width=700>   

---
### *Mathematical Intuition*
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Cluster%20Analysis/image/img05.png" width=620>   

---
# *Elbow Method*
***The Elbow Method is a heuristic technique used to choose the `optimal number of clusters (K)` in K-Means clustering.***
- ***It is based on `inertia` (`WCSS` – Within-Cluster Sum of Squares).***      
- ***Inertia measures how tightly the data points are clustered around their centroids.***    

***Lower inertia ⇒ clusters are more compact***     
***Higher inertia ⇒ clusters are more spread out***     

***Inertia computes how far the data points in a cluster are from the centroid of that cluster.***    
***More precisely:***   
- ***For each cluster, inertia calculates the distance of every point from the cluster centroid***    
- ***These distances are then summed up***   
- ***Finally, the sum is taken over all clusters***    
  
***Mathematically, inertia is the sum of intracluster distances.***    
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Cluster%20Analysis/image/img06.jpg" width=620>   
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Cluster%20Analysis/image/img07.jpg" width=620>   

---
### *Author*
***Md. Rafiqul Islam***   
***CSE, CoU***
