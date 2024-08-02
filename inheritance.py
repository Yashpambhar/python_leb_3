class company:
    def _init_(self, name, city, mobile_no):
        self.name = name
        self.city = city
        self.mobile_no = mobile_no

class employee(company):
    def _init_(self, name, city, mobile_no, emp_name, designation, salary):
        super()._init_(name, city, mobile_no)
        self.emp_name = emp_name
        self.designation = designation
        self.salary = salary

emp = employee("ABC Company", "New York", "1234567890", "John Doe", "Manager", 50000)

print(emp.name)
print(emp.city)
print(emp.mobile_no)
print(emp.emp_name)
print(emp.designation)
print(emp.salary)
