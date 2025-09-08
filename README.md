# My Learning Roadmap

# Important Syntex

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
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score
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



