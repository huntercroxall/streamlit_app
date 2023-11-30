import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.subheader("Fun App for Cereal")

df = pd.read_csv("cereal.csv")
st.dataframe(df)

st.subheader("Histogram")

st.bar_chart(sns.countplot(penguins, x="species"))