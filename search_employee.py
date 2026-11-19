def search_employee(employees, emp_id):
    for employee in employees:
        if employee["id"] == emp_id:
            print("Employee Found")
            print(employee)
            return employee

    print("Employee not found")
    return None