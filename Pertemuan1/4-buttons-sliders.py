import streamlit as st
import time

st.title('Creating a Button')
button = st.button('Click Here')
if button:
    st.write('You have click the Button')
else:
    st.write('You have not clicked the Button')

st.title('Creating Select Radio')
gender = st.radio(
"Select your Gender",
('Male', 'Female'))
if gender == 'Male':
    st.write('You have select Male.')
elif gender == 'Female':
    st.write("You have selected Female.")
else:
    st.write("You have selected Others.")

st.title('Creating Checkboxess')
st.write('Select your Hobbies:')
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

st.title('Creating Dropdown')
hobby = st.selectbox('Choose Your Hobby: ',
('Books', 'Movies', 'Sports'))

st.title('Multi-Select')
hobbies = st.multiselect(
'Whats your Hobbies',
['Reading', 'Cooking', 'Watch Movie', 'Playing', 'Drawing', 'Hiking'],
['Reading', 'Playing']
)

st.title('Progress Bar')
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage+1)
st.write('Download Complete')

st.title('Spinner')
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hello Data Analyst')