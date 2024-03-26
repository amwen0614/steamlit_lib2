import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="工程咨询知识库",
    page_icon="👋",
)

st.write("hello!")

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)