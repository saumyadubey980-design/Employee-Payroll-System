import streamlit as st
import pandas as pd
from employee import Employee

obj = Employee()

st.title("👨‍💼 View Employees")

search = st.text_input("🔍 Search by Employee ID or Name")

if search:
    data = obj.search_employee(search)
else:
    data = obj.view_employee()

if data:
    df = pd.DataFrame(
        data,
        columns=[
            "ID",
            "Name",
            "Gender",
            "Age",
            "Phone",
            "Email",
            "Department",
            "Designation",
            "Joining Date",
            "Basic Salary"
        ]
    )

    st.dataframe(df, use_container_width=True)
else:
    st.warning("No Employee Found")