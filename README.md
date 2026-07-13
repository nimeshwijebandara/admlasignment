# People's Leasing & Finance PLC - Credit Risk Prediction System

## Project Overview

This project is a Machine Learning-based Credit Risk Prediction System developed for People's Leasing & Finance PLC. The system predicts whether a loan applicant is classified as a **Low Risk** or **High Risk** customer based on demographic and financial information.

The project compares three machine learning models:

- Logistic Regression
- Random Forest
- XGBoost

The final selected model is deployed as a web application using Streamlit.

---

## Objectives

- Predict customer credit risk.
- Improve loan approval decisions.
- Reduce loan default risk.
- Support faster and data-driven decision-making.

---

## Features

- Customer Information Input
- Automatic Debt-to-Income Ratio Calculation
- Credit Risk Prediction
- Prediction Probability
- Interactive Streamlit Web Interface

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| Scikit-learn | Machine Learning |
| XGBoost | Classification Model |
| Streamlit | Web Application |
| Joblib | Model Serialization |
| Matplotlib | Data Visualization |

---

## Dataset Features

- Age
- Gender
- Marital Status
- Employment Type
- Monthly Income
- Loan Amount
- Loan Term
- Existing Liabilities
- Debt-to-Income Ratio
- Credit History Length

Target Variable

- Risk
    - Low Risk
    - High Risk

---

## Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Data Transformation
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Model Selection
9. Streamlit Deployment

---

## Model Evaluation Metrics

The following metrics were used:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Confusion Matrix
- Cross Validation

---

## Project Structure

```
Credit_Risk_Project/

│── app.py
│── credit_risk_model.pkl
│── credit_risk_dataset.csv
│── notebook.ipynb
│── requirements.txt
│── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/nimeshwijebandara/admlasignment.git
```

Go to the project folder

```bash
cd Credit_Risk_Project
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## Example Prediction

Input

- Age : 35
- Gender : Male
- Employment Type : Permanent
- Monthly Income : Rs.150,000
- Loan Amount : Rs.2,500,000
- Existing Liabilities : Rs.500,000
- Credit History Length : 10 years

Prediction

```
Low Risk Customer
```

---

## Results

| Model | Accuracy | AUC |
|---------|----------|------|
| Logistic Regression | 82% | 0.84 |
| Random Forest | 89% | 0.91 |
| XGBoost | 92% | 0.94 |

The XGBoost model achieved the best overall performance and was selected for deployment.

---

## Future Improvements

- Real-time database integration
- Explainable AI (SHAP/LIME)
- Loan recommendation module
- Customer dashboard
- REST API integration
- Cloud deployment

---

## Author

**Nimesh Wijebandara**


---

## License

This project was developed for educational and research purposes only.