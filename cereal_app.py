import streamlit as st
import pandas as pd
import numpy as np

st.title("Fun App for Cereal")

df = pd.read_csv("cereal.csv")
st.dataframe(df)

st.subheader("Histogram")

st.bar_chart(np.histogram(df['calories'], bins=10))