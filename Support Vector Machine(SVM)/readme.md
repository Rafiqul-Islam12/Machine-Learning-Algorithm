#### **`Main Goal`**: ***Find the best boundary (hyperplane) that separates different classes of data points.***  
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Support%20Vector%20Machine(SVM)/images/img01.png" width="600">  

#### **`Hyperplane`**: ***A decision boundary separating different classes. Mathematically, it is represented as:***  ***`wx + b = 0`***  
***where:***  
- ***w is the weight vector (determines orientation of the hyperplane)***
- ***x is the feature vector (data points)***
- ***b is the bias term (determines the offset from the origin)*** 
#### **`Support Vectors`**: ***The closest data points to the hyperplane.***  
#### **`Margin`**: ***The distance between the hyperplane and the support vectors. SVM aims to maximize this margin because:***  
***1. A larger margin reduces overfitting, improving generalization.***  
***2. It ensures the model is more robust to small variations in data.***  

# Mathematical Intuition
***If the value of `w.x+b>0` then we can say it is a `positive point` otherwise it is a `negative point`.***  
***Now we need (w,b) such that the margin has a maximum distance. Let’s say this distance is `‘d’`.***  
 <img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Support%20Vector%20Machine(SVM)/images/img02.png" width="320">   
***To calculate ‘d’ we need the equation of L1 and L2.***  
***For this, we will take few assumptions that the equation of `L1 is w.x+b=1` and `L2 is w.x+b=-1`.***  
***Mathematically, the margin width is given by:***  2/(||w||)

***For better understanding:*** [Read This](https://www.analyticsvidhya.com/blog/2021/10/support-vector-machinessvm-a-complete-guide-for-beginners/)  

### **`Hard Margin`**
***A maximum-margin hyperplane that perfectly separates the data without misclassifications.***  
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Support%20Vector%20Machine(SVM)/images/img05.png" width="420">  
***The equation which we have to maximize is:***  
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Support%20Vector%20Machine(SVM)/images/img06.png" width="480">   
### **`Soft Margin`**
***In reality, data is not perfectly separable. Some points may fall inside the margin or even be misclassified.***  
***Soft Margin allows few misclassifications that means it allows few points to be wrongly classified.***  
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Support%20Vector%20Machine(SVM)/images/img04.jpg" width="420">  
***The equation which we have to minimize is:***  
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Support%20Vector%20Machine(SVM)/images/img07.png" width="480">   
***In Soft margin equation, we add 2 more terms which is `zeta` and multiply that by a `hyperparameter ‘c’`***  
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Support%20Vector%20Machine(SVM)/images/img08.png" width="310">   
***So now we can say that,***  
***`SVM Error = Margin Error + Classification Error.`***  
- ***If 𝜉 = 0 → point is correctly classified outside the margin.***
- ***If 0 < 𝜉 < 1 → point is inside the margin but still correctly classified.***
- ***If 𝜉 > 1 → point is misclassified.***

***`C` is a regularization parameter***  
- ***High C: model focuses on reducing misclassification (narrow margin).***
- ***Low C: model allows more misclassifications but keeps margin wider.***  

***For Example:***   
***Let’s say you take a high value of ‘c’ =1000, this would mean that you don’t want to focus on margin error and just want a model which doesn’t misclassify any data point.***  

<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Support%20Vector%20Machine(SVM)/images/img09.png" width="710">  

***If you don’t want any misclassification in the model then you can choose figure 2. That means we’ll increase ‘c’ to decrease Classification Error but if you want that your margin should be maximized then the value of ‘c’ should be minimized.***  

#### `Final SVM optimization = Margin Maximization + Hinge Loss Minimization.`  

## Author
### ***Md. Rafiqul Islam***
### ***CSE, CoU***
