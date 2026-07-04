import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Student Performance Data Analysis Dashboard")

st.write("""
Welcome! This dashboard analyzes the Student Performance dataset using
**Python, Pandas, Matplotlib, and Streamlit**.
""")

st.sidebar.title("Dashboard Menu")
st.sidebar.write("Week 1 Internship Project")
st.sidebar.write("Data Analysis using Streamlit")

df = pd.read_csv("dataset.csv")

st.header("Dataset Preview")
st.dataframe(df.head())


st.header("Dataset Size")

col1, col2 = st.columns(2)

with col1:
    st.metric("Number of Rows", df.shape[0])

with col2:
    st.metric("Number of Columns", df.shape[1])


st.header("Column Names")
st.write(df.columns.tolist())


st.header("Data Types")
st.dataframe(df.dtypes.reset_index().rename(columns={"index":"Column",0:"Data Type"}))


st.header("Statistical Summary")
st.dataframe(df.describe())


st.header("Missing Values")
st.dataframe(df.isnull().sum().reset_index().rename(columns={"index":"Column",0:"Missing Values"}))

st.header("Data Visualizations")

# GPA Distribution
st.subheader("1. GPA Distribution")

fig, ax = plt.subplots(figsize=(7,4))

ax.hist(df["GPA"], bins=10)

ax.set_title("GPA Distribution")
ax.set_xlabel("GPA")
ax.set_ylabel("Number of Students")

st.pyplot(fig)

# Gender Distribution
st.subheader("2. Gender Distribution")

gender = df["Gender"].value_counts()

st.bar_chart(gender)


numeric_columns = df.select_dtypes(include="number").columns.tolist()

if len(numeric_columns) > 0:

    st.subheader("3. Line Chart")

    selected_column = st.selectbox(
        "Select a Numeric Column",
        numeric_columns
    )

    st.line_chart(df[selected_column])

st.header("Dataset Information")

st.write(f"**Total Records:** {len(df)}")
st.write(f"**Total Features:** {len(df.columns)}")


st.success("Dashboard created successfully!")
