import streamlit as st
import pandas as pd
import joblib

# Load model and display evaluation metrics
model = joblib.load("house_price_model.pkl")
r2_score = 0.85  # Replace with your actual test score if available

def show_prediction_page():
    st.set_page_config(page_title="🏠 House Price Estimator", layout="wide")

    st.sidebar.header("ℹ️ How to Use")
    st.sidebar.write("""
    - Fill in the house features.
    - Click on 'Predict Price' to see the estimated value.
    - Trained on Ames Housing Dataset.
    """)
    st.sidebar.markdown("----")
    st.sidebar.success("🔑 Logged in")

    st.title("🏠 House Price Estimator")
    st.subheader("Get an instant estimate based on house features!")
    
    with st.expander("📈 View Model Accuracy"):
        st.metric(label="R² Score", value=f"{r2_score * 100:.2f} %")

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

        st.markdown(f"<div style='background-color:#e0f7fa;padding:15px;border-radius:10px;font-size:22px;font-weight:bold;color:#0072C6;'>💰 Estimated Price: ₹ {int(prediction):,}</div>", unsafe_allow_html=True)
