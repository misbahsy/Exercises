class Employee:
    def __init__(self, name, employee_id, salary, years_at_company):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.years_at_company = years_at_company
    
def give_raises(employee_lst):
    for employee in employee_lst:
        if employee.years_at_company <= 5:
            employee.salary = employee.salary + 5000
        elif employee.years_at_company < 10:
            employee.salary = employee.salary + 8000
        if employee.years_at_company >= 10:
            employee.salary = employee.salary + 10000
