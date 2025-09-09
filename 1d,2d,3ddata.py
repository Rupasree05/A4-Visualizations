import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# App Title
st.title("📊 1D, 2D & 3D Visualization Explorer")

# File uploader
uploaded_file = st.file_uploader("C:/Users/User/Desktop/Rupa Sree")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("🔍 Dataset Preview")
    st.dataframe(df.head())

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    all_cols = df.columns.tolist()

    # ---------------- 1D VISUALIZATIONS ----------------
    st.header("1D Visualizations")

    one_d_choice = st.selectbox(
        "Choose a 1D plot:",
        ["Bar Chart", "Pie Chart", "Histogram", "Box Plot"]
    )

    if one_d_choice == "Bar Chart":
        x_col = st.selectbox("Select categorical column", all_cols, key="bar_x")
        y_col = st.selectbox("Select numeric column", numeric_cols, key="bar_y")
        fig, ax = plt.subplots()
        sns.barplot(x=df[x_col], y=df[y_col], ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    elif one_d_choice == "Pie Chart":
        col = st.selectbox("Select categorical column", all_cols, key="pie_col")
        pie_data = df[col].value_counts()
        fig, ax = plt.subplots()
        ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
        ax.axis("equal")
        st.pyplot(fig)

    elif one_d_choice == "Histogram":
        col = st.selectbox("Select numeric column", numeric_cols, key="hist_col")
        fig, ax = plt.subplots()
        sns.histplot(df[col], bins=20, kde=True, ax=ax)
        st.pyplot(fig)

    elif one_d_choice == "Box Plot":
        col = st.selectbox("Select numeric column", numeric_cols, key="box_col")
        fig, ax = plt.subplots()
        sns.boxplot(y=df[col], ax=ax)
        st.pyplot(fig)

    # ---------------- 2D VISUALIZATIONS ----------------
    st.header("2D Visualizations")

    two_d_choice = st.selectbox(
        "Choose a 2D plot:",
        ["Scatter Plot", "Line Plot", "Heatmap"]
    )

    if two_d_choice == "Scatter Plot" and len(numeric_cols) >= 2:
        x_col = st.selectbox("X-axis", numeric_cols, key="scatter_x")
        y_col = st.selectbox("Y-axis", numeric_cols, key="scatter_y")
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[x_col], y=df[y_col], ax=ax)
        st.pyplot(fig)

    elif two_d_choice == "Line Plot" and len(numeric_cols) >= 2:
        x_col = st.selectbox("X-axis", all_cols, key="line_x")
        y_col = st.selectbox("Y-axis", numeric_cols, key="line_y")
        fig, ax = plt.subplots()
        sns.lineplot(x=df[x_col], y=df[y_col], marker="o", ax=ax)
        st.pyplot(fig)

    elif two_d_choice == "Heatmap":
        fig, ax = plt.subplots(figsize=(6, 5))
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    # ---------------- 3D VISUALIZATIONS ----------------
    st.header("3D Visualizations")

    if len(numeric_cols) >= 3:
        three_d_choice = st.selectbox("Choose a 3D plot:", ["3D Scatter Plot"])

        if three_d_choice == "3D Scatter Plot":
            x_col = st.selectbox("X-axis", numeric_cols, key="3d_x")
            y_col = st.selectbox("Y-axis", numeric_cols, key="3d_y")
            z_col = st.selectbox("Z-axis", numeric_cols, key="3d_z")

            fig = plt.figure()
            ax = fig.add_subplot(111, projection="3d")
            ax.scatter(df[x_col], df[y_col], df[z_col], c='blue', s=50)
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            ax.set_zlabel(z_col)
            st.pyplot(fig)
    else:
        st.warning("Need at least 3 numeric columns for 3D plot.")
