import streamlit as st
import pandas as pd
from tensorflow.keras.models import load_model
import joblib
from predict import preprocess_data, predict_fraud

model_path = "fraud_detection_model_final.keras"  
scaler_path = "scaler.pkl"
model = load_model(model_path)
scaler = joblib.load(scaler_path)

acc_no = st.text_input("Account No", max_chars=24)
tran_date = st.text_input("Transaction Date", max_chars=10)
tran_detail = st.text_input("Transaction Details", max_chars=15)
chq_no = st.number_input("CHQ.NO.")
val_date = st.text_input("VALUE DATE", value=tran_date)
withdrawal_amt = st.number_input("WITHDRAWAL AMT")
deposit_amt = st.number_input("DEPOSIT AMT")
balance_amt = st.number_input("BALANCE AMT")

submit_button = st.button("Submit")

if submit_button:
    data = {
        'Account No': acc_no,
        'DATE': tran_date,
        'TRANSACTION DETAILS': tran_detail,
        'CHQ.NO.': chq_no,
        'VALUE DATE': val_date,
        'WITHDRAWAL AMT': withdrawal_amt,
        'DEPOSIT AMT': deposit_amt,
        'BALANCE AMT': balance_amt
    }
    
    df = pd.DataFrame([data])
    processed_data = preprocess_data(df)
    
    fraud_probability = predict_fraud(model, processed_data, scaler)
    
    df['Fraud Probability'] = fraud_probability
    
    df.to_csv("transaction_data_with_fraud_prob.csv", index=False)
    
    if any(fraud_probability == 1):
        st.error("Alert: Transaction(s) with fraud probability Found. Admin action required.")
    else:
        st.success("Transaction completed successfully! kindly check CSV file ")

if st.button("Show CSV File"):
    try:
        csv_data = pd.read_csv("transaction_data_with_fraud_prob.csv")
        st.write("CSV file contents:")
        st.write(csv_data)
     
    except FileNotFoundError:
        st.error("CSV file not found. Please submit data first.")
