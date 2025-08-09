# app.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
df = pd.read_csv('train.csv')

# Use only the below consistent features
features = ['OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt', 'Neighborhood', 'BldgType']
target = 'SalePrice'

X = df[features]
y = df[target]

# Define columns
numerical = ['OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt']
categorical = ['Neighborhood', 'BldgType']

# Preprocessing pipeline
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numerical),
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical)
])

# Combine preprocessor + model
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', LinearRegression())
])

# Train the pipeline
pipeline.fit(X, y)

# Save the complete pipeline
joblib.dump(pipeline, 'house_price_model.pkl')
print("✅ Model trained and saved.")
