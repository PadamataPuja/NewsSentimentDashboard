import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("News Sentiment Dashboard")

output_path = "stream_output/"

if os.path.exists(output_path):
    # List all Parquet files in the folder
    parquet_files = [os.path.join(output_path, f) for f in os.listdir(output_path) if f.endswith(".parquet")]

    if parquet_files:
        # Load and combine all Parquet files
        df_list = [pd.read_parquet(f) for f in parquet_files]
        df = pd.concat(df_list, ignore_index=True)

        st.write("Columns in DataFrame:", df.columns)
        st.write(df.head())

        # Use the actual prediction column name
        if "prediction" in df.columns:
            fig = px.histogram(df, x="prediction")
            st.plotly_chart(fig)
        else:
            st.write("No 'prediction' column found in the data.")
    else:
        st.write("No Parquet files found in stream_output/.")
else:
    st.write("No data yet. Run streaming_process.py first.")
