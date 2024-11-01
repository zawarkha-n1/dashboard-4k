import streamlit as st 
from streamlit_gsheets import GSheetsConnection


def db_conn():
    conn = st.connection("gsheets", type=GSheetsConnection)
    return conn