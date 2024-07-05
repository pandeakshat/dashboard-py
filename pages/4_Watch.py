import streamlit as st
import pandas as pd
import gspread
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
import time
from datetime import datetime
import json

st.sidebar.title("Watch")
st.title("Watch - Dashboard")
st.caption("PandeAkshat")


option = st.sidebar.radio(" ", ("All", "Manga/Manhwa", "Anime", "TV Show", "Movie"))


g_credentials = st.secrets["google_auth"]
cred = dict(g_credentials) 
# Google Sheets Authentication
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_dict( cred, scope)
gc = gspread.authorize(credentials)


# Load Google Sheet data
sheet_url = cred.get("spreadsheet")
spreadsheet = gc.open_by_url(sheet_url)
worksheet = spreadsheet.worksheet("Watch")
data = worksheet.get_all_records()
df = pd.DataFrame(data)


if option=='All':
    for item in df.itertuples():
        col1, col2,col3 = st.columns([4,1,1])
        with col1:
            with st.expander(item.Title + ' ----- ' + item.Status + ' ----- [' + item.Category + ']'):
                st.write(item.Description)
        with col2:
            st.link_button('Review', item.Review)
        with col3:
            st.link_button('Resource', item.Resource)

if option=='Manga/Manhwa':
    for item in df.itertuples():
        if item.Category=='Manga/Manhwa':
            col1, col2,col3 = st.columns([4,1,1])
            with col1:
                with st.expander(item.Title + ' ----- ' + item.Status + ' ----- [' + item.Category + ']'):
                    st.write(item.Description)
            with col2:
                st.link_button('Review', item.Review)
            with col3:
                st.link_button('Resource', item.Resource)

if option=='Anime':
    for item in df.itertuples():
        if item.Category=='Anime':
            col1, col2,col3 = st.columns([4,1,1])
            with col1:
                with st.expander(item.Title + ' ----- ' + item.Status + ' ----- [' + item.Category + ']'):
                    st.write(item.Description)
            with col2:
                st.link_button('Review', item.Review)
            with col3:
                st.link_button('Resource', item.Resource)
if option=='TV Show':
    for item in df.itertuples():
        if item.Category=='TV Show':
            col1, col2,col3 = st.columns([4,1,1])
            with col1:
                with st.expander(item.Title + ' ----- ' + item.Status + ' ----- [' + item.Category + ']'):
                    st.write(item.Description)
            with col2:
                st.link_button('Review', item.Review)
            with col3:
                st.link_button('Resource', item.Resource)
if option=='Movie':
    for item in df.itertuples():
        if item.Category=='Movie':
            col1, col2,col3 = st.columns([4,1,1])
            with col1:
                with st.expander(item.Title + ' ----- ' + item.Status + ' ----- [' + item.Category + ']'):
                    st.write(item.Description)
            with col2:
                st.link_button('Review', item.Review)
            with col3:
                st.link_button('Resource', item.Resource)

