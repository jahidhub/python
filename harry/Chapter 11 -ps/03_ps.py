"""Create a
class ‘Employee’
and add
salary and
increment
properties to it.

Write a method
‘salaryAfterIncrement’ method with a @property decorator with a
setter
which changes the value of
increment based on the salary."""


class Employee:
    # salary = 5000
    # increment = 20
    
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self.increment) / 100

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self.increment = (new_salary / self.salary - 1) * 100

        # new salary =  old salary ( 1+ increment/100)
        # (new salary/old salary -1) * 100 = increment


e = Employee(18000, 20)
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 18000
print(f"{e.increment} %")
