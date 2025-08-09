# streamlit_app.py
import streamlit as st
import pandas as pd
import joblib

# Load the trained pipeline
model = joblib.load('house_price_model.pkl')

# Page configuration
st.set_page_config(page_title="🏠 House Price Estimator", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
            padding: 20px;
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            padding: 0.5rem 1rem;
        }
        .prediction {
            background-color: #e8f0fe;
            padding: 20px;
            border-radius: 10px;
            font-size: 24px;
            font-weight: bold;
            color: #0f5132;
            border-left: 5px solid #0072C6;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("ℹ️ How to Use")
st.sidebar.write("""
- Fill in the house features.
- Click on 'Predict Price' to see the estimated value.
- The model is trained on Ames Housing Dataset.
""")
st.sidebar.markdown("---")
st.sidebar.write("👩‍🎓 Project by: **Arpita Dhiman**")

# Title
st.title("🏠 House Price Estimator")
st.subheader("Get an instant estimate based on house features!")

# Input Form
with st.form("prediction_form"):
    st.markdown("### 📋 Fill in House Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        OverallQual = st.slider("🏗️ Overall Quality (1–10)", 1, 10, 5)
        GrLivArea = st.number_input("📏 Living Area (sq ft)", 300, 5000, 1500)
        GarageCars = st.slider("🚗 Garage Capacity (Cars)", 0, 5, 2)
        TotalBsmtSF = st.number_input("🏚️ Basement Area (sq ft)", 0, 3000, 800)
    
    with col2:
        FullBath = st.slider("🛁 Full Bathrooms", 0, 4, 2)
        YearBuilt = st.number_input("📅 Year Built", 1900, 2024, 2005)
        Neighborhood = st.selectbox("🏘️ Neighborhood", [
            'CollgCr', 'Veenker', 'Crawfor', 'NoRidge', 'Mitchel',
            'Somerst', 'NWAmes', 'OldTown', 'BrkSide', 'Sawyer',
            'NAmes', 'SawyerW', 'IDOTRR', 'MeadowV', 'Edwards',
            'Timber', 'Gilbert', 'StoneBr', 'ClearCr', 'NPkVill',
            'Blmngtn', 'BrDale', 'SWISU', 'Blueste'
        ])
        BldgType = st.selectbox("🏗️ Building Type", ['1Fam', '2fmCon', 'Duplex', 'TwnhsE', 'Twnhs'])
    
    submit = st.form_submit_button("🔍 Predict Price")

# Prediction Result
if submit:
    input_df = pd.DataFrame([{
        'OverallQual': OverallQual,
        'GrLivArea': GrLivArea,
        'GarageCars': GarageCars,
        'TotalBsmtSF': TotalBsmtSF,
        'FullBath': FullBath,
        'YearBuilt': YearBuilt,
        'Neighborhood': Neighborhood,
        'BldgType': BldgType
    }])
    
    prediction = model.predict(input_df)[0]
    
    st.markdown(f"<div class='prediction'>💰 Estimated House Price: <span style='color:#0072C6'>₹ {int(prediction):,}</span></div>", unsafe_allow_html=True)
