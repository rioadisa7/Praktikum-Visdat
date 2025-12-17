import streamlit as st
import pandas as pd  
import numpy as  np 
import altair as alt 


st.title("Praktikum 1")
st.caption("Text Element")
st.markdown("""
Kelompok:
- Rio  Adi  Saputro - 0110122076
- Nama - NIM
- Nama - NIM
""")

st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)

st.dataframe(df)

st.subheader("Highlight Minimum Value di DataFrame")

st.dataframe(df.style.highlight_min(axis=0))

st.subheader("Tabel Statis")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)

st.table(df)

st.subheader("Metrics")

st.metric(label="Temperatur", value="31 °C", delta="1.2 °C")

col1, col2, col3 = st.columns(3)

col1.metric("Curah Hujan",  "100 cm", "10 cm")
col2.metric(label="Populasi", value="100 miliar", delta="1 miliar",
delta_color="inverse")
col3.metric(label="Pelanggan", value="100", delta="10",
delta_color="off")

st.metric(label="Speed", value=None, delta=0)
st.metric("Tres", "91456", "-1132649")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)

st.write('Here is out Data', df, 'Data is in dataframe format.\n', "\nWrite is Super function")

df = pd.DataFrame(
np.random.randn(10,2),
columns=['a', 'b'])
chart = alt.Chart(df).mark_bar().encode(
x='a', y='b', tooltip=['a', 'b'])
st.write(chart)

"Adding 5 & 4 =", 5+4

a = 5
'a', a

"""
# Magic Feature
Markdown working without desining its function explicitly.
"""

df = pd.DataFrame({'col': [1,2]})
'dataframe', df

import matplotlib.pyplot as plt
s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)
"chart", chart