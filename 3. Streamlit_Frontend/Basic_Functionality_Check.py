import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Streamlit APP")
st.write("This is a simple app demonstrates basic functionalities of streamlit")

st.sidebar.header("User input features")

# user input - user name
user_name = st.sidebar.text_input("User Name")

# user password
user_pswd = st.sidebar.text_input("Password", type='password')

age = st.sidebar.slider("select your age", 1, 100, 22)

desease = st.sidebar.selectbox("What is your health problem",["headche", "fever", "cold", "caugh"])

# Main page content
st.header(f"Welcome {user_name} !!")
st.write(f"You have scheduled apppointment for general health check up - major issue is {desease}")

# --- Displaying Data ---
st.subheader("Here's some random data of Patient ")

# Create a sample data frame
data = pd.DataFrame(
    np.random.randn(10,5),
    columns = ('col %d' % i for i in range(5)) 
)

st.dataframe(data)

# check box to show or hide content
if st.checkbox("show raw data"):
    st.subheader("Raw Data")
    st.write(data)
    
# Button to trigger an action
if st.button("Say Hello!"):
    st.write("Hello there !")
else:
    st.write("Goodbye !!")

    

