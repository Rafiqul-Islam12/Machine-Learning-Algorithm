# ***Hyperparameter Tuning***
***Hyperparameter Tuning মানে হলো, কোনো Machine Learning model-এর best parameters খুঁজে বের করা, যাতে model সবচেয়ে ভালো performance দেয়।*** 

### [***Decision Tree Classifier***](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier)  
  
- ***`criterion` → Node split করার quality measure করে; (সাধারণত gini বা entropy)***
- ***`splitter` → Node split করার strategy; best (best split নেয়) বা random (random split নেয়)।***
- ***`max_depth` → Tree কতটা গভীর (depth) পর্যন্ত grow করবে সেটি নির্ধারণ করে।; overfitting কমাতে limit দেওয়া হয়।***
- ***`min_samples_split` → একটি node split করার জন্য minimum কত sample লাগবে।***
- ***`min_samples_leaf` → leaf node এ minimum কত sample থাকতে হবে।***
- ***min_weight_fraction_leaf → weighted data হলে leaf node এ minimum weight fraction নির্ধারণ করে।***
- ***`max_features` → Node split করার সময় কতগুলো feature consider করা হবে (None, sqrt,log2)***
- ***random_state → random process reproducible করার জন্য seed value।***
- ***max_leaf_nodes → tree এ সর্বোচ্চ কত leaf node থাকতে পারবে।******
- ***min_impurity_decrease → impurity কতটা কমলে split করা হবে তা নির্ধারণ করে।***
- ***class_weight → imbalanced dataset হলে class গুলোর weight adjust করতে ব্যবহৃত হয়।***
- ***ccp_alpha → cost-complexity pruning parameter; বড় tree ছোট করতে pruning করে|***
- ***monotonic_cst → কিছু feature এর monotonic constraint enforce করতে ব্যবহৃত হয় (advanced use)।***
  
***Choosing the right combination of hyperparameters can make a model perform better on unseen data.***     

---
# ***GridSearchCV vs RandomizedSearchCV***    
- ***`GridSearchCV` সব possible parameter combination try করে।***       
- ***`RandomizedSearchCV` সব combination try করে না। Randomly কিছু combination try করে।   
  Let, possible combination = 100, then set, n_iter = 20  
 তাহলে random ভাবে 20টা combination try করবে***

<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Hyperparameter%20Tuning/images/img1.png" width="800">     
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Hyperparameter%20Tuning/images/img2.png" width="800">  

---
### ***Author***  
***MD. RAFIQUL ISLAM***  
***CSE, CoU***  
