# ============================================
# Maternal Continuum of Care (CoC) Prediction
# Python version using scikit-learn
# Converted from COC_ML_Rcode.R
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                            f1_score, roc_auc_score, roc_curve, confusion_matrix,
                            classification_report, ConfusionMatrixDisplay)
from imblearn.over_sampling import SMOTE
from boruta import BorutaPy
import shap
import warnings
warnings.filterwarnings('ignore')

# For reproducibility
np.random.seed(123)

# ============================================
# 1. DATA LOADING (instead of read.dta)
# ============================================

# Load the Stata file
# Option 1: If you have .dta file
data = pd.read_stata("D:\\New folder\\COC_Data2.dta")

# Option 2: If you have CSV
# data = pd.read_csv("COC_Data2.csv")

print("Dataset shape:", data.shape)
print("\nColumn names:", data.columns.tolist())
print("\nFirst 5 rows:")
print(data.head())

# ============================================
# 2. DATA PREPARATION (same as R code)
# ============================================

# Select relevant predictors (same as R code)
predictors = [
    "wo_age", "hus_age", "wo_edu", "hus_edu", "wo_ocu", "hus_ocu",
    "religion", "wealth_index", "media", "birth_order", "intended_pregnancy",
    "level_women_involvement", "prev_pl", "distance_facility", "area", "division"
]

# Create a clean dataset for modeling
data_smote = data[["coc"] + predictors].copy()

# Handle missing values - mode imputation (like R's mode_impute function)
def mode_impute(df):
    for col in df.columns:
        if df[col].dtype in ['object', 'category'] or df[col].dtype.name == 'category':
            mode_val = df[col].mode()[0] if not df[col].mode().empty else df[col].iloc[0]
            df[col] = df[col].fillna(mode_val)
        else:
            mode_val = df[col].mode()[0] if not df[col].mode().empty else df[col].median()
            df[col] = df[col].fillna(mode_val)
    return df

data_smote = mode_impute(data_smote)

# Drop any remaining NA
data_smote = data_smote.dropna()

# Convert categorical variables to appropriate types
categorical_cols = ["wo_edu", "hus_edu", "wo_ocu", "hus_ocu", "religion", 
                    "media", "intended_pregnancy", "level_women_involvement", 
                    "prev_pl", "distance_facility", "area", "division"]

for col in categorical_cols:
    if col in data_smote.columns:
        data_smote[col] = data_smote[col].astype('category')

# Encode categorical variables for modeling
le_dict = {}
for col in categorical_cols:
    if col in data_smote.columns:
        le = LabelEncoder()
        data_smote[col] = le.fit_transform(data_smote[col].astype(str))
        le_dict[col] = le

# Ensure outcome is numeric (0/1)
if data_smote['coc'].dtype == 'object':
    data_smote['coc'] = data_smote['coc'].map({'No': 0, 'Yes': 1})
else:
    data_smote['coc'] = data_smote['coc'].astype(int)

# Check class distribution
print("\n=== Class Distribution ===")
print(data_smote['coc'].value_counts())

# ============================================
# 3. SMOTE (same as R code)
# ============================================

# Separate features and target
X = data_smote.drop('coc', axis=1)
y = data_smote['coc']

# Apply SMOTE (dup_size=0 in R means balance the classes)
smote = SMOTE(random_state=123, k_neighbors=5)
X_resampled, y_resampled = smote.fit_resample(X, y)

print("\n=== After SMOTE Class Distribution ===")
print(pd.Series(y_resampled).value_counts())

# Create new dataframe with resampled data
data_resampled = pd.DataFrame(X_resampled, columns=X.columns)
data_resampled['coc'] = y_resampled

# ============================================
# 4. BORUTA FEATURE SELECTION (same as R)
# ============================================

print("\n=== Running Boruta Feature Selection ===")

# Random Forest for Boruta
rf_boruta = RandomForestClassifier(n_jobs=-1, class_weight='balanced', random_state=123)

# Initialize Boruta
boruta = BorutaPy(
    estimator=rf_boruta,
    n_estimators='auto',
    max_iter=100,
    random_state=123,
    verbose=2
)

