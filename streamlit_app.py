import streamlit as st
import pandas as pd
import seaborn as sns

st.title("Hello World")

penguins = sns.load_dataset('penguins')

st.subheader('Raw Data')
st.write(penguins)