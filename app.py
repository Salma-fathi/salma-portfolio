import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Salma Mohammed | Interactive Portfolio", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: #0f172a;
        color: #f1f5f9;
    }
    [data-testid="stSidebar"] {
        background: #020617;
    }
    h1, h2, h3, h4, h5, h6, p, label, span {
        color: #f8fafc;
    }
    .stMarkdown, .stCaption {
        color: #cbd5e1;
    }
    div[data-testid="stMetricValue"] {
        color: #22d3ee;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("Navigation")
app_mode = st.sidebar.radio("Go to:", ["About Me & Skills", "Interactive Portfolio", "Contact"])

if app_mode == "About Me & Skills":
    st.title("Business Intelligence & Data Analyst")
    st.subheader("Transforming raw enterprise telemetry into dynamic business architecture.")

    st.write("---")
    st.markdown("### Core Technical Stack")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.success(
            "**Languages & Frameworks**\n\n"
            "- Python (Pandas, NumPy)\n"
            "- SQL (PostgreSQL, BigQuery)"
        )
    with col2:
        st.info(
            "**Business Intelligence**\n\n"
            "- Power BI (DAX Studio)\n"
            "- Tableau Cloud"
        )
    with col3:
        st.warning(
            "**Data Architecture**\n\n"
            "- ETL Pipelines\n"
            "- Advanced Analytical Reporting"
        )

elif app_mode == "Interactive Portfolio":
    st.title("Interactive KPI Dashboard Demo")
    st.caption("This mock dynamic visualization demonstrates pipeline rendering performance built completely inside Python.")

    np.random.seed(42)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    regions = ["North America", "EMEA", "APAC", "LATAM"]

    mock_data = []
    for region in regions:
        base_sales = np.random.randint(40000, 90000)
        for month in months:
            sales = base_sales + np.random.randint(-15000, 20000)
            mock_data.append({"Region": region, "Month": month, "Sales ($)": sales})

    df = pd.DataFrame(mock_data)
    df["Month"] = pd.Categorical(df["Month"], categories=months, ordered=True)

    st.write("### Dashboard Filters")
    selected_region = st.selectbox("Select Business Territory Region:", regions)

    filtered_df = df[df["Region"] == selected_region].sort_values("Month")

    fig = px.line(
        filtered_df,
        x="Month",
        y="Sales ($)",
        title=f"2026 Commercial Revenue Trendline for {selected_region}",
        markers=True,
        template="plotly_dark",
    )
    fig.update_traces(line_color="#22d3ee", line_width=3)
    fig.update_layout(
        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",
        font_color="#e2e8f0",
        xaxis_title=None,
        yaxis_title="Sales ($)",
    )

    st.plotly_chart(fig, use_container_width=True)

    st.write("---")
    st.markdown("### Case Study: Enterprise Sales & Segmentation")
    st.markdown(
        """
        - **The Problem:** Fragmented system reporting causing severe blindspots in targeted consumer retention leading to an unchecked churn curve.
        - **The Data-Driven Solution:** Automated script querying transactional databases, running data engineering transformations and deploying interactive filters.
        - **Business Impact:** **Boosted localized conversion rates by 14%** and successfully saved **22% of high-risk churn targets** within the first quarter.
        """
    )

else:
    st.title("Let's Build Something Impactful Together")
    st.write("Feel free to drop a line or review my work via the links below:")
    st.markdown("- **LinkedIn:** [linkedin.com/in/salma](https://linkedin.com)")
    st.markdown("- **GitHub:** [github.com/salma-fathi](https://github.com/salma-fathi)")
    st.markdown("- **Email:** salma@example.com")
