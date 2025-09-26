# My Learning Roadmap

### ***Regression Algorithm***
- [***Simple Linear Regression***](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Linear%20Regression/Simple%20Linear%20Regression.ipynb)
- [***Multiple Linear Regression***](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Linear%20Regression/Multiple%20Linear%20Regression.ipynb)
- [***Polynomial Regression***](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Polynomial%20Regression/Polynomial%20Regression.ipynb)
- [***Gradient Descent***](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Polynomial%20Regression/Polynomial%20Regression.ipynb)
  
---
- [***Bias & Variance***](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Regression%20Analysis/Bias%20%26%20Variance.ipynb)
- [***Overfitting and Underfitting Concepts***](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Regression%20Analysis/Overfitting%20and%20Underfitting%20Concepts.ipynb)
- [***Train-Test Split***](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Regression%20Analysis/Train-Test%20Split.ipynb)
- [***Pearson Correlation Coefficient***](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Regression%20Analysis/Pearson%20Correlation%20Coefficient.ipynb)
- [***Confusion Matrix***](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/tree/main/Confusion%20Matrix)
---
### ***Classification Algorithm***
- [***K-Nearest Neighbor(KNN)***](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/tree/main/K-Nearest%20Neighbor(KNN))
   - [***KNN Classifier***](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/K-Nearest%20Neighbor(KNN)/KNN%20Classifier.ipynb)
   - [***KNN Regressor***](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/K-Nearest%20Neighbor(KNN)/KNN%20Regressor.ipynb)
- [***Logistic Regression***](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/tree/main/Logistic%20Regression)
- [***Support Vector Machine(SVM)***](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/tree/main/Support%20Vector%20Machine(SVM))
- [***Decision Tree***](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/tree/main/Decision%20Tree)
- [***Ensemble Learning***](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/tree/main/Ensemble%20Learning)
  - ***Bagging***
    - [***Random Forest***](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/tree/main/Random%20Forest)
    - [***Extra Trees***](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Extra%20Trees/Extra%20Trees%20Classifier.ipynb)
  - ***Boosting***
    - [***AdaBoost***](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/tree/main/AdaBoost%20Algorithm)
    - [***Gradient Boosting***](https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/tree/main/Gradient%20Boosting)
    - [***XGBoost***]()
---
### ***Feature-Engineering***
- [***Handling NaN Values***](https://github.com/Rafiqul-Islam12/Feature-Engineering/blob/main/1.%20Handling%20NaN%20Values.ipynb)
- [***Encoding Without Encoder Techniques***](https://github.com/Rafiqul-Islam12/Feature-Engineering/blob/main/2.%20Encoding%20Without%20%20Encoder%20Techniques.ipynb)
- [***Label Encoder***](https://github.com/Rafiqul-Islam12/Feature-Engineering/blob/main/3.%20Label%20Encoder.ipynb)
- [***One-Hot Encoding***](https://github.com/Rafiqul-Islam12/Feature-Engineering/blob/main/4.%20One-Hot%20Encoding.ipynb)
- [***Binary Encoder***](https://github.com/Rafiqul-Islam12/Feature-Engineering/blob/main/5.%20%20Binary%20Encoder.ipynb)
- [***Ordinal Encoder***](https://github.com/Rafiqul-Islam12/Feature-Engineering/blob/main/6.%20Ordinal%20Encoder.ipynb)
- [***Hashing Encoder***](https://github.com/Rafiqul-Islam12/Feature-Engineering/blob/main/7.%20Hashing%20Encoder.ipynb)

---
# Important Syntex
### ***Import Libraries***  
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings as wr
wr.filterwarnings('ignore')
```
### ***Train-Test Split***  
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
```

### ***Loss & Cost Functions***  
```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, root_mean_squared_error
mae = mean_absolute_error(actual_y, predicted_y)
mse = mean_squared_error(actual_y, predicted_y)
rmse = root_mean_squared_error(actual_y, predicted_y)
```
```python
from sklearn.metrics import r2_score
r2_score(actual_y, reg.predict(X_test))
```
```python
model.score(X_train,y_train)
```

### ***Confusion Matrix***  
```python
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score,
                            precision_score, recall_score, f1_score
```
```python
cm = confusion_matrix(actual,predicted)
```
```python
sns.heatmap(cm, 
            annot=True,
            xticklabels=['Label-01','Label-02'],
            yticklabels=['Label-01','Label-02'],
            cmap="Blues")
plt.title('Confusion Matrix', fontsize=17, pad=20)
plt.xlabel('Prediction', fontsize=13)
plt.ylabel('Actual', fontsize=13)
plt.gca().xaxis.set_label_position('top') 
plt.gca().xaxis.tick_top()

plt.show()
```
```python
print(classification_report(actual, predicted))
```
```python
print(accuracy_score(actual,predicted))
print(precision_score(actual,predicted,average=None))
print(recall_score(actual,predicted,average=None))
print(f1_score(actual,predicted,average=None))
```

---
### ***Author***
***Md. Rafiqul Islam***  
***CSE, CoU*** 


