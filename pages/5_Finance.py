import streamlit as st
import pandas as pd
import gspread
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
import time
from datetime import datetime
import json

st.sidebar.title("Finance")
st.title("Finance - Dashboard")
st.caption("PandeAkshat")


option = st.sidebar.radio(" ", ("Currency", "Stock", "Crypto", "Commodity", "Asset"))



g_credentials = st.secrets["google_auth"]
cred = dict(g_credentials) 
# Google Sheets Authentication
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_dict( cred, scope)
gc = gspread.authorize(credentials)


# Load Google Sheet data
sheet_url = cred.get("spreadsheet")
spreadsheet = gc.open_by_url(sheet_url)
worksheet = spreadsheet.worksheet("Finance")
data = worksheet.get_all_records()
st.dataframe(data)