import streamlit as st
st.title('Obesity Prediction based on Eating Habits and Physical Condition')

col1, col2 = st.columns(2)

with col1 :
Berat = st.number_input("Masukkan Berat Badan", 0)

with col2 :
Tinggi = st.number_input("Masukkan Berat Badan",0)

with col1 :
kalori = st.number_input("Masukkan nilai kalori harian",0)

with col2 :
fisik = st.number_input("Masukkan nilai Aktifitas Fisik",0)

   with col1 :
    Insulin = st.number_input("Masukkan nilai Insulin",0)

with col2 :
    BMI = st.number_input("Apakah ada Aktifitas Fisik",0)

with col1 :
    ObesPedigreeFunction = st.number_input("Apakah Gaya Hidup Anda",0)

with col2 :
    Umur = st.number_input("Masukkan Umur",0)

# code untuk prediksi Obes

if st.button('Test Prediksi Obesitas'):
   obes_prediction = obes_model.predict([[Berat, tinggi, kalori, fisik, Insulin, BMI, ObesPedigreeFunction, Umur]])

    if(diab_prediction[0] == 1):
        obes_diagnosis = 'Anda mengalami Obess'
    else:
        obes_diagnosis = 'Anda tidak mengalami Obes'
st.success(obes_diagnosis)
