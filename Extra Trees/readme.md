***`Extra Trees` stands for `Extremely Randomized Trees`. It is an ensemble learning method used for regression and classification, very similar to Random Forest, but with more randomness.***  

---
### ***Main Mechanism***
***1. `Full Dataset Usage`***  
       ***Unlike Random Forest, each tree uses the complete training dataset rather than a bootstrap sample.***  
       
***2. `Random Feature Selection`  
       When making a split, each tree only considers a random subset of features (typically square root of total features), similar to Random Forest.***  
       
***3. `Random Split Selection`  
The key difference is in splitting — instead of searching for the optimal threshold, Extra Trees randomly generates several split points for each feature and picks the best among these random splits. This makes it much faster than Random Forest.***  

***4. `Growing Trees`  
Each tree grows using these extremely randomized splits until it reaches a stopping point (like pure groups or minimum sample size).***  

***5. `Final Prediction`***  
- ***For Classification → Majority voting.***  
- ***For Regression → Averaging(Mean).***

---
### ***Resources***
- [***An awesome explanatory article***](https://medium.com/@samybaladram/extra-trees-explained-a-visual-guide-with-code-examples-4c2967cedc75)

---
### ***Author***
***Md. Rafiqul Islam***  
***CSE, CoU***
