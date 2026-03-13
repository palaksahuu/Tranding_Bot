import streamlit as st
from bot.orders import place_market_order, place_limit_order

st.title("Binance Futures Testnet Trading Bot")

symbol = st.text_input("Symbol", "BTCUSDT")

side = st.selectbox("Side", ["BUY", "SELL"])

order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])

quantity = st.number_input("Quantity", min_value=0.001)

price = None

if order_type == "LIMIT":
    price = st.number_input("Price", min_value=1.0)

if st.button("Place Order"):

    try:

        if order_type == "MARKET":
            response = place_market_order(symbol, side, quantity)
        else:
            response = place_limit_order(symbol, side, quantity, price)

        st.success("Order placed successfully")

        st.write("Order ID:", response.get("orderId"))
        st.write("Status:", response.get("status"))
        st.write("Executed Qty:", response.get("executedQty"))
        st.write("Avg Price:", response.get("avgPrice"))

    except Exception as e:

        st.error(str(e))