import streamlit as st
import pandas as pd


st.title("Fun App for Cereal")

df = pd.read_csv("cereal.csv")
