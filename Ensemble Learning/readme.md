### ***`Goal`***:
***Combining the predictions of multiple individual models (learners) to create a more robust and accurate model.***  
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Ensemble%20Learning/images/img01.png" width="600">  

## ***Bagging vs Boosting***
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Ensemble%20Learning/images/img02.png" width="700">  

| Aspect | **Bagging (Bootstrap Aggregating)**  | **Boosting**  |
|--------|--------------------------------------|----------------|
| **Main Idea** | Build multiple independent models in **parallel** and then combine them (majority vote/average). | Build models **sequentially**, each new model learns from mistakes of the previous ones. |
| **Goal / Focus** | Reduce **variance** (handles overfitting problem). | Reduce both **bias & variance** (makes weak learners stronger). |
| **How Data is Used** | Creates different **random subsets** of data (sampling **with replacement**, called bootstrap samples). | Uses the **entire dataset**, but assigns **higher weights to misclassified data** in the next round. |
| **Training Style** | All models trained **independently** (parallel). | Models trained **dependently** (one after another). |
| **Model Weighting** | All models usually have **equal weight** when combining results. | Models are given **different weights** depending on their performance (better models get more say). |
| **Combination Method** | Classification → **Majority voting**; Regression → **Averaging**. | Classification/Regression → **Weighted sum / weighted voting**. |
| **Examples** | Random Forest, Bagged Decision Trees. | AdaBoost, Gradient Boosting, XGBoost, LightGBM, CatBoost. |  

**In short:**  
- **Bagging = Parallel, reduces variance, simple average.**  
- **Boosting = Sequential, reduces both bias & variance, weighted combination.**
---

#### Example 

- **Bagging:**  
  Imagine you want to know the winner of a sports match. You ask 100 random people separately (independent opinions). Then, you go with the majority opinion.  
  → Reduces noise (**variance**).  

- **Boosting:**  
  Imagine teaching a weak student. First, you give a test → student makes mistakes. Next, you give another test focusing **only on mistakes** → student improves. Repeat this many times.  
  → Reduces ignorance (**bias**).  

---
## Author
### ***MD. RAFIQUL ISLAM***
### ***CSE, CoU***
