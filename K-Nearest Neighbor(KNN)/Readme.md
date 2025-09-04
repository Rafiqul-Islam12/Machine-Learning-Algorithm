# K-Nearest Neighbor(KNN) Algorithm
### ***`KNN` can be used for `both classification and regression.`***  
#### ***Consider the following example:***
| ID  | Age | Height | Weight |
|-----|-----|--------|--------|
| 1   | 45  | 5.0    | 77     |
| 2   | 26  | 5.11   | 47     |
| 3   | 30  | 5.6    | 55     |
| 4   | 34  | 5.9    | 59     |
| 5   | 40  | 4.8    | 72     |
| 6   | 36  | 5.8    | 60     |
| 7   | 19  | 5.3    | 40     |
| 8   | 28  | 5.8    | 60     |
| 9   | 23  | 5.5    | 45     |
| 10  | 32  | 5.6    | 58     |
| 11  | 38  | 5.5    | ?      |  
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/K-Nearest%20Neighbor(KNN)/images/img02.png" width="520">  

**`Step 1:`** **Calculating Distance**  
**The most common distance metric is the Euclidean distance:**    

$$
**d(x, y) = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2}**
$$

<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/K-Nearest%20Neighbor(KNN)/images/img03.png" width="520"> 

**`Step 2:`** **Selecting the Optimal Value of K**  
**K is the number of nearest neighbors to consider when making a prediction.**  
**Choosing the right value of K is important:**   
- **Small K → Model is more sensitive to noise (overfit).**  
- **Large K → Model is smoother but may ignore local patterns (underfit).**  

**Common practice: Use cross-validation to find the K that gives the best performance on validation data.**   

**`Step 3:`** **Making Predictions**  
**For Regression, take the average (mean) of the values of the K nearest neighbors.**  

- **K = 3** **→ Take 3 nearest neighbors**  
**Smallest distances: 1, 5, 6**  
**Predicted Weight = mean = (77 + 72 + 60) / 3 = 69.6 kg**  

<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/K-Nearest%20Neighbor(KNN)/images/img04.png" width="600">  

- **K = 5 → Take 5 nearest neighbors**  
**Smallest distances: 1, 5, 6, 4, 10**  
**Predicted Weight = mean = (77 + 72 + 60 + 59 + 58) / 3 = 65.2 kg**

<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/K-Nearest%20Neighbor(KNN)/images/img05.png" width="600">  

**`For Classification (Majority Voting)`**  
**The class with the highest frequency is assigned to the new data point.**  
**Example: If among 5 neighbors → 3 are “Spam” and 2 are “Not Spam”, the prediction = Spam.**  

## Aurthor  
**Md. Rafiqul Islam**  
**CSE, CoU**  







