import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values(by="Date")

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

df_filtered = df[df["Month"] == month]

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# revenue per unit (faturamento por unidade)
fig_date = px.bar(
    df_filtered, x="Date", y="Total", color="City", title="Billing per Day"
)
col1.plotly_chart(fig_date, use_container_width=True)

# most sold product
fig_product = px.bar(
    df_filtered,
    x="Date",
    y="Product line",
    color="City",
    title="Billing per Product",
    orientation="h",
)
col2.plotly_chart(fig_product, use_container_width=True)

# average evaluation of each branch
city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_average = px.bar(city_total, x="City", y="Total", title="Billing per Branch")
col3.plotly_chart(fig_average, use_container_width=True)

# performance of payment methods
fig_payment = px.pie(
    df_filtered,
    values="Total",
    names="Payment",
    color="City",
    title="Payment Measure",
)
col4.plotly_chart(fig_payment, use_container_width=True)

# media de avaliacao de cada cidade
fig_evaluation = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_average = px.bar(fig_evaluation, x="City", y="Rating", title="Evaluation Branch")
col5.plotly_chart(fig_average, use_container_width=True)
