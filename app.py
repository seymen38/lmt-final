import streamlit as st

st.set_page_config(page_title="LMT Flight", layout="wide")

st.title("LMT Flight")
st.write("Eger bunu goruyorsan, calisiyor!")

if st.button("Test Et"):
    st.success("Buton calisti!")
