import streamlit as st
from zerodha_charges import zerodha_charges
import pandas as pd

st.title("Calculate Zerodha Charges For Intraday And Delivery")
amount = st.number_input("Enter the total amount for buy/sell:", min_value=0.0, step=0.01)
market = st.selectbox("Select Marketplace:", ["BSE", "NSE"])
type = st.selectbox("Select Transaction Type:", ["delivery", "intraday"])
intent = st.selectbox("Select Intent Type:", ["buy", "sell"])

if st.button("Calculate"):
     results, charges_list = zerodha_charges(amount = amount, type = type, market = market, intent = intent)
     if isinstance(results, str):
         st.error(results)
     else:
        st.write(f"For your invested amount of {amount}, approximate net will be: {results['Net amount']:.4f}")
        st.write(f"Your total charges will be: {results['Total charges']:.4f}")
        df = pd.DataFrame(list(results.items()), columns=[
                          "Charge Type", "Amount"])
        st.write("Charges Breakdown:")
        st.dataframe(df)
        st.write("Zerodha also charges AMC that we have not taken into account. Rs 100 to 300 per annum.")
        
