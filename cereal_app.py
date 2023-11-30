import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def calculate_bmi(height, weight):
    height_meters = height / 100
    bmi = weight / (height_meters ** 2)
    return bmi

st.title("Height and Weight Visualization")

height = st.slider("Select Height (inches)", 30, 100, 75)

weight = st.slider("Select Weight (pounds)", 20, 300, 120)

bmi = calculate_bmi(height, weight)

st.write(f"**BMI:** {bmi:.2f}")

fig, ax = plt.subplots()
ax.scatter(height, weight, color='blue', s = 100, label='Individual')

ax.set_xlim(left=0, right=100)
ax.set_ylim(bottom=0, top=300)
ax.set_xlabel('Height in inches')
ax.set_ylabel('Weight in pounds')
ax.set_title('Height vs. Weight')
ax.legend()

st.pyplot(fig)

st.write("Did you find this app awesome?")

agree = st.checkbox('Yes')
disagree = st.checkbox('No')
maybe = st.checkbox('Maybe so')

if agree:
    st.write(':smile:'*100)
if disagree:
    st.write(":cry:"*100)
if maybe:
    st.write(":wink:"*100)