# Fit Boruta
X_boruta = X_resampled.values
y_boruta = y_resampled.values
boruta.fit(X_boruta, y_boruta)

# Get confirmed important features
confirmed_vars_idx = boruta.support_
confirmed_vars = X_resampled.columns[confirmed_vars_idx].tolist()
print("\nConfirmed important variables:", confirmed_vars)

# Filter data to confirmed features
if len(confirmed_vars) > 0:
    X_final = X_resampled[confirmed_vars]
else:
    X_final = X_resampled
    confirmed_vars = X_resampled.columns.tolist()

y_final = y_resampled

# ============================================
# 5. TRAIN-TEST SPLIT (80-20 stratified)
# ============================================

X_train, X_test, y_train, y_test = train_test_split(
    X_final, y_final, test_size=0.2, random_state=123, stratify=y_final
)

print(f"\nTraining set size: {X_train.shape}")
print(f"Test set size: {X_test.shape}")
print(f"Training set class distribution: \n{pd.Series(y_train).value_counts()}")

# For models that need scaling (SVM, KNN, Neural Network)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ============================================
# 6. MODEL DEFINITION AND HYPERPARAMETER TUNING
# ============================================

# 5-fold cross-validation setup
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=123)

# Dictionary to store all models
models = {}

# -------------------------------------------------------------------
# 6.1 Random Forest (same as R code: mtry = 2,4,6,8,10)
# -------------------------------------------------------------------
print("\n=== Training Random Forest ===")
rf_param_grid = {
    'max_features': [2, 4, 6, 8, 10],
    'n_estimators': [100, 200, 500],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10]
}
rf_grid = GridSearchCV(
    RandomForestClassifier(random_state=123, n_jobs=-1),
    rf_param_grid, cv=cv, scoring='roc_auc', n_jobs=-1, verbose=0
)
rf_grid.fit(X_train, y_train)
models['RandomForest'] = rf_grid.best_estimator_
print(f"Best RF params: {rf_grid.best_params_}")
print(f"Best RF CV AUC: {rf_grid.best_score_:.4f}")

# -------------------------------------------------------------------
# 6.2 Decision Tree (same as R: cp = seq(0.01, 0.5, 0.01))
# -------------------------------------------------------------------
print("\n=== Training Decision Tree ===")
dt_param_grid = {
    'ccp_alpha': np.arange(0.01, 0.51, 0.01),
    'max_depth': [5, 10, 15, 20, None],
    'min_samples_split': [2, 5, 10]
}
dt_grid = GridSearchCV(
    DecisionTreeClassifier(random_state=123),
    dt_param_grid, cv=cv, scoring='roc_auc', n_jobs=-1, verbose=0
)
dt_grid.fit(X_train, y_train)
models['DecisionTree'] = dt_grid.best_estimator_
print(f"Best DT params: {dt_grid.best_params_}")
print(f"Best DT CV AUC: {dt_grid.best_score_:.4f}")

# -------------------------------------------------------------------
# 6.3 Logistic Regression (same as R: glm)
# -------------------------------------------------------------------
print("\n=== Training Logistic Regression ===")
lr_param_grid = {
    'C': [0.001, 0.01, 0.1, 1, 10, 100],
    'penalty': ['l2'],
    'solver': ['lbfgs']
}
lr_grid = GridSearchCV(
    LogisticRegression(random_state=123, max_iter=1000),
    lr_param_grid, cv=cv, scoring='roc_auc', n_jobs=-1, verbose=0
)
lr_grid.fit(X_train_scaled, y_train)  # Scaled for better convergence
models['LogisticRegression'] = lr_grid.best_estimator_
print(f"Best LR params: {lr_grid.best_params_}")
print(f"Best LR CV AUC: {lr_grid.best_score_:.4f}")

