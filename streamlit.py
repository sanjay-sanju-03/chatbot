import streamlit as st


st.title('Summarization Applicstion')


inp_text=st.text_area('Enter your text here')
clicked=st.button('Summarize!')
