import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

st.title("Data Penguins")
penguins_df = pd.read_csv("penguins.csv")
st.write("AgGrid DataFrame:")
response = AgGrid(penguins_df, height=500, editable=True, theme='alpine', fit_columns_on_grid_load=True, enable_enterprise_modules=True, allow_unsafe_jscode=True, key='grid')
df_edited = response["data"]
st.write("Edited DataFrame:")
st.dataframe(df_edited)
 
