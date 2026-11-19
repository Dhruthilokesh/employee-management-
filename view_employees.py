def view_employees(employees):
    if not employees:
        print("No employees found")
        return

    print("\nEmployee List")

    for employee in employees:
        print(employee["id"], employee["name"], employee["department"])