import streamlit as st
import pandas as pd
import joblib


# model of fraude detection
model = joblib.load("fraud_detection_pipeline.pkl")


st.title("Fraud Detection Prediction App")

st.markdown("Please enter the transaction details and use the predict button")

st.divider()

# Form

# the type of transaction
transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "CASH_IN", "DEBIT"])

# the amount
amount = st.number_input("Amount", min_value = 0.0, max_value = 1000.0)

# oldbalanceOrg
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value = 0.0, max_value = 10000.0)

# newbalanceOrig
newbalanceOrig = st.number_input("New Balance (Sender)", min_value = 0.0, max_value = 10000.0)

# oldbalanceDest
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value = 0.0, max_value = 10000.0)

# newbalanceDest
newbalanceDest = st.number_input("New Balance (Receiver)", min_value = 0.0, max_value = 10000.0)


if st.button("Predict"):
    input_data = pd.DataFrame([
        {
            "type": transaction_type,
            "amount": amount,
            "oldbalanceOrg": oldbalanceOrg,
            "newbalanceOrig": newbalanceOrig,
            "oldbalanceDest": oldbalanceDest,
            "newbalanceDest": newbalanceDest
        }
    ])

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction: '{int(prediction)}'")

    if prediction == 1:
        st.error("This transaction can be fraud")
    else:
        st.success("This transaction looks like it is not a fraud")