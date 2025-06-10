import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="🌍 GDP per Capita Dashboard", layout="wide")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("gdp_per_capita.csv")

df = load_data()

st.title("🌍 GDP per Capita Analysis Dashboard")

# Basic info
st.subheader("Dataset Preview")
if st.checkbox("Show raw data"):
    st.dataframe(df.head(100))

# Filter data by year
st.sidebar.header("Filter Options")

min_year, max_year = int(df["Year"].min()), int(df["Year"].max())
selected_year = st.sidebar.slider("Select Year", min_value=min_year, max_value=max_year, value=max_year)

# Filter by selected year
year_df = df[df["Year"] == selected_year]

# Select countries
countries = df["Entity"].unique().tolist()
selected_countries = st.sidebar.multiselect("Select Countries", countries, default=["India", "United States", "China"])

# Line chart for GDP per capita over years
st.subheader("📈 GDP per Capita Over Time")
for country in selected_countries:
    country_data = df[df["Entity"] == country]
    st.line_chart(country_data.set_index("Year")["GDP per capita"], height=300, use_container_width=True)

# Correlation heatmap
st.subheader(f"📊 Correlation Heatmap for {selected_year}")
numeric_cols = year_df.select_dtypes(include=['float64', 'int64']).drop(columns=["Year"])
correlation = numeric_cols.corr()

fig, ax = plt.subplots(figsize=(10, 5))
sns.heatmap(correlation, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Country comparison
st.subheader(f"📊 Country Comparison for {selected_year}")
comp_col = st.selectbox("Select a metric", ["GDP per capita", 
                                            "Value of global merchandise exports as a share of GDP", 
                                            "Trade as a Share of GDP", 
                                            "Inflation, consumer prices (annual %)"])
plot_df = year_df[year_df["Entity"].isin(selected_countries)][["Entity", comp_col]]
st.bar_chart(plot_df.set_index("Entity"))

st.markdown("---")
st.caption("Data source: gdp_per_capita.csv")
