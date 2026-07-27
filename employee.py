from db import con, cursor

class Employee:

    def add_employee(self, name, gender, age, phone, email, department, designation, joining_date, basic_salary):
        query = """
        INSERT INTO employee
        (emp_name, gender, age, phone, email, department, designation, joining_date, basic_salary)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(query, (
            name,
            gender,
            age,
            phone,
            email,
            department,
            designation,
            joining_date,
            basic_salary
        ))
        con.commit()

    def view_employee(self):
        query = "SELECT * FROM employee"
        cursor.execute(query)
        return cursor.fetchall()

    def search_employee(self, search_value):
        query = "SELECT * FROM employee WHERE emp_id=%s OR emp_name=%s"
        cursor.execute(query, (search_value, search_value))
        return cursor.fetchall()

    def update_employee(self, emp_id, name, gender, age, phone, email,
                        department, designation, joining_date, basic_salary):

        query = """
        UPDATE employee
        SET emp_name=%s,
            gender=%s,
            age=%s,
            phone=%s,
            email=%s,
            department=%s,
            designation=%s,
            joining_date=%s,
            basic_salary=%s
        WHERE emp_id=%s
        """

        cursor.execute(query, (
            name,
            gender,
            age,
            phone,
            email,
            department,
            designation,
            joining_date,
            basic_salary,
            emp_id
        ))
        con.commit()

    def get_employee_by_id(self, emp_id):
        query = "SELECT * FROM employee WHERE emp_id=%s"
        cursor.execute(query, (emp_id,))
        return cursor.fetchone()

    def delete_employee(self, emp_id):
        cursor.execute("DELETE FROM attendance WHERE emp_id=%s", (emp_id,))
        cursor.execute("DELETE FROM employee WHERE emp_id=%s", (emp_id,))
        con.commit()

    def add_payroll(self, emp_id, month, year, basic_salary, hra, bonus,
                    overtime, pf, tax, net_salary):

        query = """
        INSERT INTO payroll
        (emp_id, month, year, basic_salary, hra, bonus,
         overtime, pf, tax, net_salary)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(query, (
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
        ))

        con.commit()

    def mark_attendance(self, emp_id, attendance_date, status):
        query = """
        INSERT INTO attendance
        (emp_id, attendance_date, status)
        VALUES (%s,%s,%s)
        """

        cursor.execute(query, (
            emp_id,
            attendance_date,
            status
        ))
        con.commit()