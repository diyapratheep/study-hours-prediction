import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('model.pkl')

# GUI for data input
st.title('Prediction App')
st.write('Enter your data below:')

hours = st.number_input('Hours Studied', min_value=0)
input_data = pd.DataFrame({'Hours': [hours]})

if st.button('Predict'):
    prediction = model.predict(input_data)
    st.write(f'Predicted Score: {prediction[0][0]:.4f}')
