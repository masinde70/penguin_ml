import pandas as pd
import plotly.express as px
import requests
import streamlit as st
from pydantic_settings import BaseSettings
from streamlit_lottie import st_lottie
from streamlit_pandas_profiling import st_profile_report
from streamlit_plotly_events import plotly_events
from ydata_profiling import ProfileReport

df = pd.read_csv("penguins.csv")
from streamlit_plotly_events import plotly_events

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_penguin = load_lottieurl(
    "https://assets9.lottiefiles.com/private_files/lf30_lntyk83o.json"
)
st_lottie(lottie_penguin, height=200, speed=1, reverse=False, loop=True, quality="low")
st.subheader("Pandas Profiling of Penguin Dataset")

fig = px.scatter(df, x="bill_length_mm", y="bill_depth_mm", color="species")
selected_point = plotly_events(fig, click_event=True)

penguin_profile = ProfileReport(df, explorative=True)
st_profile_report(penguin_profile)



