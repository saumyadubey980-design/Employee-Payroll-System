_mport streamlit as st
from employee import Employee

obj = Employee()

st.set_page_config(page_title="Delete Employee", page_icon="🗑️")

st.title("🗑️ Delete Employee")

emp_id = st.number_input(
    "Enter Employee ID",
    min_value=1,
    step=1
)

if st.button("Delete Employee"):

    emp = obj.get_employee_by_id(emp_id)

    if emp:
        obj.delete_employee(emp_id)
        st.success("Employee Deleted Successfully ✅")
    else:
        st.error("Employee ID Not Found ❌")