# -------------------------------------------------------------------
# 6.4 K-Nearest Neighbors (same as R: k = seq(3,15,2))
# -------------------------------------------------------------------
print("\n=== Training KNN ===")
knn_param_grid = {
    'n_neighbors': list(range(3, 16, 2)),
    'weights': ['uniform', 'distance'],
    'metric': ['euclidean', 'manhattan']
}
knn_grid = GridSearchCV(
    KNeighborsClassifier(),
    knn_param_grid, cv=cv, scoring='roc_auc', n_jobs=-1, verbose=0
)
knn_grid.fit(X_train_scaled, y_train)
models['KNN'] = knn_grid.best_estimator_
print(f"Best KNN params: {knn_grid.best_params_}")
print(f"Best KNN CV AUC: {knn_grid.best_score_:.4f}")

# -------------------------------------------------------------------
# 6.5 SVM with RBF Kernel (same as R: svmRadial)
# -------------------------------------------------------------------
print("\n=== Training SVM ===")
svm_param_grid = {
    'C': [0.25, 0.5, 1, 2],
    'gamma': [0.25, 0.5, 1, 2],
    'kernel': ['rbf']
}
svm_grid = GridSearchCV(
    SVC(probability=True, random_state=123),
    svm_param_grid, cv=cv, scoring='roc_auc', n_jobs=-1, verbose=0
)
svm_grid.fit(X_train_scaled, y_train)
models['SVM'] = svm_grid.best_estimator_
print(f"Best SVM params: {svm_grid.best_params_}")
print(f"Best SVM CV AUC: {svm_grid.best_score_:.4f}")

# -------------------------------------------------------------------
# 6.6 XGBoost (same as R: nrounds=50,100; max_depth=3,6; eta=0.01,0.1)
# -------------------------------------------------------------------
print("\n=== Training XGBoost ===")
xgb_param_grid = {
    'n_estimators': [50, 100],
    'max_depth': [3, 6],
    'learning_rate': [0.01, 0.1],
    'subsample': [0.8, 1.0],
    'colsample_bytree': [0.8, 1.0]
}
xgb_grid = GridSearchCV(
    XGBClassifier(random_state=123, use_label_encoder=False, eval_metric='logloss'),
    xgb_param_grid, cv=cv, scoring='roc_auc', n_jobs=-1, verbose=0
)
xgb_grid.fit(X_train, y_train)
models['XGBoost'] = xgb_grid.best_estimator_
print(f"Best XGBoost params: {xgb_grid.best_params_}")
print(f"Best XGBoost CV AUC: {xgb_grid.best_score_:.4f}")

# -------------------------------------------------------------------
# 6.7 Neural Network (same as R: size=3,5,7; decay=0.01,0.1)
# -------------------------------------------------------------------
print("\n=== Training Neural Network ===")
nn_param_grid = {
    'hidden_layer_sizes': [(3,), (5,), (7,), (10,)],
    'alpha': [0.01, 0.1, 0.001],
    'learning_rate_init': [0.001, 0.01],
    'max_iter': [200]
}
nn_grid = GridSearchCV(
    MLPClassifier(random_state=123, early_stopping=True),
    nn_param_grid, cv=cv, scoring='roc_auc', n_jobs=-1, verbose=0
)
nn_grid.fit(X_train_scaled, y_train)
models['NeuralNet'] = nn_grid.best_estimator_
print(f"Best NN params: {nn_grid.best_params_}")
print(f"Best NN CV AUC: {nn_grid.best_score_:.4f}")

# ============================================
# 7. MODEL EVALUATION FUNCTION (same as R)
# ============================================

def evaluate_model(model, X_test, y_test, model_name, use_scaled=False):
    """
    Evaluate model and return metrics similar to R's evaluate_model function
    """
    if use_scaled:
        X_test_eval = X_test_scaled
    else:
        X_test_eval = X_test
    
    # Predictions
    y_pred = model.predict(X_test_eval)
    
    # Probability predictions for positive class (1)
    if hasattr(model, "predict_proba"):
        y_prob = model.predict_proba(X_test_eval)[:, 1]
    else:
        y_prob = model.decision_function(X_test_eval)
        y_prob = (y_prob - y_prob.min()) / (y_prob.max() - y_prob.min())
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, zero_division=0)
    recall = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    auc = roc_auc_score(y_test, y_prob)
    
    return {
        'Model': model_name,
        'Accuracy': accuracy,
        'Precision': precision,
        'Recall': recall,
        'F1': f1,
        'AUC': auc
    }

