import streamlit as st
import pandas as pd
import gspread
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
import time
from datetime import datetime
import json

st.sidebar.title("Write")
st.title("Write - Dashboard")
st.caption("PandeAkshat")

option = st.sidebar.radio(" ", ("All", "Article", "Poetry", "Odyssey", "Newsletter", "Quotes"))


g_credentials = st.secrets["google_auth"]
cred = dict(g_credentials) 
# Google Sheets Authentication
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_dict( cred, scope)
gc = gspread.authorize(credentials)


# Load Google Sheet data
sheet_url = cred.get("spreadsheet")
spreadsheet = gc.open_by_url(sheet_url)
worksheet = spreadsheet.worksheet("Write")
data = worksheet.get_all_records()
df = pd.DataFrame(data)


if option=='All':
    for item in df.itertuples():
        col1, col2 = st.columns([4,1])
        with col1:
            with st.expander(item.Title + ' ----- [' + item.Category + ']'):
                st.write(item.Description)
        with col2:
            st.link_button('Link', item.Link)

if option=='Article':
    for item in df.itertuples():
        if item.Category=='Article':
            col1, col2 = st.columns([4,1])
            with col1:
                with st.expander(item.Title + ' ----- [' + item.Category + ']'):
                    st.write(item.Description)
            with col2:
                st.link_button('Link', item.Link)

if option=='Poetry':
    for item in df.itertuples():
        if item.Category=='Poetry':
            col1, col2 = st.columns([4,1])
            with col1:
                with st.expander(item.Title + ' ----- [' + item.Category + ']'):
                    st.write(item.Description)
            with col2:
                st.link_button('Link', item.Link)

if option=='Odyssey':
    for item in df.itertuples():
        if item.Category=='Odyssey':
            col1, col2 = st.columns([4,1])
            with col1:
                with st.expander(item.Title + ' ----- [' + item.Category + ']'):
                    st.write(item.Description)
            with col2:
                st.link_button('Link', item.Link)

if option=='Newsletter':
    for item in df.itertuples():
        if item.Category=='Newsletter':
            col1, col2 = st.columns([4,1])
            with col1:
                with st.expander(item.Title + ' ----- [' + item.Category + ']'):
                    st.write(item.Description)
            with col2:
                st.link_button('Link', item.Link)

if option=='Quotes':
    for item in df.itertuples():
        if item.Category=='Quotes':
            col1, col2 = st.columns([4,1])
            with col1:
                with st.expander(item.Title + ' ----- [' + item.Category + ']'):
                    st.write(item.Description)
            with col2:
                st.link_button('Link', item.Link)
