import streamlit as st
import pickle
import pandas as pd

churn_prediction_model = pickle.load(open('churn_prediction_model.pkl', 'rb'))


def main():
    st.header('--Bank Churn Prediction App--')
    st.subheader('Sanith Samaraweera | SE 26')
    st.text('Enter Customer Details to Predict Churn')

    credit_score = st.number_input('Credit Score', step=1)
    geography = st.selectbox('Geography (Germany:0, Spain:1, France:2 ) ', [0, 1, 2])
    gender = st.selectbox('Gender (Male: 0, Female: 1 )', [0, 1])
    age = st.number_input('Age', step=1)
    tenure = st.number_input('Tenure', step=1)
    balance = st.number_input('Balance')
    num_of_products = st.number_input('Number of Products', step=1)
    has_cr_card = st.selectbox('Has Credit Card (No: 0, Yes: 1)', [0, 1])
    is_active_member = st.selectbox('Is Active Member (No: 0, Yes: 1)', [0, 1])
    estimated_salary = st.number_input('Estimated Salary')

    input_data = pd.DataFrame({
        'CreditScore': [credit_score],
        'Geography': [geography],
        'Gender': [gender],
        'Age': [age],
        'Tenure': [tenure],
        'Balance': [balance],
        'NumOfProducts': [num_of_products],
        'HasCrCard': [has_cr_card],
        'IsActiveMember': [is_active_member],
        'EstimatedSalary': [estimated_salary]
    })

    if st.button('Predict Churn'):
        prediction = churn_prediction_model.predict(input_data)[0]
        if prediction == 1:
            st.error('Prediction:  Churned')
        else:
            st.success('Prediction:  Not Churned')

if __name__ == '__main__':
    main()