import matplotlib.pyplot as plt 
import streamlit as st 
import pandas as pd 

suhu = [20, 22, 25, 27, 30, 33, 35, 35, 40]
penjualan = [50, 60, 70, 90, 100, 110, 130, 150, 155]

penjualan_weekdays = [50, 60, 70, 80, 90, 100, 110, 120, 130]
penjualan_weekends = [60, 70, 80, 100, 110, 120, 140, 160, 200]

data = {
    'Suhu': [20, 22, 24, 26, 28, 30, 32, 34, 36],
    'Penjualan_Cokelat': [50, 60, 70, 80, 90, 100, 110, 120, 130],
    'Penjualan_Vanila': [60, 70, 80, 90, 100, 110, 130, 140, 150],
    'Penjualan_Stroberi': [40, 50, 60, 70, 80, 90, 100, 110, 120],
    'Kelembapan': [60, 65, 70, 75, 80, 85, 90, 95, 100]
}

df = pd.DataFrame(data)

st.title('Visualisais Scatter Plot Penjualan Es')
st.sidebar.header("Pengaturan Visualisasi")

option = st.sidebar.selectbox(
    "Pilih cotoh scatter plot",
    (
        "Basic Scatter Plot",
        "Kustomisasi Scatter Plot",
        "Multiple Scatter Plot",
        "Analisis Scatter Plot"
    )
)

st.caption("Praktikum 5 - Matplotlib Scatter Plot")
st.markdown("""
kelompok 21:
- Rio Adi Saputro - 0110122076
""")

def basic_scatter():
    st.subheader("1. Basic Scatte Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan)
    ax.set_title("Hubungan Suhu dan Penjualan")
    ax.set_xlabel("Suhu")
    ax.set_ylabel("Penjualan Es")
    st.pyplot(fig)

def custom_scatter():
    st.subheader("2. Customisasi Scatte Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan, color='orange', s=100, edgecolor='black', alpha=0.7)
    ax.set_title("Hubungan Suhu dan Penjualan")
    ax.set_xlabel("Suhu")
    ax.set_ylabel("Penjualan Es")
    ax.grid(True)
    st.pyplot(fig)

def multiple_scatter():
    st.subheader("3. Multiple Scatte Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan_weekdays, color='green', label='Hari Kerja', s=80)
    ax.scatter(suhu, penjualan_weekends, color='purple', label='Akhir Pekan', s=80)
    ax.set_title("Hubungan Suhu dan Penjualan")
    ax.set_xlabel("Suhu")
    ax.set_ylabel("Penjualan Es")
    ax.grid(True)
    st.pyplot(fig)

def scatter_3_variabel():
    st.subheader("4. Analisis dengan Scatte Plot")
    jenis_eskrim = st.selectbox('Pilih Jenis Es Krim', ['Cokelat', 'Vanila', 'Stroberi'])

    if jenis_eskrim == 'Cokelat':
        penjualan = df['Penjualan_Cokelat']
    elif jenis_eskrim == 'Vanila':
        penjualan = df['Penjualan_Vanila']
    else:
        penjualan = df['Penjualan_Stroberi']
    
    st.subheader("Data Penjualan dan Suhu")
    st.dataframe(df)

    fig, ax = plt.subplots()
    scatter = ax.scatter(df['Suhu'], penjualan, c=df['Kelembapan'], s=100, cmap='coolwarm', alpha=0.7)
    ax.set_title(f'hasil Penjualan {jenis_eskrim} vs Suhu dan Kelembapan')
    ax.set_xlabel('Suhu (°C)')
    ax.set_ylabel(f'Penjualan Es Krim {jenis_eskrim}')
    fig.colorbar(scatter, label='kelembapn (%)')

    st.pyplot(fig)

    st.subheader('Analisis Hubungan')
    st.write(f"Grafik menunjukan hubunganantara suhu, kelembapan, dan penjualan es krim jenis **{jenis_eskrim}**.")

if option == "Basic Scatter Plot":
    basic_scatter()

elif option == "Kustomisasi Scatter Plot":
    custom_scatter()

elif option == "Multiple Scatter Plot":
    multiple_scatter()

elif option == "Analisis Scatter Plot":
    scatter_3_variabel()