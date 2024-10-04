import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset
def load_data():
    data = pd.read_csv('D:\projects\dicoding\dashboard\hour.csv')
    data['dteday'] = pd.to_datetime(data['dteday'])
    return data

df = load_data()

# judul dashboard
st.title('Bike Sharing Data Insights Dashboard')

# penggunaan paling tinggi
st.write('## Penggunaan Sepeda Tertinggi')
hourly_usage = df.groupby('hr')['cnt'].mean()

plt.figure(figsize=(10, 6))
sns.barplot(x=hourly_usage.index, y=hourly_usage.values, palette='coolwarm')
plt.axvline(x=8, color='red', linestyle='--', label='Waktu Penggunaan Terbanyak: 8 AM')
plt.axvline(x=17, color='red', linestyle='--', label='Waktu Penggunaan Terbanyak: 5-6 PM')
plt.title('Rata-rata Penggunaan Sepeda Per Jam Dalam Sehari')
plt.xlabel('Jam Per Hari')
plt.ylabel('Rata-rata Pengguna Sepeda')
plt.xticks(range(24))
plt.legend()
st.pyplot(plt)

# analisi musim
st.write('## Analisis Tiap Musim')
seasonal_usage = df.groupby('season')['cnt'].mean()

plt.figure(figsize=(10, 6))
sns.barplot(x=seasonal_usage.index, y=seasonal_usage.values, palette='pastel')
plt.title('Rata-rata Pengguna Sepeda Tiap Musim')
plt.xlabel('Musim (1: Semi, 2: Panas, 3: Gugur, 4: Dingin)')
plt.ylabel('Rata-rata Pengguna Sepeda')
st.pyplot(plt)

# dampak cuaca
st.write('## Dampak Cuaca Terhadap Pengguna Sepeda')

# hujan lebat/salju lebat
weather_conditions = df.groupby('weathersit')['cnt'].mean()
plt.figure(figsize=(10, 6))
sns.barplot(x=weather_conditions.index, y=weather_conditions.values, palette='Set2')
plt.title('Rata-rata Pengguna Sepeda Berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Rata-rata Pengguna Sepeda')
st.pyplot(plt)

# data aslinya
st.sidebar.subheader('Analisis lebih lanjut')
show_raw_data = st.sidebar.checkbox('Tunjukkan Data Mentah')

if show_raw_data:
    st.write('## Data Mentah')
    st.write(df)
