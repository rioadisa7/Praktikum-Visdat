import streamlit as st

st.title("Text Box")
name = st.text_input("Enter Your Name")
st.write("Your Name Is", name)

input_text = st.text_area("Enter Your Review")
st.write("""You Entered: \n""", input_text)

num = st.number_input("Enter Your Number", 0, 10, 5, 2)
st.write("Min. Value is 0, \n Max. Value is 10")
st.write("Default is 5, \n Step size is 2")
st.write("Total value after adding Number entered with step value is", num)

st.title("Time")
st.time_input("Select Your Time")

import streamlit as st
import datetime

st.title("Date")

st.date_input("Select Your Date", 
value=datetime.date(1989, 12, 25),
min_value=datetime.date(1987, 1, 1),
max_value=datetime.date(2005, 12, 1))

st.title("Select Color")
color_code = st.color_picker("Select Your Color")
st.header(color_code)

st.title("CSV Data")

data_file = st.file_uploader("Upload CSV", type=["csv"])
details = st.button("Check Details")

if details:
    if data_file is not None:
        file_details = {"file_name": data_file.name, 
                        "file_type": data_file.type, 
                        "file_size": data_file.size}
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write("No CSV File is Uploaded")

my_form = st.form(key='form')
a = my_form.text_input(label='Enter any text')

submit_button = my_form.form_submit_button(label='Submit')
st.write(a)






