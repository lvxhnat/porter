import streamlit as st

from porter.components import create_transaction_table

def app() -> None:
    user_input = st.text_input("Alphavantage API Key")
    create_transaction_table()
    print(user_input)
    return 

app()