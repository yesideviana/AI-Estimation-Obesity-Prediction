import streamlit as st
st.title('Obesity Prediction based on Eating Habits and Physical Condition')

col1, col2 = st.columns(2)

with col1 :
    tinggi = st.text_input ('Masukkan Tinggi Anda')

with col2 :
    berat = st.text_input ('Masukkan Berat Anda')

with col1 :
    umur = st.text_input ('Masukkan Umur Anda')

with col2 :
    Aktifitas = st.text_input ('Apakah ada Aktifitas Fisik')

with col1 :
    Gaya = st.text_input ('Apakah Gaya Hidup anda Sehat')

with col2 :
    kalori = st.text_input ('Masukkan Kalori Harian Anda')

with col1 :
    obesPedigreeFunction = st.text_input ('Masukkan Obes Pedigree Function')

with col2 :
    sayur = st.text_input ('Apakah anda Mengkonsumsi Sayur')

# code untuk prediksi Obes

if st.button('Test Prediksi Obesitas'):
   obesity_prediction = obes_model.predict([[berat, tinggi, kalori, Gaya, Aktifitas, obesPedigreeFunction, umur, sayur]])

    if(obesity_prediction[0] == 1):
        obesity_diagnosis = 'Anda mengalami Obesitas'
    else:
        obesity_diagnosis = 'Anda tidak mengalami Obesitas'
st.success(obesity_diagnosis)
