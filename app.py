import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("News Sentiment Dashboard")

output_path = "stream_output/"
if os.path.exists(output_path):
    df = pd.read_parquet(output_path)
    st.write(df)
    fig = px.histogram(df, x="sentiment")
    st.plotly_chart(fig)
else:
    st.write("No data yet. Run streaming_process.py first.")
