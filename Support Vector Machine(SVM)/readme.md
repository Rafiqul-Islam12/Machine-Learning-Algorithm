#### **`Main Goal`**: ***Find the best boundary (hyperplane) that separates different classes of data points.***  
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Support%20Vector%20Machine(SVM)/images/img01.png" width="600">  

#### **`Hyperplane`**: ***A decision boundary separating different classes in feature space and is represented by the equation wx + b = 0 in linear classification.***  
#### **`Support Vectors`**: ***The closest data points to the hyperplane.***  
#### **`Margin`**: ***The distance between the hyperplane and the support vectors. SVM aims to maximize this margin for better classification performance.***  

***To classify a point as negative or positive we need to define a decision rule. We can define decision rule as:***  
 <img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Support%20Vector%20Machine(SVM)/images/img03.png" width="220">  
***If the value of `w.x+b>0` then we can say it is a `positive point` otherwise it is a `negative point`. Now we need (w,b) such that the margin has a maximum distance. Let’s say this distance is `‘d’`.***  
 <img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Support%20Vector%20Machine(SVM)/images/img02.png" width="340">   
***To calculate ‘d’ we need the equation of L1 and L2. For this, we will take few assumptions that the equation of L1 is w.x+b=1 and for L2 it is w.x+b=-1.***  
### **`Hard Margin`**
