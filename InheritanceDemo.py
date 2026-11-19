class Employee:
    def __init__(self, emp_id, name, designation):
        self.emp_id = emp_id
        self.name = name
        self.designation = designation
 
    def display_info(self):
        print(f"ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Designation: {self.designation}")
 
 
class Manager(Employee):
    def __init__(self, emp_id, name, designation, team_members, team_name):
        super().__init__(emp_id, name, designation)
        self.team_members = team_members
        self.team_name = team_name
 
    def display_info(self):
        super().display_info()
        print(f"Number of Team Members: {self.team_members}")
        print(f"Team Name: {self.team_name}")
 
 
class Developer(Employee):
    def __init__(self, emp_id, name, designation, project_title):
        super().__init__(emp_id, name, designation)
        self.project_title = project_title
 
    def display_info(self):
        super().display_info()
        print(f"Project Title: {self.project_title}")
 
 
m1 = Manager(101, "Raam", "Manager", 8, "Alpha Team")
m1.display_info()
 
print()
 
d1 = Developer(102, "neha", "Developer", "Payroll App")
d1.display_info()