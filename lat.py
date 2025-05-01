import streamlit as st
st.title('Obesity Prediction based on Eating Habits and Physical Condition')
tinggi = st.number_input("Masukkan Tinggi Badan", 0)
berat = st.number_input("Masukkan Berat Badan", 0)
hitung = st.button('Hitung IMT')