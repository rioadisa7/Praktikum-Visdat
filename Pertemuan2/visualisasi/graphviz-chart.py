import streamlit as st  
import graphviz as graphviz

st.title("Graph Chart")
st.write("Kelompok 21")
st.markdown("""
    - Rio Adi Saputro (0110122076)
    - Nama (NIM)
""")

st.graphviz_chart("""
    digraph {
        "Training Data" -> "ML Algorithm"
        "ML Algorithm"-> "Model"
        "Model" -> "Result Forecasting"
        "New Data" -> "Model"
        }
""")