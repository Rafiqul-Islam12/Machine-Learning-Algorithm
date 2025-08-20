# **Decision Tree Classification: Mathematical Intuition and Implementation**
A decision tree is a supervised learning algorithm used for **`both classification and regression`** tasks.       
It has a hierarchical tree structure which consists of a root node, branches, internal nodes and leaf nodes. It It works like a flowchart help to make decisions step by step where:         
- Internal nodes represent attribute tests
- Branches represent attribute values
- Leaf nodes represent final decisions or predictions.

### Example
Imagine you want to decide whether wear a jacket based on the weather.      
A decision tree helps you to make this decision by asking series of question about the weather conditions.        

<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Decision%20Tree/images/img01.png" width="700">

### Identify Pure and Impure Splits
**`Pure Split:`** When all examples (or rows) at a split belong to the same category (eg all “Yes” or all “No” for playing outside).          
**`Impure Split:`** When some examples (or rows) at a split belong to different category (eg some “Yes” or some “No” for playing outside).    

### Choosing features to split
**`Entropy:`** Measures randomness or impurity in the data. Lower entropy means more organised data.    
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Decision%20Tree/images/img02.png" width="300">
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Decision%20Tree/images/img03.png" width="450">

**`Information gain:`** Measures how much a feature (question) reduces entropy.        
Higher gain means the feature is good for splitting.       

<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Decision%20Tree/images/img08.png" width="500">    

**`Gini Impurity:`** Measures impurity of data. Lower Gini indicates more purity.                   
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Decision%20Tree/images/img12.png" width="150"> 

## 🔹 Step 1: Root Entropy
Target: Wear Jacket? (Yes = 3, No = 4)            
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Decision%20Tree/images/img04.png" width="350">

## 🔹 Step 2: Information Gain of Each Feature
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Decision%20Tree/images/img05.png" width="550">   
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Decision%20Tree/images/img06.png" width="550">  
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Decision%20Tree/images/img07.png" width="550">            
✅ Best root split = Temperature (IG = 0.522)

## 🔹 Step 3: Branch Expansion
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Decision%20Tree/images/img10.png" width="550">   
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Decision%20Tree/images/img09.png" width="550">   

## ✅ Final Decision Tree
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Decision%20Tree/images/img11.png" width="520">  

# Using Gini Impurity
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Decision%20Tree/images/img13.png" width="520">    
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Decision%20Tree/images/img14.png" width="520">       
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Decision%20Tree/images/img15.png" width="520">       
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Decision%20Tree/images/img16.png" width="480">       
<img src="https://github.com/Rafiqul-Islam12/Machine-Learning-Algorithm/blob/main/Decision%20Tree/images/img17.png" width="570">       

## Entropy vs. Gini Impurity
- **For larger datasets, Gini impurity is often preferred due to its computational efficiency.**
- **Both metrics serve the same purpose but might lead to different decision paths.**

## Author
### Md. Rafiqul Islam
### CSE, CoU
