import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# load dataset
def load_data_hour():
    data = pd.read_csv('./hour.csv')
    data['dteday'] = pd.to_datetime(data['dteday'])
    return data

def load_data_day():
    data = pd.read_csv('./day.csv')
    data['dteday'] = pd.to_datetime(data['dteday'])
    return data

df_hour = load_data_hour()
df_day = load_data_day()

# judul dashboard
st.title('Bike Sharing Data Insights Dashboard')

# bikin tab
tab1, tab2 = st.tabs(["Pertanyaan 1", "Pertanyaan 2"])
 
with tab1:
    # penggunaan paling tinggi
    st.header('Kapan dan pada musim apa jumlah pengguna sepeda paling banyak?')

    hourly_usage = df_hour.groupby('hr')['cnt'].mean()
    daily_usage = df_day.groupby('weekday')['cnt'].mean()
    seasonal_usage = df_day.groupby('season')['cnt'].mean()

    # perjam
    plt.figure(figsize=(10, 6))
    sns.barplot(x=hourly_usage.index, y=hourly_usage.values, palette='coolwarm')
    plt.axvline(x=8, color='red', linestyle='--', label='Waktu Penggunaan Terbanyak: 8 AM')
    plt.axvline(x=17, color='red', linestyle='--', label='Waktu Penggunaan Terbanyak: 5-6 PM')
    plt.title('Rata-rata Pengguna Sepeda Berdasarkan Jam')
    plt.xlabel('Jam')
    plt.ylabel('Jumlah Pengguna')
    plt.xticks(range(24))
    plt.legend()
    st.pyplot(plt)

    # perhari
    plt.figure(figsize=(10,6))
    sns.barplot(x=daily_usage.index, y=daily_usage.values, palette='coolwarm')
    plt.axvline(x=5, color='red', linestyle='--', label='Hari Penggunaan Terbanyak: Kamis')
    plt.axvline(x=6, color='red', linestyle='--', label='Hari Penggunaan Terbanyak: Jumat')
    plt.title('Rata-rata Pengguna Berdasarkan Hari dalam Seminggu')
    plt.xlabel('Hari dalam Minggu')
    plt.ylabel('Jumlah Pengguna')
    plt.legend()
    st.pyplot(plt)

    # permusim
    plt.figure(figsize=(10,6))
    sns.barplot(x=seasonal_usage.index, y=seasonal_usage.values, palette='pastel')
    plt.title('Rata-rata Pengguna Sepeda Tiap Musim')
    plt.xlabel('Musim (1: Semi, 2: Panas, 3: Gugur, 4: Dingin)')
    plt.ylabel('Rata-rata Pengguna Sepeda')
    st.pyplot(plt)

    st.header("Kesimpulan:")
    st.text("Pengguna sepeda paling banyak pada jam 8 pagi dan jam 5 hingga 6 sore.\nPengguna sepeda paling banyak terjadi pada musim gugur.")
 
with tab2:
    # penurunan jumlah pengguna
    st.header('Pada kondisi bagaimana terjadi penurunan pengguna sepeda?')

    weather_conditions = df_day.groupby('weathersit')['cnt'].mean()
    temp_conditions = df_day.groupby('temp')['cnt'].mean()
    hum_conditions = df_day.groupby('hum')['cnt'].mean()

    # hujan lebat/salju lebat
    plt.figure(figsize=(10,6))
    sns.barplot(x=weather_conditions.index, y=weather_conditions.values, palette='Set2')
    plt.title('Rata-rata Pengguna Sepeda Berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Rata-rata Pengguna Sepeda')
    st.pyplot(plt)

    # suhu
    plt.figure(figsize=(8,6))
    sns.scatterplot(x=temp_conditions.index, y=temp_conditions.values, palette='Set2')
    plt.title('Rata-rata Pengguna Sepeda Berdasarkan Suhu')
    plt.xlabel('Suhu')
    plt.ylabel('Rata-rata Pengguna Sepeda')
    st.pyplot(plt)

    # kelembapan
    plt.figure(figsize=(8,6))
    sns.scatterplot(x=hum_conditions.index, y=hum_conditions.values, palette='Set2')
    plt.title('Rata-rata Pengguna Sepeda Berdasarkan Kelembapan')
    plt.xlabel('Kelembapan')
    plt.ylabel('Rata-rata Pengguna Sepeda')
    st.pyplot(plt)

    st.header("Kesimpulan:")
    st.text("Pengguna sepeda mengalami penurunan drastis pada kondisi hujan deras atau salju\nderas, suhu yang terlalu panas atau terlalu dingin, dan pada kelembapan ekstrem.")

# data aslinya
st.sidebar.subheader('Analisis lebih lanjut')
show_raw_data = st.sidebar.checkbox('Tunjukkan Data Mentah')

if show_raw_data:
    st.write('## Data Mentah')
    st.write(df_hour)
    st.write(df_day)

