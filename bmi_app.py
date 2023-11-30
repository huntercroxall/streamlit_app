import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)


def calculate_bmi(height, weight):
    height_meters = height/100
    bmi = weight / (height_meters ** 2)
    return bmi

st.title("Height and Weight Visualization")

height = st.slider("Select Height (centimeters)", 100, 200, 150)

weight = st.slider("Select Weight (kilograms)", 36, 120, 70)

bmi = calculate_bmi(height, weight)

st.subheader(f"**BMI:** {bmi:.2f}")

if bmi < 18.5:
    st.write("Underweight")
elif bmi >= 18.5 and bmi <= 25:
    st.write("Normal/Healthy Weight")
elif bmi > 25 and bmi < 30:
    st.write("Overweight")
elif bmi >= 30:
    st.write("Obese")

#st.line_chart({"Height": [height], "Weight": [weight]})

fig, ax = plt.subplots()
ax.scatter(height, weight, color='blue', s = 100, label='Individual')

ax.set_xlim(left=100, right=200)
ax.set_ylim(bottom=20, top=150)
ax.set_xlabel('Height in centimeters')
ax.set_ylabel('Weight in kilograms')
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
