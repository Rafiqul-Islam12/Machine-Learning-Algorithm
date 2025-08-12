# Gradient Descent
Gradient Descent is an **iterative optimization algorithm** used to find the **minimum** of a function.  

### **Goal:**
In Machine Learning, its main purpose is to **minimize the Cost Function (Loss Function)** by updating model parameters step-by-step.
  
## Why do we need Gradient Descent?
- ML models often have thousands, millions, or even billions of parameters.
- Solving for the minimum analytically (using calculus) is often impossible.
- Gradient Descent finds the minimum **step-by-step** without solving the equations directly.

## Gradient Descent Terminology
**`1. Learning Rate (L):`** Gives the rate of speed where the gradient moves during gradient descent.        
- Setting it too high would make your path instable, too low would make convergence slow.       
- Put it to zero means your model isn’t learning anything from the gradients.
- ***Small learning rate → moves down slowly, takes longer to reach the correct solution (minima).***               
- ***Large learning rate → takes bigger jumps, can reach faster, but if too large it may overshoot the solution and keep bouncing without reaching it.***

**`2. Iteration & Epoch`**
- Iteration: One update of parameters after looking at some data.   
- Epoch: One complete pass over the whole dataset.       
- Example: If you have 1000 data points and update parameters every 100 points, you have 10 iterations in 1 epoch.

**`3. Cost Function`**                   
A straight line is represented using the following formula: `y = mx + c`    
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Gradient%20Descent/images/image01.png" width="300">
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Gradient%20Descent/images/img02.png" width="300">
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Gradient%20Descent/images/img03.png" width="330">
 
**`4. Global Minimum`**       
- The absolute lowest point of the cost function.           
- Best possible solution.        

**`5. Local Minimum`**      
- A point lower than surroundings but not the lowest overall.         
- GD can get stuck here if learning rate is small or function is complex.

**`6. Convergence`**
- The point where updates become very small, meaning the model has reached the minimum (or close enough).
- It means we’re already at, or very close to, the lowest possible cost (minimum), so further steps won’t improve the model much.  

**`7. Example`**   
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Gradient%20Descent/images/img07.png" width="1200">

# Gradient Descent as an Iterative Method
An iterative method is a way of **solving problems step-by-step**, where each step **uses the result of the previous step** to get **closer to the solution**.     

**`Principle:`**    
***Use the result from the previous step to produce a better result in the next step, and repeat until changes become so small that you’ve practically reached the solution.***

**`3 steps:`**             
**Initial Guess** → Start with some starting values (even if they are wrong)              
**Update Rule** → Apply a formula to improve the guess.            
**Stop Condition** → Keep going until the improvement is very tiny (convergence).    

**`Example in Gradient Descent`**           
**Initial Guess** → Guess m and c              
**Update Rule** → Update them using derivatives to move toward the cost function’s minimum            
**Stop Condition** → Repeat until the slope of the cost curve is almost zero             

# Gradient Descent Algorithm
### **Step-1:**   
 Let, `m = 0` and `c = 0`. Let `L = 0.01`       
 L be our learning rate. It could be a small value like 0.01 for good accuracy.

### **Step-2: Compute Gradient**       
Calculate the partial derivative of the Cost function with respect to m.        
Let partial derivative of the Cost function with respect to m be Dm.        
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Gradient%20Descent/images/img04.png" width="350">               

Similarly, let’s find the partial derivative with respect to c.         
Let partial derivative of the Cost function with respect to c be Dc.             
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Gradient%20Descent/images/img05.png" width="350">       

### **Step-3: Update the current values of m and c**            
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Gradient%20Descent/images/img06.png" width="120">         
 
### **Step-4: Repeat step 2 & 3**             
We will repeat this process until our Cost function is very small (ideally 0).

# Types of Gradient Descent
1. Batch Gradient Descent (BGD)
2. Stochastic Gradient Descent (SGD)
3. Mini-batch Gradient Descent

# Resources
### **Gradient Descent in Linear Regression**
[01. Gradient Descent in Linear Regression](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Gradient%20Descent/01.%20Gradient%20Descent%20in%20Linear%20Regression.ipynb)                        
[02. Gradient Descent in Linear Regression](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Gradient%20Descent/02.%20Gradient%20Descent%20in%20Linear%20Regression.ipynb)               

### **Youtube Resources**  
`Iftikhar Hasan`
[Class-01](https://youtu.be/ccaH1gCVXiw?si=GH1XaWxZWLcqtNkY)
[Class-02](https://youtu.be/YazrR76V2wQ?si=1BnWVe3H4YccwjUI)       

`STUDY MART`
[Class-01](https://youtu.be/5YNP5B5NtTw?si=iYKKLeRb3XQs-Q52)
[Class-02](https://youtu.be/NG4P2V1hAb0?si=dkkejXGmh7NnxKEm)
[Class-03](https://youtu.be/P_rSOHZETsM?si=jfEkQP9WK-o0Z2Kz) 

---
## Author:
**Md. Rafiqul Islam**      
**CSE, CoU**
