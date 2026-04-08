import streamlit as st

st.title("Welcome to Streamlit - App created by Hemalatha")

st.write("This App checks whether EVEN number or ODD number")

st.header("select any number")
number = st.slider("Pick any number", 0, 100, 25)

st.subheader("Result")
if number % 2 == 0:
    st.write(f"Selected number {number} is an Even number")
else:
    st.write(f"Selected number {number} is an ODD number")
