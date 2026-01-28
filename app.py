import streamlit as st
import numpy as np

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Smart Loan Approval System – Stacking Model",
    page_icon="🎯",
    layout="wide"
)

# -------------------- TITLE & DESCRIPTION --------------------
st.title("🎯 Smart Loan Approval System – Stacking Model")
st.markdown(
    """
    **This system uses a Stacking Ensemble Machine Learning model to predict whether a loan will be approved
    by combining multiple ML models for better decision making.**
    """
)

# -------------------- SIDEBAR INPUTS --------------------
# -------------------- SIDEBAR INPUTS --------------------
st.sidebar.header("📝 Applicant Details")

applicant_income = st.sidebar.number_input(
    "Applicant Income",
    min_value=0,
    max_value=100000,
    value=3000,
    step=500
)

coapplicant_income = st.sidebar.number_input(
    "Co-Applicant Income",
    min_value=0,
    max_value=100000,
    value=1500,
    step=500
)

loan_amount = st.sidebar.number_input(
    "Loan Amount",
    min_value=0,
    max_value=1000,
    value=200,
    step=50
)

loan_term = st.sidebar.number_input(
    "Loan Amount Term (Months)",
    min_value=12,
    max_value=480,
    value=360,
    step=12
)

credit_history = st.sidebar.radio(
    "Credit History", ["Yes", "No"], index=0
)

employment_status = st.sidebar.selectbox(
    "Employment Status", ["Salaried", "Self-Employed"]
)

property_area = st.sidebar.selectbox(
    "Property Area", ["Urban", "Semi-Urban", "Rural"]
)

credit_history_val = 1 if credit_history == "Yes" else 0


# -------------------- MODEL ARCHITECTURE DISPLAY --------------------
st.subheader("🧠 Stacking Model Architecture")

st.markdown(
    """
    ### 🔹 Base Models Used
    - Logistic Regression  
    - Decision Tree  
    - Random Forest  

    ### 🔹 Meta Model Used
    - Logistic Regression  

    📌 *Base models first make individual predictions.  
    These predictions are then combined and passed to the meta-model
    for the final decision.*
    """
)

# -------------------- PREDICTION BUTTON --------------------
st.subheader("🔍 Loan Eligibility Prediction")

if st.button("🔘 Check Loan Eligibility (Stacking Model)"):

    # ----------- BASE MODEL SIMULATED PREDICTIONS -----------
    # (Replace with real trained models if available)

    logistic_pred = 1 if applicant_income > 2500 and credit_history_val == 1 else 0
    decision_tree_pred = 1 if loan_amount < 300 and credit_history_val == 1 else 0
    random_forest_pred = 1 if applicant_income + coapplicant_income > 4000 else 0

    base_predictions = np.array([
        logistic_pred,
        decision_tree_pred,
        random_forest_pred
    ])

    # ----------- META MODEL (STACKING) -----------
    final_prediction = 1 if base_predictions.sum() >= 2 else 0
    confidence_score = int((base_predictions.sum() / 3) * 100)

    # -------------------- OUTPUT SECTION --------------------
    st.subheader("📊 Prediction Result")

    if final_prediction == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")

    # Base Model Outputs
    st.markdown("### 📊 Base Model Predictions")

    st.write(f"**Logistic Regression →** {'Approved' if logistic_pred else 'Rejected'}")
    st.write(f"**Decision Tree →** {'Approved' if decision_tree_pred else 'Rejected'}")
    st.write(f"**Random Forest →** {'Approved' if random_forest_pred else 'Rejected'}")

    # Final Decision
    st.markdown("### 🧠 Final Stacking Decision")
    st.write("**Approved**" if final_prediction else "**Rejected**")

    # Confidence Score
    st.markdown("### 📈 Confidence Score")
    st.progress(confidence_score / 100)
    st.write(f"**{confidence_score}% confidence**")

    # -------------------- BUSINESS EXPLANATION --------------------
    st.subheader("📌 Business Explanation")

    if final_prediction == 1:
        st.markdown(
            """
            Based on the applicant’s income, credit history, and combined predictions
            from multiple machine learning models, the applicant is **likely to repay the loan**.

            Therefore, the **stacking model predicts loan approval**.
            """
        )
    else:
        st.markdown(
            """
            Based on income level, credit history, and combined predictions
            from multiple machine learning models, the applicant is **unlikely to repay the loan**.

            Therefore, the **stacking model predicts loan rejection**.
            """
        )

# -------------------- FOOTER --------------------
st.markdown("---")
st.markdown("🎓 *Educational ML Project – Stacking Ensemble Model for Loan Approval*")
