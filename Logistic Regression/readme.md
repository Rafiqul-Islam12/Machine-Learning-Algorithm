## **Linear Regression Vs. Logistic Regression**
| Linear Regression | Logistic Regression |
|-------------------|-------------------|
| Predicts continuous values| Predicts categorical values|
| Uses best fit-line| Uses sigmoid S-curve|
| Solved regression problems| Solved classification problems|  
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Logistic%20Regression/images/img01.png" width="800">

### **Sigmoid function**
***Sigmoid function converts the continuous variable data into the `probability` i.e between 0 and 1.***     
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Logistic%20Regression/images/img03.png" width="400">    
***If x → +∞ → output ≈ 1***  
***If x → −∞ → output ≈ 0***   
***If x = 0 → output = 0.5*** 

- ***If the output of the sigmoid function is more than 0.5, we can classify the outcome as 1 or YES.***   
- ***If it is less than 0.5, we can classify it as 0 or NO.***  
#### **Example**  
***If the sigmoid output = 0.82***  
***- Means the probability of Class 1 = 82%***  
***- Since it’s greater than 0.5 → Predict YES (Class 1)***  

***If the sigmoid output = 0.23***  
***- Probability of Class 1 = 23%***   
***- Since it’s less than 0.5 → Predict NO (Class 0)***  

<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Logistic%20Regression/images/img02.png" width="700">  


## **Types of Logistic Regression**
**`Binary Logistic Regression`**: **The target variable has only two possible outcomes such as Spam or Not Spam.**  
**`Multinomial Logistic Regression`**: **The target variable has three or more nominal categories, such as predicting the type of Wine.**  
**`Ordinal Logistic Regression`**: **The target variable has three or more ordinal categories, such as product rating from 1 to 5.**  

## Author
### **Md. Rafiqul Islam**
### **CSE, CoU**
