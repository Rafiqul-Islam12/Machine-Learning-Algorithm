# Gradient Descent

## Overview
Gradient Descent is an **iterative optimization algorithm** used to find the **minimum** of a function.  

In Machine Learning, its main purpose is to **minimize the Cost Function (Loss Function)** by updating model parameters step-by-step.

**Goal:**  
- Find parameters (like weights `w`, bias `b`) that give the smallest possible cost.   
- The smaller the cost, the better the model fits the data.
- **Machine Learning-এ এর প্রধান কাজ হলো Cost Function (Error) কমানো।**

## Why do we need Gradient Descent?
- ML models often have thousands, millions, or even billions of parameters.
- Solving for the minimum analytically (using calculus) is often impossible.
- Gradient Descent finds the minimum **step-by-step** without solving the equations directly.
- **অনেক মেশিন লার্নিং মডেলে ডেটার পরিমাণ ও প্যারামিটারের সংখ্যা অনেক বেশি হয়।**
- **এখানে ক্যালকুলাস দিয়ে সরাসরি Minima বের করা প্রায় অসম্ভব।**
- **Gradient Descent হলো ধাপে ধাপে মিনিমামের দিকে এগোনোর পদ্ধতি।**

# Core Idea
This straight line is represented using the following formula:            `y = mx + c`          
![Alt text](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Gradient%20Descent/images/image01.png)

## **Cost Function**   
![Alt text](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Gradient%20Descent/images/img02.png)
![Alt text](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Gradient%20Descent/images/img03.png)

## Gradient Descent Algorithm
### **Step-1:**   
 Let, `m = 0` and `c = 0`. Let `L = 0.01`       
 L be our learning rate. It could be a small value like 0.01 for good accuracy.

- **Learning rate** gives the rate of speed where the gradient moves during gradient descent.          
  Setting it too high would make your path instable, too low would make convergence slow.      
  Put it to zero means your model isn’t learning anything from the gradients.

### **Step-2: Compute Gradient**       
Calculate the partial derivative of the Cost function with respect to m.        
Let partial derivative of the Cost function with respect to m be Dm.            
![Alt text](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Gradient%20Descent/images/img04.png)

Similarly, let’s find the partial derivative with respect to c.         
Let partial derivative of the Cost function with respect to c be Dc.             
![Alt text](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Gradient%20Descent/images/img05.png)         

### **Step-3: Update the current values of m and c**            
![Alt text](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Gradient%20Descent/images/img06.png)          
 
### **Step-4: Repeat step 2 & 3**             
We will repeat this process until our Cost function is very small (ideally 0).

---
# Aurhor:
**Md. Rafiqul Islam**      
**CSE, CoU**
