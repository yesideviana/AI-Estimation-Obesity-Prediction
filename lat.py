import streamlit as st
st.title('Obesity Prediction based on Eating Habits and Physical Condition')

col1, col2 = st.columns(2)
with col1 :
Berat = st.number("Masukkan Berat Badan", 0)

with col2 :
Tinggi = st.number("Masukkan Berat Badan",0 )

with col1 :
kalori = st.number ("Masukkan nilai kalori harian",0)

with col2 :
fisik = st.number ("Masukkan nilai Aktifitas Fisik",0)

   with col1 :
    Insulin = st.number ('Masukkan nilai Insulin',0)

with col2 :
    BMI = st.number ('Apakah ada Aktifitas Fisik',0)

with col1 :
    ObesPedigreeFunction = st.number ('Apakah Gaya Hidup Anda',0)

with col2 :
    Age = st.number ('input nilai Age',0)

# code untuk prediksi Obes

if st.button('Test Prediksi Obesitas'):
   obes_prediction = obes_model.predict([[Berat, tinggi, kalori, fisik, Insulin, BMI, ObesPedigreeFunction, Age]])

    if(diab_prediction[0] == 1):
        obes_diagnosis = 'Anda mengalami Obess'
    else:
        obes_diagnosis = 'Anda tidak mengalami Obes'
st.success(obes_diagnosis)
