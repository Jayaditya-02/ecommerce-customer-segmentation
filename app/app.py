import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="E-Commerce Customer Segmentation",
    page_icon="🛒",
    layout="wide"
)

st.title("E-Commerce Online Retail Customer Segmentation")
st.subheader("Smart Incentive Recommendation System")

DATA_PATH = "data/processed/customer_segments.csv"
@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()

st.sidebar.header("Filters")

segments = st.sidebar.multiselect(
    "Select Customer Segment",
    options=df["Segment"].unique(),
    default=df["Segment"].unique()
)

filtered_df = df[df["Segment"].isin(segments)]

total_customers = filtered_df["CustomerID"].nunique()
avg_recency = round(filtered_df["Recency"].mean(), 2)
avg_frequency = round(filtered_df["Frequency"].mean(), 2)
avg_monetary = round(filtered_df["Monetary"].mean(), 2)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", total_customers)
col2.metric("Avg Recency", avg_recency)
col3.metric("Avg Frequency", avg_frequency)
col4.metric("Avg Monetary", avg_monetary)

st.markdown("---")

left, right = st.columns(2)

with left:
    segment_count = filtered_df["Segment"].value_counts().reset_index()
    segment_count.columns = ["Segment", "Count"]

    fig1 = px.bar(
        segment_count,
        x="Segment",
        y="Count",
        color="Segment",
        title="Customer Count by Segment"
    )
    st.plotly_chart(fig1, use_container_width=True)

with right:
    fig2 = px.scatter(
        filtered_df,
        x="Recency",
        y="Monetary",
        color="Segment",
        hover_data=["CustomerID", "Frequency"],
        title="Recency vs Monetary Value"
    )
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

st.subheader("Smart Incentive Recommendations")

recommendation_table = filtered_df[
    ["CustomerID", "Segment", "Recency", "Frequency", "Monetary", "Recommended_Incentive"]
]

st.dataframe(recommendation_table, use_container_width=True)

st.download_button(
    label="Download Customer Incentive Report",
    data=recommendation_table.to_csv(index=False),
    file_name="customer_incentive_report.csv",
    mime="text/csv"
)