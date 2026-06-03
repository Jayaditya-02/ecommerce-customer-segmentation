# E-Commerce Online Retail Customer Segmentation for Smart Incentive System

This mini project segments online retail customers using RFM analysis and K-Means clustering. The system identifies customer groups based on purchasing behavior and recommends suitable incentives such as loyalty rewards, cashback, reactivation coupons, free shipping, and welcome offers.

## Project Overview

Online retail businesses serve customers with different purchase patterns. Some customers buy frequently, some spend high amounts, some are new, and some have not purchased recently. Sending the same offer to every customer is inefficient and may reduce marketing effectiveness.

This project uses transaction data to calculate Recency, Frequency, and Monetary values for each customer. These features are used with K-Means clustering to divide customers into meaningful segments. A Streamlit dashboard displays customer segments, visualizations, and incentive recommendations.

## Objectives

- Analyze online retail transaction data.
- Clean and preprocess customer purchase records.
- Generate RFM features for customer behavior analysis.
- Segment customers using K-Means clustering.
- Recommend smart incentives for each customer segment.
- Build an interactive Streamlit dashboard for visualization and reporting.

## Technology Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Plotly
- Streamlit
- Jupyter Notebook

## Project Structure

```text
MINI PROJECT/
  app/
    app.py
  data/
    raw/
      Online Retail.xlsx
    processed/
      customer_segments.csv
  docs/
    ABSTRACT.md
    PROJECT_REPORT.md
  models/
    kmeans_model.pkl
    scaler.pkl
  customer_segmentation.ipynb
  requirements.txt
  README.md
```

## Run Locally

```bash
cd "/Users/kasulajayaditya/Documents/MINI PROJECT"
source .venv/bin/activate
streamlit run app/app.py
```

## Main File for Deployment

```text
app/app.py
```

## Live Project Link

Add your Streamlit deployment link here after deployment.

