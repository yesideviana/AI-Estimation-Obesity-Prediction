import streamlit as st
st.title('Obesity Prediction based on Eating Habits and Physical Condition')
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

data = {
   
    tinggi = st.number_input("Masukkan Tinggi Badan", 0)
    berat = st.number_input("Masukkan Berat Badan", 0)
    'jenis_kelamin': [0, 1, 0, 1, 1, 0],  # 0 untuk perempuan, 1 untuk laki-laki
    'pola_makan': [1, 0, 1, 0, 1, 1],  # 1 untuk buruk, 0 untuk baik
    'aktivitas_fisik': [1, 0, 1, 0, 0, 1],  # 1 untuk aktif, 0 untuk tidak aktif
    'obesitas': [0, 1, 0, 1, 1, 0]  # 0 untuk tidak obesitas, 1 untuk obesitas
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Memisahkan fitur dan label
X = df[['usia', 'tinggi_badan', 'berat_badan', 'jenis_kelamin', 'pola_makan', 'aktivitas_fisik']]
y = df['obesitas']

# Membagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Mengstandarkan fitur
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Membuat model regresi logistik
model = LogisticRegression()
model.fit(X_train, y_train)

# Memprediksi
y_pred = model.predict(X_test)

# Menampilkan akurasi dan laporan klasifikasi
print("Akurasi:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
