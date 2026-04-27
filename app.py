import streamlit as st
import pandas as pd
import numpy as np
import pickle

# load the model
model = pickle.load(open('gb_model.pkl', 'rb'))

# title for app
st.title('Insurance Price Prediction App')

# define inputs
age = st.number_input('Age', min_value=1, max_value=100, value=25)
gender = st.selectbox('Gender', ('male', 'female'))
bmi = st.number_input('BMI', min_value=10.0, max_value=80.0, value=30.0)
smoker = st.selectbox('Smoker', ('yes', 'no'))
children = st.number_input('Children', min_value=0, max_value=10, value=2)
region = st.selectbox('Region', ('southwest', 'southeast', 'northwest', 'northeast'))

# encoding
Smoker = 1 if smoker == 'yes' else 0

sex_male = 1 if gender == 'male' else 0
sex_female = 1 if gender == 'female' else 0

region_dict = {
    'southwest': 0,
    'northwest': 1,
    'northeast': 2,
    'southeast': 3
}
Region = region_dict[region]

# create dataframe
input_data = pd.DataFrame({
    'age': [age],
    'bmi': [bmi],
    'children': [children],
    'Region': [Region],
    'Smoker': [Smoker],
    'sex_female': [sex_female],
    'sex_male': [sex_male]
})

# prediction
if st.button('Predict'):
    prediction = model.predict(input_data)
    
    # if model trained on log values, use exp
    output = round(np.exp(prediction[0]), 2)
    
    st.success(f'Predicted Insurance Charges: ${output}')