# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import altair as alt
# import time

# # 🌟 Streamlit Page Configuration
# st.set_page_config(
#     page_title="Data sweeper",
#     page_icon="📊",
#     layout="wide"
# )
# st.title("Data Sweeper")
# st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization!")

# # 🌟 Dark Mode Toggle
# dark_mode = st.sidebar.checkbox("🌙 Enable Dark Mode")

# # 🌟 Apply Theme Configuration
# if dark_mode:
#     st.markdown("""
#         <style>
#         body, .stApp {
#             background-color: #121212 !important;
#             color: #ffffff !important;
#         }
#         .css-1d391kg, .css-18e3th9, .stButton > button {
#             background-color: #1e1e1e !important;
#             color: #ffffff !important;
#             border: 1px solid #bb86fc !important;
#         }
#         .stTextInput > div > div > input {
#             background-color: #1e1e1e !important;
#             color: #ffffff !important;
#         }
#         .stSelectbox > div > div > select {
#             background-color: #1e1e1e !important;
#             color: #ffffff !important;
#         }
#         </style>
#     """, unsafe_allow_html=True)
# else:
#     st.markdown("""
#         <style>
#         body, .stApp {
#             background-color: #ffffff !important;
#             color: #000000 !important;
#         }
#         .css-1d391kg, .css-18e3th9, .stButton > button {
#             background-color: #f0f2f6 !important;
#             color: #000000 !important;
#             border: 1px solid #ccc !important;
#         }
#         .stTextInput > div > div > input {
#             background-color: #ffffff !important;
#             color: #000000 !important;
#         }
#         .stSelectbox > div > div > select {
#             background-color: #ffffff !important;
#             color: #000000 !important;
#         }
#         </style>
#     """, unsafe_allow_html=True)

# # 💂️ Sidebar for File Upload
# st.sidebar.title("📂 Upload Your File")
# uploaded_file = st.sidebar.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

# if uploaded_file:
#     # 🌊 Read File
#     with st.spinner("📂 Processing File..."):
#         file_extension = uploaded_file.name.split(".")[-1]
#         try:
#             if file_extension == "csv":
#                 df = pd.read_csv(uploaded_file, encoding='latin1')
#             else:
#                 import openpyxl
#                 df = pd.read_excel(uploaded_file)
#         except ImportError:
#             st.error("❌ Missing optional dependency 'openpyxl'. Please install it using `pip install openpyxl`.")
#             st.stop()
#         time.sleep(1)

#     st.success("✅ File Successfully Uploaded!")

#     # 🎯 Data Overview
#     st.write("### 👋 Data Overview")
#     st.write(df.head())

#     # 🚀 Data Cleaning Options
#     st.sidebar.subheader("🛠 Data Cleaning")
#     fill_na = st.sidebar.checkbox("Fill Missing Values")
#     remove_duplicates = st.sidebar.checkbox("Remove Duplicate Rows")
    
#     if fill_na:
#         df.fillna("N/A", inplace=True)  # Replace missing values with 'N/A'
#         st.sidebar.success("✅ Missing Values Filled")
    
#     if remove_duplicates:
#         df.drop_duplicates(inplace=True)
#         st.sidebar.success("✅ Duplicate Rows Removed")

#     # 🎨 Data Visualization
#     st.write("## 📊 Data Visualization")

#     col1, col2 = st.columns(2)

#     # 📈 Plotly Chart
#     with col1:
#         st.subheader("📈 Plotly Interactive Chart")
#         numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
#         if len(numeric_columns) > 1:
#             x_axis = st.selectbox("Choose X-axis", numeric_columns, key="plotly_x")
#             y_axis = st.selectbox("Choose Y-axis", numeric_columns, key="plotly_y")
#             if x_axis in df.columns and y_axis in df.columns:
#                 fig = px.scatter(df, x=x_axis, y=y_axis, color=df.columns[1] if len(df.columns) > 1 else None)
#                 st.plotly_chart(fig, use_container_width=True)

#     # 📊 Altair Chart (Fixed)
#     with col2:
#         st.subheader("📊 Altair Chart")
#         categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
        
#         if len(numeric_columns) > 1:
#             x_axis = st.selectbox("Choose X-axis for Altair", numeric_columns, key="altair_x")
#             y_axis = st.selectbox("Choose Y-axis for Altair", numeric_columns, key="altair_y")
#             color_column = st.selectbox("Choose Color Column", [None] + categorical_columns, key="altair_color")

#             if not x_axis or not y_axis:
#                 st.warning("⚠️ Please select valid X-axis and Y-axis columns!")
#             else:
#                 if color_column and color_column in df.columns:
#                     df[color_column] = df[color_column].astype(str).fillna("Unknown")
#                 else:
#                     color_column = None

#                 chart = alt.Chart(df).mark_circle(size=60).encode(
#                     x=alt.X(x_axis, type="quantitative", title=x_axis),
#                     y=alt.Y(y_axis, type="quantitative", title=y_axis),
#                     color=alt.Color(color_column, type="nominal", title=color_column) if color_column else alt.value("gray"),
#                     tooltip=[x_axis, y_axis] + ([color_column] if color_column else [])
#                 ).interactive()

