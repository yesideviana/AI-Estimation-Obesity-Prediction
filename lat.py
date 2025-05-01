import streamlit as st
st.title('Obesity Prediction based on Eating Habits and Physical Condition')
tinggi = st.number_input("Masukkan Tinggi Badan", 0)
berat = st.number_input("Masukkan Berat Badan", 0)
kalori = st.number_input("Masukkan Kalori harian", 0)
sayur = st.get_option("Yes or No,")
frekuensi = st.number_input("Masukkan Frekuensi Makan Berat", 0)
hitung = st.button('Indeks Massa Tubuh= berat/(tinggi)^2')
hitung = st.button('Prediksi Menderita Obesitas')
