import streamlit as st
import pandas as pd
import numpy as np


st.title("Motor Vehicle Collisions in NY City")
st.markdown("This application is a Streamlit Dashboard that can be used to analyze motor vehicle collisions in NY City.")

@st.cache(persist = True)
def load_data(rows):
	data = pd.read_csv("Motor_Vehicle_Collisions_-_Crashes.csv", nrows = row, parse_dates =[['CRASH_DATE', 'CRASH_TIME']])
	data.dropna(subset=[['LATITUDE', 'LONGITUDE']], inplace = True)
	lowercase= lambda x: str(x).lower()
	data.rename(lowercase, axis= 'columns', inplace = True)
	return data

data = load_data(1000)
if st.checkbox("Show Raw Data", False):
	
st.subheader("Raw Data")
st.write(data)
	
