import streamlit as st
import pandas as pd

st.title("🧹 Data Cleaner App")
st.markdown("**Mr MorningStar**")

# 

# File uploader
uploaded_file = st.file_uploader("Upload your dataset (CSV or Excel)", type=["csv", "xlsx"])

if uploaded_file:
    # Read the file
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("📊 Raw Data Preview")
    st.dataframe(df.head())

    st.subheader("🧹 Cleaning Options")
    remove_dupes = st.checkbox("Remove Duplicates")
    drop_nulls = st.checkbox("Drop Rows with Missing Values")
    fill_nulls = st.checkbox("Fill Missing Values (with 0)")
    lower_colnames = st.checkbox("Convert Column Names to Lowercase")

    if st.button("Clean Data"):
        cleaned_df = df.copy()

        if remove_dupes:
            cleaned_df = cleaned_df.drop_duplicates()

        if drop_nulls:
            cleaned_df = cleaned_df.dropna()
        elif fill_nulls:
            cleaned_df = cleaned_df.fillna(0)

        if lower_colnames:
            cleaned_df.columns = [col.lower() for col in cleaned_df.columns]

        st.success("✅ Data Cleaned Successfully")
        st.dataframe(cleaned_df.head())

        # Download cleaned data
        st.download_button("📥 Download Cleaned Data as CSV", 
                           data=cleaned_df.to_csv(index=False), 
                           file_name="cleaned_data.csv",
                           mime="text/csv")
