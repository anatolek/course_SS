# create a class Employee
class Employee(object):

    def __init__(self, fname, sname, salary, experiance):
        self.fname = fname
        self.sname = sname
        self.salary = salary
        self.experiance = experiance

    def get_salary(self):
        if self.experiance > 2:
            self.salary += 200
        elif self.experiance > 5:
            self.salary *= 1.2
            self.salary += 500


class Developer(Employee):
    pass


class Designer(Employee):
    pass


class Manager(Employee):
    pass
