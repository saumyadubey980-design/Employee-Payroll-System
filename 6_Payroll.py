import streamlit as st
from employee import Employee

obj = Employee()

st.set_page_config(page_title="Payroll", page_icon="💰")

st.title("💰 Employee Payroll")

emp_id = st.number_input("Employee ID", min_value=1, step=1)

month = st.selectbox(
    "Month",
    ["January","February","March","April","May","June",
     "July","August","September","October","November","December"]
)

year = st.number_input("Year", min_value=2024, value=2026)

basic_salary = st.number_input("Basic Salary", min_value=0.0)

hra = st.number_input("HRA", min_value=0.0)

bonus = st.number_input("Bonus", min_value=0.0)

overtime = st.number_input("Overtime", min_value=0.0)

pf = st.number_input("PF", min_value=0.0)

tax = st.number_input("Tax", min_value=0.0)

gross_salary = basic_salary + hra + bonus + overtime
net_salary = gross_salary - pf - tax

st.info(f"Gross Salary : ₹{gross_salary:.2f}")
st.success(f"Net Salary : ₹{net_salary:.2f}")

if st.button("Save Payroll"):

    emp = obj.search_employee(emp_id)

    if emp:
        obj.add_payroll(
            emp_id,
            month,
            year,
            basic_salary,
            hra,
            bonus,
            overtime,
            pf,
            tax,
            net_salary
        )

        st.success("Payroll Saved Successfully ✅")

    else:
        st.error("Employee ID Not Found ❌")