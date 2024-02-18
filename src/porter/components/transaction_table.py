import streamlit as st
import pandas as pd
from datetime import datetime

def create_transaction_table():
    
    # Initialize the session state for the table if it does not exist
    if 'table_data' not in st.session_state:
        st.session_state.table_data = pd.DataFrame(columns=['Date', 'Ticker', 'Execution Price', 'Units', 'Transaction Fee'])

    # Function to add a new row to the table
    def add_row(date, ticker, execution_price, units, transaction_fee):
        new_row = {'Date': date,
                'Ticker': ticker,
                'Execution Price': execution_price,
                'Units': units,
                'Transaction Fee': transaction_fee}
        
        st.session_state.table_data.loc[len(st.session_state.table_data)] = new_row

    # Input form
    with st.form("add_row_form"):
        date = st.date_input("Date", datetime.now())
        ticker = st.text_input("Ticker")
        execution_price = st.number_input("Execution Price", format="%.2f")
        units = st.number_input("Units", format="%d")
        transaction_fee = st.number_input("Transaction Fee", format="%.2f")
        
        submit_button = st.form_submit_button("Add Row")

    if submit_button:
        add_row(date, ticker, execution_price, units, transaction_fee)

    # Display the table
    st.table(st.session_state.table_data)
