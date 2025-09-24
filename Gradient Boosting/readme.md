***Gradient Boosting is an ensemble machine learning technique that builds a strong predictive model by sequentially adding decision trees.***   
- ***`Error Correction`: Each new tree is trained to fix the mistakes (residual errors) of the combined model built so far.***
- ***`Residual Focus`: Instead of fitting trees directly to the target values, Gradient Boosting fits each tree to the residuals (the differences between actual and predicted values).***
- ***`Deeper Trees`: Unlike AdaBoost, which often uses shallow decision stumps (1-split trees), Gradient Boosting typically uses deeper trees as weak learners, allowing it to capture more complex patterns.***

---
### ***Main Mechanism***
- ***`Initialize Model`: Start with a simple prediction, typically the mean of target values.***     
- ***`Iterative Learning`: For a set number of iterations, compute the residuals, train a decision tree to predict these residuals, and add the new tree’s predictions (scaled by the learning rate) to the running total.***   
- ***`Build Trees on Residuals`: Each new tree focuses on the remaining errors from all previous iterations.***   
- ***`Final Prediction`: Sum up all tree contributions (scaled by the learning rate) and the initial prediction.***

---
### ***Key differences from AdaBoost***
- ***max_depth is typically higher (3-8) in Gradient Boosting, while AdaBoost prefers stumps.***   
- ***No sample_weight updates because Gradient Boosting uses residuals instead of sample weighting.***
- ***The learning_rate is typically much smaller (0.01-0.1) compared to AdaBoost's larger values (0.1-1.0).***
- ***Initial prediction starts from the mean while AdaBoost starts from zero.***
- ***Trees are combined through simple addition rather than weighted voting, making each tree’s contribution more straightforward.***
- ***Optional subsample parameter adds randomness, a feature not present in standard AdaBoost.***

---
### ***Resources***
- [***Mathematical Intuition of Gradient Boosting***](https://medium.com/data-science/gradient-boosting-regressor-explained-a-visual-guide-with-code-examples-c098d1ae425c)

---
### ***Author***
***Md. Rafiqul Islam***  
***CSE, CoU***  
