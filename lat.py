import streamlit as st
st.title('Obesity Prediction based on Eating Habits and Physical Condition')

col1, col2 = st.columns(2)
with col1 :
Berat = st.number("Masukkan Berat Badan", )
with col2 :
Tinggi = st.number("Masukkan Berat Badan", )
with col1 :
kalori = st.number ("input nilai kalori harian")
with col2 :
fisik = st.number ("input nilai Aktifitas Fisik")

   with col1 :
    Insulin = st.number ('input nilai Insulin')

with col2 :
    BMI = st.number ('Apakah ada Aktifitas Fisik')

with col1 :
    ObesPedigreeFunction = st.number ('Gaya Hidup Anda')

with col2 :
    Age = st.number ('input nilai Age')

# code untuk prediksi Obes

if st.button('Test Prediksi Obesitas'):
   obes_prediction = obes_model.predict([[Berat, tinggi, kalori, fisik, Insulin, BMI, ObesPedigreeFunction, Age]])

    if(diab_prediction[0] == 1):
        obes_diagnosis = 'Anda mengalami Obess'
    else:
        obes_diagnosis = 'Anda tidak mengalami Obes'
st.success(obes_diagnosis)
