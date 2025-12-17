import streamlit as st 
import matplotlib.pyplot as plt 

month = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec']
product_A_sales = [10,20,35,20,40,60,35,40,70,80,85,80]
product_B_sales = [20,30,10,15,40,45,60,45,70,85,75,90]

# layout stream
st.title("Visualisasi Penjualan Produk")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("Pilih Tipe Visualisasi", ("Single Line Plot",
                                                         "Kustomisasi Line Plot",
                                                         "Garis Berbeda untuk Menunjukkan Trend",
                                                         "Subplot"))

st.caption("Praktikum 3 - Matplotlib Line Chart")
st.markdown("""
Kelompok 21:
- Rio Adi Saputro (0110122076)
- Nama
- Nama
""")


#   linestyle='--', market='o'
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(month, product_A_sales, label="Product A", color="blue")
    ax.set_title('Penjualan Produk A Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    st.pyplot(fig)
     
def customize_line_plot():
    fig, ax = plt.subplots()
    ax.plot(month, product_A_sales, label="Product A", color="blue", linestyle='--', marker='o')
    ax.plot(month, product_B_sales, label="Product A", color="red", linestyle='-', marker='x')
    ax.set_title('Penjualan Produk Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Data Sampel Tambahan
product_C_sales = [15,25,30,25,35,40,50,30,60,70,75,90]
product_D_sales = [10,20,20,25,30,40,60,55,70,60,80,85]

def trend_line_plot():
    fig, axs = plt.subplots()
    axs.plot(month, product_C_sales, label="Product C", color="green", linestyle='--')
    axs.plot(month, product_D_sales, label="Product D", color="purple", linestyle='-')
    axs.set_title('Penjualan Produk Per Bulan')
    axs.set_xlabel('Bulan')
    axs.set_ylabel('Jumlah Penjualan')
    axs.legend()
    axs.grid(True)
    st.pyplot(fig)


def subplots():
    fig, axs = plt.subplots(2,1, figsize=(10, 8))
    axs[0].plot(month, product_C_sales, label='Product C', color='green', marker='o')
    axs[0].set_title('Penjualan Produk C Per Bulan')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Jumlah Penjualan')
    axs[0].legend()
    axs[0].grid(True)

    axs[1].plot(month, product_D_sales, label='Product D', color='purple', marker='x')
    axs[1].set_title('Penjualan Produk D Per Bulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Jumlah Penjualan')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    st.pyplot(fig)


if option == "Single Line Plot":
    line_plot()
elif option == "Kustomisasi Line Plot":
    customize_line_plot()
elif option == "Garis Berbeda untuk Menunjukkan Trend":
    trend_line_plot()
elif option == "Subplot":
    subplots()