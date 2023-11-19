import streamlit as st
import pandas as pd
import plotly.express as px


def load_data():
    return pd.read_csv("happy.csv")


data = load_data()
st.header("In Search for Happiness")

option1 = st.selectbox("Select the data fo X-axis", data.columns)
option2 = st.selectbox("Select the data for Y-axis", data.columns)

st.subheader("GDP and Happiness")

figure = px.line(x=data[option1], y=data[option2], labels={"x": option1, "y": option2})
st.plotly_chart(figure)