# Evaluate all models (keeping track of which need scaled data)
evaluation_results = []

# Models that need scaled data
scaled_models = ['LogisticRegression', 'KNN', 'SVM', 'NeuralNet']

for name, model in models.items():
    use_scaled = name in scaled_models
    results = evaluate_model(model, X_test, y_test, name, use_scaled)
    evaluation_results.append(results)

# Create results dataframe
results_df = pd.DataFrame(evaluation_results)
print("\n" + "="*60)
print("=== MODEL PERFORMANCE COMPARISON ===")
print("="*60)
print(results_df.to_string(index=False))

# ============================================
# 8. SAVE RESULTS TABLE (like R output)
# ============================================

print("\n" + "="*60)
print("=== DETAILED RESULTS TABLE ===")
print("="*60)
print(f"{'Model':<20} {'Accuracy':<10} {'Precision':<10} {'Recall':<10} {'F1-Score':<10} {'AUC':<10}")
print("-"*70)
for _, row in results_df.iterrows():
    print(f"{row['Model']:<20} {row['Accuracy']:<10.3f} {row['Precision']:<10.3f} {row['Recall']:<10.3f} {row['F1']:<10.3f} {row['AUC']:<10.3f}")

# ============================================
# 9. ROC CURVES (same as R)
# ============================================

plt.figure(figsize=(10, 8))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

for i, (name, model) in enumerate(models.items()):
    use_scaled = name in scaled_models
    if use_scaled:
        X_eval = X_test_scaled
    else:
        X_eval = X_test
    
    if hasattr(model, "predict_proba"):
        y_prob = model.predict_proba(X_eval)[:, 1]
    else:
        y_prob = model.decision_function(X_eval)
        y_prob = (y_prob - y_prob.min()) / (y_prob.max() - y_prob.min())
    
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    auc = results_df[results_df['Model'] == name]['AUC'].values[0]
    plt.plot(fpr, tpr, color=colors[i], lw=2, label=f'{name} (AUC = {auc:.3f})')

