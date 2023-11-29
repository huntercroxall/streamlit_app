import streamlit as st
import pandas as pd
import seaborn as sns

st.title("Fun App for Cereal")

df = pd.read_csv("cereal.csv")
st.dataframe(df)
