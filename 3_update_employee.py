import streamlit as st
from employee import Employee

obj = Employee()

st.title("✏️ Update Employee")

emp_id = st.number_input("Enter Employee ID", min_value=1, step=1)

if st.button("Search"):
    emp = obj.get_employee_by_id(emp_id)

    if emp:
        st.session_state["emp"] = emp
    else:
        st.error("Employee not found")

if "emp" in st.session_state:
    emp = st.session_state["emp"]

    name = st.text_input("Name", emp[1])
    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"],
        index=["Male", "Female", "Other"].index(emp[2])
    )
    age = st.number_input("Age", value=int(emp[3]))
    phone = st.text_input("Phone", emp[4])
    email = st.text_input("Email", emp[5])
    department = st.text_input("Department", emp[6])
    designation = st.text_input("Designation", emp[7])
    joining_date = st.date_input("Joining Date", emp[8])
    basic_salary = st.number_input(
        "Basic Salary",
        value=float(emp[9]),
        step=100.0
    )

    if st.button("Update Employee"):
        obj.update_employee(
            emp_id,
            name,
            gender,
            age,
            phone,
            email,
            department,
            designation,
            joining_date,
            basic_salary
        )
        st.success("Employee Updated Successfully")