plt.plot([0, 1], [0, 1], 'k--', lw=2, label='Random Chance')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('1 - Specificity (False Positive Rate)', fontsize=12)
plt.ylabel('Sensitivity (True Positive Rate)', fontsize=12)
plt.title('ROC Curves for All Models', fontsize=14, fontweight='bold')
plt.legend(loc='lower right', fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('ROC_curve_python.png', dpi=300, bbox_inches='tight')
plt.show()
print("\nROC curve saved as 'ROC_curve_python.png'")

# ============================================
# 10. FEATURE IMPORTANCE FROM RF (same as R)
# ============================================

# Get the best Random Forest model
rf_best = models['RandomForest']

if hasattr(rf_best, 'feature_importances_'):
    feature_importance = pd.DataFrame({
        'Variable': confirmed_vars,
        'Overall': rf_best.feature_importances_
    })
    feature_importance = feature_importance.sort_values('Overall', ascending=True)
    
    plt.figure(figsize=(10, 7))
    bars = plt.barh(feature_importance['Variable'], feature_importance['Overall'], color='#00A087')
    plt.xlabel('Importance (Scaled)', fontsize=12)
    plt.ylabel('Predictor', fontsize=12)
    plt.title('Feature Importances Based on Random Forest', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('varimp_RF_python.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("\nFeature importance plot saved as 'varimp_RF_python.png'")
    print("\nFeature Importance Values:")
    print(feature_importance.sort_values('Overall', ascending=False).to_string(index=False))

# ============================================
# 11. SHAP ANALYSIS (same as R)
# ============================================

print("\n=== Running SHAP Analysis ===")

# Use the best Random Forest model for SHAP
shap_model = models['RandomForest']

# Create a SHAP explainer
explainer = shap.TreeExplainer(shap_model)

# Sample a subset for faster computation (optional)
X_sample = X_test.sample(min(500, len(X_test)), random_state=123)
shap_values = explainer.shap_values(X_sample)

# For binary classification, shap_values is a list [SHAP_for_class0, SHAP_for_class1]
# We want SHAP for class 1 (positive class)
if isinstance(shap_values, list):
    shap_values_class1 = shap_values[1]
else:
    shap_values_class1 = shap_values

# Mean signed SHAP values
mean_signed_shap = np.mean(shap_values_class1, axis=0)
print("\nMean signed SHAP values:")
for var, val in zip(confirmed_vars, mean_signed_shap):
    print(f"  {var}: {val:.6f}")

# SHAP Summary Plot (like R's ggplot with geom_jitter)
plt.figure(figsize=(12, 8))
shap.summary_plot(shap_values_class1, X_sample, feature_names=confirmed_vars, show=False)
plt.tight_layout()
plt.savefig('shap_plot_python.png', dpi=300, bbox_inches='tight')
plt.show()
print("\nSHAP plot saved as 'shap_plot_python.png'")

# Alternative: SHAP bar plot (mean absolute SHAP)
plt.figure(figsize=(10, 8))
shap.summary_plot(shap_values_class1, X_sample, feature_names=confirmed_vars, plot_type="bar", show=False)
plt.tight_layout()
plt.savefig('shap_barplot_python.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================
# 12. CALIBRATION PLOT (same as R)
# ============================================

# Get predictions from Random Forest
y_prob_rf = rf_best.predict_proba(X_test)[:, 1]

# Create calibration plot
def calibration_plot(y_true, y_prob, n_bins=10):
    # Create bins
    bins = np.percentile(y_prob, np.linspace(0, 100, n_bins+1))
    bin_indices = np.digitize(y_prob, bins) - 1
    bin_indices = np.clip(bin_indices, 0, n_bins-1)
    
    # Calculate mean predicted and observed proportion per bin
    calib_data = []
    for i in range(n_bins):
        mask = bin_indices == i
        if np.sum(mask) > 0:
            mean_pred = np.mean(y_prob[mask])
            obs_prop = np.mean(y_true[mask])
            bin_size = np.sum(mask)
            calib_data.append({
                'Mean_Predicted': mean_pred,
                'Observed_Proportion': obs_prop,
                'n': bin_size
            })
    
    calib_df = pd.DataFrame(calib_data)
    return calib_df

calib_df = calibration_plot(y_test, y_prob_rf)

plt.figure(figsize=(10, 7))
scatter = plt.scatter(calib_df['Mean_Predicted'], calib_df['Observed_Proportion'], 
                      s=calib_df['n']/calib_df['n'].max()*300, c='#1f77b4', alpha=0.8)
plt.plot(calib_df['Mean_Predicted'], calib_df['Observed_Proportion'], 
         color='#1f77b4', linewidth=2, marker='o')
plt.plot([0, 1], [0, 1], 'k--', linewidth=2, label='Perfect Calibration')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.xlabel('Mean Predicted Probability', fontsize=12)
plt.ylabel('Observed Proportion', fontsize=12)
plt.title('Calibration Plot for Random Forest (CoC Prediction)', fontsize=14, fontweight='bold')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('calibration_plot_python.png', dpi=300, bbox_inches='tight')
plt.show()
print("\nCalibration plot saved as 'calibration_plot_python.png'")

# ============================================
# 13. CONFUSION MATRIX FOR BEST MODEL
# ============================================

# Show confusion matrix for Random Forest
y_pred_rf = rf_best.predict(X_test)

plt.figure(figsize=(6, 5))
cm = confusion_matrix(y_test, y_pred_rf)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['No CoC', 'Completed CoC'])
disp.plot(cmap='Blues', values_format='d')
plt.title('Confusion Matrix - Random Forest', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('confusion_matrix_python.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n" + "="*60)
print("=== BEST HYPERPARAMETERS FROM ALL MODELS ===")
print("="*60)
for name, model in models.items():
    print(f"\n{name}:")
    print(f"  {model.get_params()}")

print("\n" + "="*60)
print("=== ANALYSIS COMPLETE ===")
print("="*60)
print("Generated files:")
print("  - ROC_curve_python.png")
print("  - varimp_RF_python.png")
print("  - shap_plot_python.png")
print("  - shap_barplot_python.png")
print("  - calibration_plot_python.png")
print("  - confusion_matrix_python.png")