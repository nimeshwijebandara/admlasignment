import streamlit as st
import pandas as pd
import joblib


model = joblib.load("credit_risk_model.pkl")

st.set_page_config(
    page_title="Credit Risk Prediction System",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 People's Finance PLC")
st.subheader("Credit Risk Prediction System")
st.write("Enter customer details and click **Predict Risk**.")



age = st.number_input(
    "Age",
    min_value=18,
    max_value=80,
    value=30
)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

marital = st.selectbox(
    "Marital Status",
    ["Single", "Married"]
)

emp = st.selectbox(
    "Employment Type",
    ["Permanent", "Contract", "Self-Employed"]
)

income = st.number_input(
    "Monthly Income",
    min_value=1.0,
    value=50000.0
)

loan = st.number_input(
    "Loan Amount",
    min_value=0.0,
    value=500000.0
)

term = st.selectbox(
    "Loan Term",
    [12,24,36,48,60,72,84]
)

liability = st.number_input(
    "Existing Liabilities",
    min_value=0.0,
    value=0.0
)

history = st.number_input(
    "Credit History Length",
    min_value=0,
    max_value=40,
    value=5
)


dti = liability / income if income > 0 else 0


gender_map = {
    "Female": 0,
    "Male": 1
}

marital_map = {
    "Single": 0,
    "Married": 1
}

emp_map = {
    "Permanent": 0,
    "Contract": 1,
    "Self-Employed": 2
}

gender = gender_map[gender]
marital = marital_map[marital]
emp = emp_map[emp]

if st.button("Predict Risk"):

    input_data = pd.DataFrame([[
        age,
        gender,
        marital,
        emp,
        income,
        loan,
        term,
        liability,
        dti,
        history
    ]], columns=[
        "Age",
        "Gender",
        "Marital status",
        "EMP type",
        "Montly income",
        "Loan Amount",
        "Loan Tearm",
        "Exsisting Liabilities",
        "Debt-to-Income Ratio",
        "Credit History Length"
    ])

    prediction = model.predict(input_data)

    probability = model.predict_proba(input_data)

    low_risk = probability[0][0]
    high_risk = probability[0][1]

    st.divider()

    st.subheader("Prediction Result")

    if prediction[0] == 0:
        st.success("🟢 Low Risk Customer")
    else:
        st.error("🔴 High Risk Customer")

    st.subheader("Prediction Probability")

    st.progress(float(low_risk))

    col1, col2 = st.columns(2)

    col1.metric(
        "Low Risk",
        f"{low_risk*100:.2f}%"
    )

    col2.metric(
        "High Risk",
        f"{high_risk*100:.2f}%"
    )

    st.subheader("Customer Information")

    st.dataframe(
        input_data,
        use_container_width=True
    )