# ***Curse of Dimensionality***

---
- ***Feature (dimension) যত বাড়ে, data তত sparse হয়ে যায়,    
আর model এর শেখা তত কঠিন হয় — এটাই Curse of Dimensionality।***  

***Sparse = Data point গুলো এক জায়গায় জমে না থেকে অনেক দূরে দূরে ছড়িয়ে থাকে → এটাকেই বলে sparse data***   

***যখন dataset-এর feature (dimension) সংখ্যা খুব বেশি হয়ে যায়, তখন data space এত বড় হয়ে যায় যে সীমিত data দিয়ে machine learning model ভালোভাবে pattern শিখতে পারে না।***  
- ***1 feature → 1D***
- ***2 feature → 2D***
- ***10+ feature → High-Dimensional space***   
***Feature যত বাড়ে, space তত exponentially বড় হয়***
 
🔹🔹🔹     
***High dimension এ Distance Meaningless হয়ে যায়  
সব point-এর দূরত্ব প্রায় সমান হয়ে যায়   
মানে:   
Nearest neighbor ≈ Farthest neighbor   
“কাছের point” বলে কিছু থাকে না   
তাই distance-based algorithm fail করে***   
  
***Example: KNN   
Low dimension → nearest neighbor সত্যিই কাছের  
High dimension → সব neighbor প্রায় same দূরত্বে***  
- ***KNN confuse হয়***
- ***Accuracy কমে যায়***

⚠️    
***Highly affected   
KNN    
K-means   
DBSCAN   
SVM (high-dim kernel)     
Decision Tree   
Random Forest***  

🔹🔹🔹   
***Curse Dimensionality দূর করার উপায়***  
1. ***Dimensionality Reduction   
PCA  
LDA  
Autoencoder***  
2. ***Feature Selection  
Unimportant feature বাদ  
Correlated feature remove***   
3. ***More Data  
Feature বাড়ালে  
Data ও বাড়াতে হবে***   

---
# ***Principal Component Analysis (PCA)***  

---
- ***Dimensionality Reduction technique***
- ***বেশি feature (dimension) থাকা dataset থেকে কম সংখ্যক নতুন feature তৈরি করে,   
যেখানে যতটা সম্ভব গুরুত্বপূর্ণ information (variance) ধরে রাখা হয়।***

- ***PCA দরকার beacuse-***  
***Feature Extraction  
Curse of Dimensionality handle করতে    
Model faster করার জন্য   
Overfitting কমানোর জন্য   
Visualization করার জন্য     
Distance-based algorithm ঠিকভাবে কাজ করানোর জন্য   
Noise reduction এর জন্য***

***PCA Finding:***
- ***“কোন direction এ data project করলে variation (spread) সবচেয়ে বেশি থাকবে?”***

--- 
# PCA: Step by Step

***`Step 1`: Standardize the Data      
সব features কে mean 0, std 1 এ আনা হয়।      
Scale mismatch থাকলে বড় scale dominate করে, তাই standardize করা জরুরি।***     
- ***“সব feature কে same starting line এ দাঁড় করানো।”***   

***`Step 2`: Compute Covariance Matrix***   
***Covariance matrix বের করা হয়, যা feature গুলোর correlation দেখায়।    
কোন feature একে অপরের সাথে কতো closely related, সেটাই বোঝা।***   

***`Step 3`: Compute Eigenvalues & Eigenvectors   
Covariance matrix থেকে eigenvalues ও eigenvectors বের করা হয়।***   
- ***Eigenvector → direction (axis)***   
- ***Eigenvalue → variance along that direction (importance)***    
- ***বড় eigenvalue → সবচেয়ে বেশি information***   
- ***ছোট eigenvalue → noise / less important***   

***`Step 4`: Select Principal Components   
Eigenvalues descending order এ সাজানো হয়।    
Top k eigenvectors (highest eigenvalues) নির্বাচন করা হয়।    
Tools: Scree plot (variance plot) ব্যবহার করে decision করা যায়।***   
- ***“সবচেয়ে important info প্রথম component এ, কম important info বাদ।”***   

***`Step 5`: Form Feature Vector   
Top k eigenvectors কে একটি matrix আকারে সাজানো হয়।   
এ matrix হচ্ছে Feature Vector।    
এটা সেই axis যেখানে আমরা original data project করব।    
কম dimension, কিন্তু maximum info retained।***   

***`Step 6`: Transform Original Dataset   
Original data rotate হয়ে নতুন axis-এ চলে আসে।   
Dimension reduce, information retained।***   

***`Step 7`: Reconstruct Data   
প্রথম few principal component ব্যবহার করে approximate original data পাওয়া যায়।   
Low-variance component বাদ দিলেও data almost same থাকে।  
Noise remove হয়।***   

---
# ***Important Resources for Understaning Math***   
- [***Mathematical Approach to PCA in Geeksforgeeks***](https://www.geeksforgeeks.org/machine-learning/mathematical-approach-to-pca/)
- [***Awesome Mathematical Intuition***](https://medium.com/analytics-vidhya/the-math-of-principal-component-analysis-pca-bf7da48247fc)
- [***PCA And It’s Underlying Mathematical Principles***](https://www.analyticsvidhya.com/blog/2021/09/pca-and-its-underlying-mathematical-principles/)


