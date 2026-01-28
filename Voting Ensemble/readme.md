# ***Voting Ensemble***

***In this technique, we use `different machine learning models` that will train on the `same dataset` to make `classification` or `regression` predictions.***

***Assumptions to be taken in voting technique:***
- ***The base model should be different.***
- ***The accuracy of each model should be greater than 50%. The final accuracy depends on the prediction probabilities of each model.***

***As we are using many base models, the effect of poor performance by one algorithm can be managed by the strong performance model.***

- ***একাধিক আলাদা model (weak/strong learners) একসাথে prediction দেয়***
- ***আর সবচেয়ে বেশি ভোট পাওয়া result-টাই final output হয়।***

---
## ***For Classification***
### ***`Hard Voting`***  
***The final prediction is based on the majority vote of individual classifiers. For instance, if three classifiers predict [Class A, Class B, Class A], the final prediction will be Class A.***  
- ***প্রতিটা model class label predict করে***  
- ***যে class টা সবচেয়ে বেশি vote পায় → final prediction***  

### ***`Soft Voting`***  
***Instead of counting votes, it averages the predicted probabilities of each classifier and selects the class with the highest probability.***   
- ***প্রতিটা model probability predict করে***  
- ***সব probability average করা হয়***
- ***যেটার probability বেশি → final class***   
     
***Example-01***     
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Voting%20Ensemble/images/img01.png" width="800">

***Example-02***   
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Voting%20Ensemble/images/img02.png" width="800"> 

---
## ***Why Use Voting Classifiers?***
***Voting classifiers improve performance when individual models have different decision boundaries. Here are some key benefits:***   
- ***Single model এর weakness কমায়***
- ***Overfitting কমে***
- ***Accuracy & stability বাড়ে***
- ***Different algorithm এর strength combine করা যায়***

---
## ***Weighted Voting*** 
***Weighted Voting হলো Voting Ensemble-এর advanced version, যেখানে সব model-কে সমান গুরুত্ব দেওয়া হয় না।***
- ***যেই model বেশি accurate / reliable → তাকে বেশি weight দেওয়া হয়***
- ***যেই model তুলনামূলক দুর্বল → তাকে কম weight দেওয়া হয়***
  
***Hard / Soft Voting এ ধরে নেওয়া হয়:***
- ***“সব model সমান ভালো”***
- ***কিন্তু বাস্তবে, Logistic Regression হয়তো 90% accurate, KNN হয়তো 75% accurate***

***তাহলে Logistic-এর opinion বেশি important হওয়া উচিত***   
***এই সমস্যাটাই Weighted Voting solve করে।***

***`Example`***  
***ধরি 3টা model:***

|***Model***|***Prediction***|***Weight***|
|---|---|---|
|***Decision Tree***|***Yes***|***1***|
|***Logistic Regression***|***Yes***|***3***|
|***KNN***|***No***|***1***|

***Weighted vote count:***
- ***Yes = 1 + 3 = 4***
- ***No = 1***
- ***Final Prediction = Yes***
 
