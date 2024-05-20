import streamlit as st
import pandas as pd
import gspread
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
import time
from datetime import datetime
import json

st.sidebar.title("Read")
st.title("Read - Dashboard")
st.caption("PandeAkshat")

option = st.sidebar.radio(" ", ("All", "Article", "Book", "YouTube", "Documentary", "Podcast"))


g_credentials = st.secrets["google_auth"]
cred = dict(g_credentials) 
# Google Sheets Authentication
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_dict( cred, scope)
gc = gspread.authorize(credentials)


# Load Google Sheet data
sheet_url = cred.get("spreadsheet")
spreadsheet = gc.open_by_url(sheet_url)
worksheet = spreadsheet.worksheet("Read")
data = worksheet.get_all_records()
df = pd.DataFrame(data)


if option=='All':
    for item in df.itertuples():
        col1, col2,col3 = st.columns([4,1,1])
        with col1:
            with st.expander(item.Title + 'by' + item.Author + ' ----- [' + item.Category + ']'):
                st.write(item.Description)
        with col2:
            st.link_button('Review', item.Review)
        with col3:
            st.link_button('Resource', item.Resource)

if option=='Article':
    for item in df.itertuples():
        if item.Category=='Article':
            col1, col2,col3 = st.columns([4,1,1])
            with col1:
                with st.expander(item.Title + 'by' + item.Author + ' ----- [' + item.Category + ']'):
                    st.write(item.Description)
            with col2:
                st.link_button('Review', item.Review)
            with col3:
                st.link_button('Resource', item.Resource)

if option=='Book':
    for item in df.itertuples():
        if item.Category=='Book':
            col1, col2,col3 = st.columns([4,1,1])
            with col1:
                with st.expander(item.Title + 'by' + item.Author + ' ----- [' + item.Category + ']'):
                    st.write(item.Description)
            with col2:
                st.link_button('Review', item.Review)
            with col3:
                st.link_button('Resource', item.Resource)
if option=='YouTube':
    for item in df.itertuples():
        if item.Category=='YouTube':
            col1, col2,col3 = st.columns([4,1,1])
            with col1:
                with st.expander(item.Title + 'by' + item.Author + ' ----- [' + item.Category + ']'):
                    st.write(item.Description)
            with col2:
                st.link_button('Review', item.Review)
            with col3:
                st.link_button('Resource', item.Resource)
if option=='Podcast':
    for item in df.itertuples():
        if item.Category=='Podcast':
            col1, col2,col3 = st.columns([4,1,1])
            with col1:
                with st.expander(item.Title + 'by' + item.Author + ' ----- [' + item.Category + ']'):
                    st.write(item.Description)
            with col2:
                st.link_button('Review', item.Review)
            with col3:
                st.link_button('Resource', item.Resource)

if option=='Documentary':
    for item in df.itertuples():
        if item.Category=='Documentary':
            col1, col2,col3 = st.columns([4,1,1])
            with col1:
                with st.expander(item.Title + 'by' + item.Author + ' ----- [' + item.Category + ']'):
                    st.write(item.Description)
            with col2:
                st.link_button('Review', item.Review)
            with col3:
                st.link_button('Resource', item.Resource)
