import streamlit as st  
import pandas as pd 
import numpy as np 

st.title("Line Chart")
st.write("Kelompok 21")
st.markdown("""
    - Rio Adi Saputro (0110122076)
    - Nama (NIM)
""")

df = pd.DataFrame(
    np.random.randn(50, 2)/[10,10] +[15.4589, 75.0078],
    columns=["latitude", "longitude"]
)

st.map(df)