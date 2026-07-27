import streamlit as st
from employee import Employee

obj = Employee()

st.set_page_config(
    page_title="Employee Payroll Management",
    page_icon="💼",
    layout="wide"
)

# Sidebar menu
st.sidebar.title("💼 Payroll Menu")
page = st.sidebar.radio(
    "Go to",
    ["Dashboard", "Employees", "Reports"]
)

# ---- Dashboard Page ----
if page == "Dashboard":
    # Custom title using HTML/CSS
    st.markdown("""
        <h1 style="color:#4B4BFF; text-align:center;">
            🧾 Employee Payroll Management
        </h1>
    """, unsafe_allow_html=True)

    # Welcome box
    st.markdown("""
        <div style="background-color:#F0F2F6; padding:15px; border-radius:10px; text-align:center;">
            <h4 style="color:#333;">Welcome, Admin 👋</h4>
        </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ---- Pull real data from database ----
    data = obj.view_employee()
    total_employees = len(data)
    total_payroll = sum(row[9] for row in data)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
            <div style="background-color:#E8F0FE; padding:20px; border-radius:10px; text-align:center;">
                <h5 style="color:#000000;">Total Employees</h5>
                <h2 style="color:#4B4BFF;">{total_employees}</h2>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div style="background-color:#E6FCE9; padding:20px; border-radius:10px; text-align:center;">
                <h5 style="color:#000000;">Total Payroll</h5>
                <h2 style="color:#2E8B57;">₹{total_payroll:,.0f}</h2>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div style="background-color:#FFF4E5; padding:20px; border-radius:10px; text-align:center;">
                <h5 style="color:#000000;">Departments</h5>
                <h2 style="color:#CC7A00;">5</h2>
            </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.info("Use the sidebar to navigate between sections.")

# ---- Employees Page ----
elif page == "Employees":
    st.markdown("<h1 style='color:#4B4BFF;'>👥 Employees</h1>", unsafe_allow_html=True)
    st.write("Your employee table/form goes here")

# ---- Reports Page ----
elif page == "Reports":
    st.markdown("<h1 style='color:#4B4BFF;'>📊 Reports</h1>", unsafe_allow_html=True)
    st.write("Your charts/reports go here")