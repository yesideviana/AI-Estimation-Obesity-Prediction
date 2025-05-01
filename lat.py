import streamlit as st
st.title('Obesity Prediction based on Eating Habits and Physical Condition')

col1, col2 = st.columns(2)
with col1 :
Berat = st.text_input("Masukkan Berat Badan")
with col2 :
Tinggi = st.text_input("Masukkan Berat Badan")
with col1 :
kalori = st.text_input ("input nilai kalori harian")
with col2 :
fisik = st.text_input ("input nilai Aktifitas Fisik")

   with col1 :
    Insulin = st.text_input ('input nilai Insulin')

with col2 :
    BMI = st.text_input ('Apakah ada Aktifitas Fisik')

with col1 :
    ObesPedigreeFunction = st.text_input ('Gaya Hidup Anda')

with col2 :
    Age = st.text_input ('input nilai Age')

# code untuk prediksi Obes

if st.button('Test Prediksi Obesitas'):
   obes_prediction = obes_model.predict([[Berat, tinggi, kalori, fisik, Insulin, BMI, ObesPedigreeFunction, Age]])

    if(diab_prediction[0] == 1):
        obes_diagnosis = 'Anda mengalami Obess'
    else:
        obes_diagnosis = 'Anda tidak mengalami Obes'
st.success(obes_diagnosis)
