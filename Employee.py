class Employee:
    def __init__(self, name, date_of_join, designation, salary):
        self.name = name
        self.date_of_join = date_of_join
        self.designation = designation
        self.salary = salary

employee1 = Employee("John Doe", "2022-01-01", "Manager", 50000)
employee2 = Employee("Jane Smith", "2022-02-15", "Developer", 40000)

print("Employee 1 Information:")
print("Name:", employee1.name)
print("Date of Join:", employee1.date_of_join)
print("Designation:", employee1.designation)
print("Salary:", employee1.salary)

print("\nEmployee 2 Information:")
print("Name:", employee2.name)
print("Date of Join:", employee2.date_of_join)
print("Designation:", employee2.designation)
print("Salary:", employee2.salary)

output :-
![pro1](https://github.com/user-attachments/assets/0d9fb83f-0ebf-42fa-9b22-d517037e1dbc)
