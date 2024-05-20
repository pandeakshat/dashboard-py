import streamlit as st
import pandas as pd
import gspread
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
import time
from datetime import datetime
import json

st.sidebar.title("Code")
st.title("Code - Dashboard")
st.caption("PandeAkshat")


option = st.sidebar.radio(" ", ("All", "Python", "Data Science", "Blockchain", "Web Development", "Rust"))



g_credentials = st.secrets["google_auth"]
cred = dict(g_credentials) 
# Google Sheets Authentication
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_dict( cred, scope)
gc = gspread.authorize(credentials)


# Load Google Sheet data
sheet_url = cred.get("spreadsheet")
spreadsheet = gc.open_by_url(sheet_url)
worksheet = spreadsheet.worksheet("Code")
data = worksheet.get_all_records()
df = pd.DataFrame(data)


if option=='All':
    for item in df.itertuples():
        col1, col2,col3 = st.columns([4,1,1])
        with col1:
            with st.expander(item.Title + ' ----- [' + item.Category + ']'):
                st.write(item.Description)
        with col2:
            st.link_button('Project', item.Project)
        with col3:
            st.link_button('Repository', item.Repository)

if option=='Python':
    for item in df.itertuples():
        if item.Category=='Python':
            col1, col2,col3 = st.columns([4,1,1])
            with col1:
                with st.expander(item.Title + ' ----- [' + item.Category + ']'):
                    st.write(item.Description)
            with col2:
                st.link_button('Project', item.Project)
            with col3:
                st.link_button('Repository', item.Repository)

if option=='Data Science':
    for item in df.itertuples():
        if item.Category=='Data Science':
            col1, col2,col3 = st.columns([4,1,1])
            with col1:
                with st.expander(item.Title + ' ----- [' + item.Category + ']'):
                    st.write(item.Description)
            with col2:
                st.link_button('Project', item.Project)
            with col3:
                st.link_button('Repository', item.Repository)
if option=='Blockchain':
    for item in df.itertuples():
        if item.Category=='Blockchain':
            col1, col2,col3 = st.columns([4,1,1])
            with col1:
                with st.expander(item.Title + ' ----- [' + item.Category + ']'):
                    st.write(item.Description)
            with col2:
                st.link_button('Project', item.Project)
            with col3:
                st.link_button('Repository', item.Repository)
if option=='Web Development':
    for item in df.itertuples():
        if item.Category=='Web Development':
            col1, col2,col3 = st.columns([4,1,1])
            with col1:
                with st.expander(item.Title + ' ----- [' + item.Category + ']'):
                    st.write(item.Description)
            with col2:
                st.link_button('Project', item.Project)
            with col3:
                st.link_button('Repository', item.Repository)

if option=='Rust':
    for item in df.itertuples():
        if item.Category=='Rust':
            col1, col2,col3 = st.columns([4,1,1])
            with col1:
                with st.expander(item.Title + ' ----- [' + item.Category + ']'):
                    st.write(item.Description)
            with col2:
                st.link_button('Project', item.Project)
            with col3:
                st.link_button('Repository', item.Repository)