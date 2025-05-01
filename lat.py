import streamlit as st
st.title('Obesity Prediction based on Eating Habits and Physical Condition')
tinggi = st.number_input("Masukkan Tinggi Badan", 0)
berat = st.number_input("Masukkan Berat Badan", 0)
kalori = st.number_input("Apakah mengkonsumsi makanan tinggi Kalori", 0)
sayur = st.bar_chart("Apakah ada sayuran",)
frekuensi = st.set_option("Masukkan Frekuensi Makan Berat", 0)
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Berat, tinggi, kalori, fisik, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diab_prediction[0] == 1):
        diab_diagnosis = 'Anda mengalami Obess'
    else:
        diab_diagnosis = 'Anda tidak mengalami Obes'
st.success(diab_diagnosis)
