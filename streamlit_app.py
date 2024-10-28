import streamlit as st
import pandas as pd 
st.title('NyumbaniTechAI')

st.write('This App is used to create machine language AI')
with st.expander('data'):
 st.write('**raw data**')
 df = pd.read_csv("https://raw.githubusercontent.com/jameschao79/cancer/refs/heads/main/Esophageal_Dataset.csv")
 df
