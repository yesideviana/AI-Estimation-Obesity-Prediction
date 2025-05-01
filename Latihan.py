import streamlit as st
st.title('Obesity Prediction based on Eating Habits and Physical Condition')
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load dataset (contoh dataset, bisa diganti dengan dataset nyata)
# Dataset harus berisi fitur seperti: kebiasaan makan, aktivitas fisik, usia, dll.
# dan label tingkat obesitas (misal: Normal, Overweight, Obese)
data = {
    'kalori_harian': [2500, 1800, 3000, 2200, 2800, 2000, 3500],
    'fast_food': [3, 1, 5, 2, 4, 1, 6],  # frekuensi per minggu
    'sayur': [4, 6, 2, 5, 3, 7, 1],     # porsi per hari
    'olahraga': [3, 5, 1, 4, 2, 6, 0],  # jam per minggu
    'usia': [25, 30, 40, 35, 28, 45, 50],
    'tinggi': [170, 165, 175, 168, 180, 160, 172],
    'berat': [70, 60, 90, 75, 85, 55, 100],
    'obesitas': [1, 0, 2, 1, 2, 0, 2]  # 0=Normal, 1=Overweight, 2=Obese
}

df = pd.DataFrame(data)

# Hitung BMI dan tambahkan sebagai fitur
df['bmi'] = df['berat'] / ((df['tinggi']/100) ** 2)

# Pisahkan fitur dan target
X = df.drop(['obesitas', 'berat', 'tinggi'], axis=1)
y = df['obesitas']

