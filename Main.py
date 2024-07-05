import streamlit as st
import pandas as pd
import gspread
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
import time
from datetime import datetime
import json

st.sidebar.title("Main")
st.title("Main - Dashboard")
st.caption("Akshat Pande (pandeakshat)")


st.header("A centralized structure for collection of everything that I will build.")

st.write('''

    I am passionate about a lot of things. I love to code project in Python, Rust, and JavaScript and in the domains of Web Development, Blockchain, and Data Science.
I also love to write! Articles and Poetry, plus my current project regarding Odyssey, and my newsletter, for which you can subscribe here.
Moreover, I love to learn, read, watch, and share! Hence a reading list of the books, article, youtube videos, and podcasts that made me learn more and fascinated me about something I got to know.
Just a few more, I don't watch a lot of things but I want to keep up with society so Anime and Manga for sure, and then some TV Shows and Movies, obviously with my reviews and opinions on the same.
        ''')

st.write("Finally, except a resume for people who are interested in hiring me, there is a finance section, that includes my portfolio of currencies, stocks, crypto, commodities, and other assets that I own.")

st.header("Make sure to check out my other projects")

st.link_button("Status Window", "https://status.pandeakshat.com")
st.link_button("Portfolio", "https://pandeakshat.com")

st.sidebar.caption("Created by:")
st.sidebar.error("Akshat Pande (pandeakshat)")
st.sidebar.link_button("Github", "https://github.com/pandeakshat")


