import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression, Ridge, Lasso, LogisticRegression
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score, classification_report, confusion_matrix, roc_curve
import matplotlib.pyplot as plt

# Sample dataset (simulated)
data = pd.DataFrame({
    'feature1': np.random.rand(100),
    'feature2': np.random.randint(0, 10, 100),
    'category': np.random.choice(['A', 'B', 'C'], 100),
    'target_class': np.random.choice([0, 1], 100),
    'target_reg': np.random.rand(100) * 10
})

# Splitting data
X = data[['feature1', 'feature2', 'category']]
y_class = data['target_class']
y_reg = data['target_reg']
X_train, X_test, y_class_train, y_class_test = train_test_split(X, y_class, test_size=0.2, random_state=42)
X_train_reg, X_test_reg, y_reg_train, y_reg_test = train_test_split(X, y_reg, test_size=0.2, random_state=42)

# Preprocessing: One-hot encoding & scaling
num_features = ['feature1', 'feature2']
cat_features = ['category']

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), num_features),
    ('cat', OneHotEncoder(handle_unknown='ignore'), cat_features)
])

# Classification Model: KNN
knn_pipeline = Pipeline([
    ('preprocess', preprocessor),
    ('knn', KNeighborsClassifier(n_neighbors=5))
])
knn_pipeline.fit(X_train, y_class_train)
y_pred_class = knn_pipeline.predict(X_test)
print("KNN Accuracy:", accuracy_score(y_class_test, y_pred_class))

# Regression Model: Linear Regression
reg_pipeline = Pipeline([
    ('preprocess', preprocessor),
    ('linreg', LinearRegression())
])
reg_pipeline.fit(X_train_reg, y_reg_train)
y_pred_reg = reg_pipeline.predict(X_test_reg)
print("Linear Regression R²:", r2_score(y_reg_test, y_pred_reg))
print("RMSE:", np.sqrt(mean_squared_error(y_reg_test, y_pred_reg)))

# Regularized Regression: Ridge & Lasso
ridge_pipeline = Pipeline([
    ('preprocess', preprocessor),
    ('ridge', Ridge(alpha=1.0))
])
lasso_pipeline = Pipeline([
    ('preprocess', preprocessor),
    ('lasso', Lasso(alpha=0.1))
])

ridge_pipeline.fit(X_train_reg, y_reg_train)
lasso_pipeline.fit(X_train_reg, y_reg_train)
print("Ridge R²:", ridge_pipeline.score(X_test_reg, y_reg_test))
print("Lasso R²:", lasso_pipeline.score(X_test_reg, y_reg_test))

# Logistic Regression & ROC Curve
y_probs = knn_pipeline.predict_proba(X_test)[:, 1]
fpr, tpr, _ = roc_curve(y_class_test, y_probs)
plt.plot(fpr, tpr, label="ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()

# Hyperparameter Tuning: GridSearchCV
param_grid = {'knn__n_neighbors': [3, 5, 7, 9]}
grid_search = GridSearchCV(knn_pipeline, param_grid, cv=5)
grid_search.fit(X_train, y_class_train)
print("Best K for KNN:", grid_search.best_params_)
