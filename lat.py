import streamlit as st
st.title('Obesity Prediction based on Eating Habits and Physical Condition')
background : rgb
col1, col2 = st.columns(2)
tinggi = st.number_input("Masukkan Tinggi Badan", 0)
berat = st.number_input("Masukkan Berat Badan", 0)

with col1 :
    Berat = st.text_input ('input nilai berat badan')

with col2 :
    tinggi = st.text_input ('input nilai tinggi badan')

with col1 :
    kalori = st.text_input ('input nilai kalori harian')

with col2 :
    fisik = st.text_input ('input nilai Aktifitas Fisik')

with col1 :
    Insulin = st.text_input ('input nilai Insulin')

with col2 :
    BMI = st.text_input ('input nilai BMI')

with col1 :
    DiabetesPedigreeFunction = st.text_input ('input nilai Diabetes Pedigree Function')

with col2 :
    Age = st.text_input ('input nilai Age')

# code untuk prediksi Obes


# membuat tombol untuk prediksi
if st.button('Test Prediksi Obesitas'):
    diab_prediction = diabetes_model.predict([[Berat, tinggi, kalori, fisik, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diab_prediction[0] == 1):
        diab_diagnosis = 'Anda mengalami Obess'
    else:
        diab_diagnosis = 'Anda tidak mengalami Obes'
st.success(diab_diagnosis)