#                 st.altair_chart(chart, use_container_width=True)

#     # 🛠 Download Cleaned Data
#     st.sidebar.subheader("⬇️ Download Processed Data")
#     def convert_df(df):
#         return df.to_csv(index=False).encode("utf-8")

#     csv = convert_df(df)
#     st.sidebar.download_button("📝 Download Cleaned CSV", csv, "cleaned_data.csv", "text/csv")

#     st.success("🎉 All set! Your data is cleaned and visualized.")
# else:
#     st.info("📂 Please upload a CSV or Excel file to get started.")

import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import time
import io

# 🌟 Streamlit Page Configuration
st.set_page_config(
    page_title="Data Sweeper",
    page_icon="📊",
    layout="wide"
)
st.title("Data Sweeper")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization!")

# 🌟 Dark Mode Toggle
dark_mode = st.sidebar.checkbox("🌙 Enable Dark Mode")

# 🌟 Apply Theme Configuration
if dark_mode:
    st.markdown("""
        <style>
        body, .stApp {
            background-color: #121212 !important;
            color: #ffffff !important;
        }
        </style>
    """, unsafe_allow_html=True)

# 💂️ Sidebar for File Upload
st.sidebar.title("📂 Upload Your File")
uploaded_file = st.sidebar.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    # 🌊 Read File
    with st.spinner("📂 Processing File..."):
        file_extension = uploaded_file.name.split(".")[-1]
        try:
            if file_extension == "csv":
                df = pd.read_csv(uploaded_file, encoding='latin1')
            else:
                df = pd.read_excel(uploaded_file)
        except ImportError:
            st.error("❌ Missing optional dependency 'openpyxl'. Please install it using `pip install openpyxl`.")
            st.stop()
        time.sleep(1)

    st.success("✅ File Successfully Uploaded!")

    # 🎯 Data Overview
    st.write("### 👋 Data Overview")
    st.write(df.head())

    # 🚀 Data Cleaning Options
    st.sidebar.subheader("🛠 Data Cleaning")
    fill_na = st.sidebar.checkbox("Fill Missing Values")
    remove_duplicates = st.sidebar.checkbox("Remove Duplicate Rows")
    
    if fill_na:
        df.fillna("N/A", inplace=True)
        st.sidebar.success("✅ Missing Values Filled")
    
    if remove_duplicates:
        df.drop_duplicates(inplace=True)
        st.sidebar.success("✅ Duplicate Rows Removed")

    # 🎨 Data Visualization
    st.write("## 📊 Data Visualization")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 Plotly Interactive Chart")
        numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
        if len(numeric_columns) > 1:
            x_axis = st.selectbox("Choose X-axis", numeric_columns, key="plotly_x")
            y_axis = st.selectbox("Choose Y-axis", numeric_columns, key="plotly_y")
            fig = px.scatter(df, x=x_axis, y=y_axis, color=df.columns[1] if len(df.columns) > 1 else None)
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("📊 Altair Chart")
        categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
        
        if len(numeric_columns) > 1:
            x_axis = st.selectbox("Choose X-axis for Altair", numeric_columns, key="altair_x")
            y_axis = st.selectbox("Choose Y-axis for Altair", numeric_columns, key="altair_y")
            color_column = st.selectbox("Choose Color Column", [None] + categorical_columns, key="altair_color")

            if not x_axis or not y_axis:
                st.warning("⚠️ Please select valid X-axis and Y-axis columns!")
            else:
                if color_column and color_column in df.columns:
                    df[color_column] = df[color_column].astype(str).fillna("Unknown")
                else:
                    color_column = None

                chart = alt.Chart(df).mark_circle(size=60).encode(
                    x=alt.X(x_axis, type="quantitative", title=x_axis),
                    y=alt.Y(y_axis, type="quantitative", title=y_axis),
                    color=alt.Color(color_column, type="nominal", title=color_column) if color_column else alt.value("gray"),
                    tooltip=[x_axis, y_axis] + ([color_column] if color_column else [])
                ).interactive()

                st.altair_chart(chart, use_container_width=True)

    # 🛠 File Conversion
    st.sidebar.subheader("🔄 Convert File Format")
    convert_option = st.sidebar.radio("Convert to:", ("CSV", "Excel (.xlsx)"))

    def convert_file(df, file_type):
        buffer = io.BytesIO()
        if file_type == "csv":
            df.to_csv(buffer, index=False)
            return buffer.getvalue(), "text/csv", "converted_data.csv"
        else:
            with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='Sheet1')
            return buffer.getvalue(), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "converted_data.xlsx"

    file_data, mime_type, file_name = convert_file(df, "csv" if convert_option == "CSV" else "xlsx")
    st.sidebar.download_button(f"⬇️ Download {convert_option}", file_data, file_name, mime_type)
    
    st.success("🎉 All set! Your data is cleaned, visualized, and ready for download.")
else:
    st.info("📂 Please upload a CSV or Excel file to get started.")
