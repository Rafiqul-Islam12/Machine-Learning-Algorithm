#### ***Random Forest is an `ensemble learning` algorithm based on `bagging`.***
#### ***It builds a `"forest" of decision trees` and combines their results to get a stronger, more accurate prediction.***

<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Random%20Forest/images/img01.png" width="800">  

#### ***`Step 1`: Row Sampling (Bootstrap Sampling) + Feature Sampling (Random Feature Selection)***  
***From the original dataset, Random Forest creates random subsets of rows.***  
***At each split in a tree, Random Forest does not check all features.***  
***Instead, it randomly picks a subset of features (columns) and finds the best split only among those.***  

***Row Sampling → reduces overfitting by ensuring trees don’t all see the same data.***  
***Feature Sampling → reduces correlation between trees (they don’t all split on the same features).***  

#### ***`Step 2`: Build Many Decision Trees***
***Each tree is trained using different sampled rows + different sampled features.***  
***As a result, every tree learns something unique.***  

#### ***`Step 3`: Prediction***
***Combining results → makes the model robust, accurate, and generalizable.***  
- ***For Classification → Majority voting.***  
- ***For Regression → Averaging(Mean).***

---

### ***Advantages***
***1. Handles Missing Data: It can work even if some data is missing so you don’t always need to fill in the gaps yourself.***  
***2. Shows Feature Importance: It tells you which features (columns) are most useful for making predictions which helps you understand your data better.***  

---
### ***Example***
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Random%20Forest/images/img02.png" width="720">  

---
### ***Out-of-Bag (OOB) Evaluation in Random Forest***
***In Random Forest, each tree is trained on a `random subset of rows` (with replacement).***   
***Some rows are never selected in this subset.***   
***These unused rows are called `Out-of-Bag (OOB)` samples.***   

#### ***`OOB Evaluation`***
***1. For each tree:***  
   - ***Use the OOB samples (rows not used for training that tree) to make predictions.***   
    
***2. Combine predictions from all trees for each OOB sample:***
   - ***Classification: Majority vote***  
   - ***Regression: Averaging(Mean)***

***3. Compare predictions with actual labels to compute OOB Score or OOB Error.***  
   - ***OOB Score: Accuracy (for classification) or R² (for regression) on OOB samples.***
   - ***OOB Error = 1 - OOB Score***
---
### ***Decision Tree vs Random Forest***
- ***Decision Tree = One model → simple but unstable.***  
  ***Like asking one friend for advice. If that friend is wrong, you get the wrong answer.***
  
- ***Random Forest = Many trees → strong, accurate, and stable.***  
  ***Like asking 100 friends for advice. You take the majority opinion → more reliable.***   

---
### ***Author***
***MD. RAFIQUL ISLAM***  
***CSE, CoU***  
