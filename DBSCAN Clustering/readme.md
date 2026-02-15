# *DBSCAN Clustering - Density based clustering*  

***DBSCAN হলো একটা unsupervised density based clustering algorithm.***  
***যেটা ডাটার density দেখে cluster বানায়।***   
- ***যেখানে অনেক পয়েন্ট একসাথে কাছাকাছি থাকে → ওটাই cluster***      
- ***যেখানে পয়েন্ট কম → ওটা noise / outlier***

***`K-Means`***
- ***আগে থেকে K দিতে হয় (কয়টা cluster)***
- ***centroid দিয়ে গোলাকার cluster বানায়***
- ***সব পয়েন্টকে কোনো না কোনো cluster এ ঢুকায়***
- ***outlier handle করতে পারে না***   
  
***`DBSCAN`***   
- ***আগে থেকে K দিতে হয় না***   
- ***Irregular shape detect করতে পারে.***   
- ***Outlier আলাদা করে.***
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/DBSCAN%20Clustering/images/img02.png" width="600">  

---
## ***How DBSCAN Works***
***DBSCAN clusters data points based on `two parameters`:***   

***`Epsilon (ε)`:   
The maximum distance between two points for them to be considered neighbors.***    
- ***ε বলে দেয় — “কত দূর পর্যন্ত আমি পাশের পয়েন্ট ধরবো”***   
- ***যদি দুইটা পয়েন্টের distance ≤ ε হয়, তাহলে তারা neighbour হিসেবে গণ্য হবে।***   
- ***Let, ε = 0.5 তাহলে, 0.5 distance এর ভিতরে থাকা সব পয়েন্ট neighbour।***   

***`MinPts`:    
The minimum number of points required to form a dense region (cluster).***     
- ***Minimum কতগুলো পয়েন্ট থাকলে একটি জায়গাকে dense area ধরা হবে।***
- ***Let, MinPts = 5 মানে কোনো পয়েন্টের ε radius এর ভিতরে যদি ৫টা বা তার বেশি পয়েন্ট থাকে, তাহলে সেটা dense region.***

---
## ***Key Concepts***   
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/DBSCAN%20Clustering/images/img01.png" width="700">     
  
***`Core points`***  
***Which have a sufficient number of neighbors within a specified radius (eplison).***   
- ***ε (epsilon) radius এর ভিতরে কমপক্ষে MinPts সংখ্যক neighbour আছে।***  

***`Border points`***  
***Which are near core points but lack enough neighbors to be core points themselves.***   
- ***Core Point এর কাছে আছে (ε এর ভিতরে), কিন্তু তার নিজের চারপাশে MinPts নেই।***   

***`Noise points`***   
***Which do not belong to any cluster.***   

---
# ***Algorithm***  
***Step 0: Define Epsilon and MinPts***   
***Step 1: Identify all points as either core point, border point or noise point***   
***Step 2: For all of the unclustered core points***  
***Step 2a: Create a new cluster***  
***Step 2b: add all the points that are unclustered and density connected to the current point into this cluster***   
***Step 3: For each unclustered border point assign it to the cluster of nearest core point***   
***Step 4: Leave all the noise points as it is.***

---
# ***An Example***  
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/DBSCAN%20Clustering/images/img03.png" width="500">     
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/DBSCAN%20Clustering/images/img04.png" width="500">     
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/DBSCAN%20Clustering/images/img05.png" width="700">     
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/DBSCAN%20Clustering/images/img06.png" width="700">     
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/DBSCAN%20Clustering/images/img07.png" width="700">     
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/DBSCAN%20Clustering/images/img08.png" width="700">     

---
# ***Limitations***  
- ***Selecting optimal ε and MinPts values can be challenging.***  
- ***Struggles with varying density clusters.***  
- ***Sensitive to high-dimensional data.***  

---
# ***Resources***
- [***DBSCAN Clustering: Density-Based Approach for Unsupervised Learning***](https://medium.com/@lomashbhuva/dbscan-clustering-density-based-approach-for-unsupervised-learning-0dd0cba82896)   
- [***Visualizing DBSCAN Clustering***](http://naftaliharris.com/blog/visualizing-dbscan-clustering/)

---
## ***Author***   
***MD. RAFIQUL ISLAM***  
***CSE, CoU***   
