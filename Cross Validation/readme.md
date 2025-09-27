#### ***Cross-validation is a `model evaluation technique` used to check how well a machine learning model performs on `unseen data` while preventing overfitting. It works by:***
- ***Splitting the dataset into several parts.***
- ***Then trains the model on some parts and tests it on the remaining part.***
- ***We repeat this process multiple times.***
- ***Finally, the model averages results from each validation step.***

---
### ***Types of Cross-Validation***
***1. K-Fold Cross-Validation***  
***2. Stratified K-Fold Cross-Validation***  
***3. Leave-One-Out Cross-Validation (LOOCV)***  
***4. Repeated K-Fold Cross-Validation***  
***5. Nested Cross-Validation***  

---
### ***K-Fold Cross-Validation*** 
- ***Dataset is split into `K equal folds`.***  
- ***Each iteration: `1 fold = test`, `remaining (K–1) folds = train`.***

***`Best for` balanced datasets.*** 

<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Cross%20Validation/images/img01.png" width="650">
 
***Choosing the Value of K***  
- ***Small K (2, 5): Faster computation with increased variance in performance estimates.***
- ***Large K 10, N): Lower variance but higher computational cost.***  
  ***`K = N` corresponds to `Leave-One-Out Cross Validation (LOOCV)`.***

---
### ***Stratified K-Fold Cross-Validation***
***`Same as K-Fold`, but ensures each fold has the same class distribution as the original dataset.***   
- ***`Best for` imbalanced datasets.*** 
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Cross%20Validation/images/img02.png" width="420">

***For example,  
Imagine a binary classification dataset with 100 samples where:***  
- ***80 samples are Yes***
- ***20 samples are No***    

***Using random sampling in an 80:20 split then all 80 Yes in the training set and all 20 No in the test set. In this case model will never learn to classify No and would give misleading accuracy.***
  
***Now, let’s use stratified sampling on same dataset:***   
***1. Training Set (80 samples):***
- ***64 from Yes (80% of 80)***
- ***16 from No (80% of 20)***

***2. Test Set (20 samples):***
- ***16 from Yes (20% of 80)***
- ***4 from No (20% of 20)***

---
### ***Leave-One-Out Cross-Validation (LOOCV)***   
- ***Special case of K-Fold where `K = N`.***   
- ***Each iteration: `1 sample = test`, `remaining = train`.***

***`Best for` Very small datasets.***

---
### ***Author***
***Md. Rafiqul Islam***   
***CSE, CoU***
