import streamlit as st
from employee import Employee
from datetime import date

obj = Employee()

st.set_page_config(page_title="Attendance", page_icon="📅")

st.title("📅 Employee Attendance")

emp_id = st.number_input(
    "Employee ID",
    min_value=1,
    step=1
)

attendance_date = st.date_input(
    "Attendance Date",
    value=date.today()
)

status = st.selectbox(
    "Status",
    ["Present", "Absent", "Leave"]
)

if st.button("Mark Attendance"):

    emp = obj.search_employee(emp_id)

    if emp:
        obj.mark_attendance(emp_id, attendance_date, status)
        st.success("Attendance Marked Successfully ✅")
    else:
        st.error("Employee ID Not Found ❌")