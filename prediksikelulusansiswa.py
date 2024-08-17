# %%
# Mengimpor pustaka pandas untuk pengolahan data
import pandas as pd

# Membaca dataset dari file CSV ke dalam DataFrame
df = pd.read_csv('students-final-grade.csv')

# %%
# Mengonversi kolom 'homework_completion' menjadi nilai numerik
# Jika 'yes' maka 1, jika 'no' maka 0
df['homework_completion'] = df['homework_completion'].apply(lambda x: 1 if x == 'yes' else 0)

# %%
# Memilih fitur yang akan digunakan untuk prediksi
# 'X' berisi nilai-nilai dari mata pelajaran, persentase kehadiran, dan penyelesaian tugas
X = df[['math_score', 'science_score', 'english_score', 'history_score', 'attendance_percentage', 'homework_completion']]

# Mendefinisikan target (label) 'y' sebagai kelulusan, dengan syarat nilai akhir > 75
y = df['final_score'] > 75  # Nilai di atas 75 dinyatakan lulus

# %%
# Mengimpor DecisionTreeClassifier dari scikit-learn
from sklearn.tree import DecisionTreeClassifier

# Membuat dan melatih model Decision Tree menggunakan data X dan y
model = DecisionTreeClassifier()
model.fit(X, y)

# %%
# Mengimpor pustaka Streamlit untuk membuat aplikasi web interaktif
import streamlit as st

# Judul aplikasi
st.title('Prediksi Kelulusan Siswa')

# Input dari pengguna
math_score = st.number_input('Nilai Matematika')
science_score = st.number_input('Nilai Sains')
english_score = st.number_input('Nilai Bahasa Inggris')
history_score = st.number_input('Nilai Sejarah')
attendance_percentage = st.slider('Persentase Kehadiran', 0, 100)
homework_completion = st.selectbox('Penyelesaian Tugas', ['yes', 'no'])

# Konversi input
homework_completion = 1 if homework_completion == 'yes' else 0

# Membuat DataFrame dari input pengguna
input_data = pd.DataFrame({
    'math_score': [math_score],
    'science_score': [science_score],
    'english_score': [english_score],
    'history_score': [history_score],
    'attendance_percentage': [attendance_percentage],
    'homework_completion': [homework_completion]
})

# Membuat prediksi
prediction = model.predict(input_data)

# Menampilkan hasil prediksi
if st.button('Prediksi'):
    st.write('Lulus' if prediction else 'Tidak Lulus')


