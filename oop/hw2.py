# create a class Employee
class Employee(object):
    def __init__(self, fname, sname, salary, experiance):
        self.fname = fname
        self.sname = sname
        self.salary = salary
        self.experiance = experiance

    def get_salary(self):
        if self.experiance > 2:
            return self.salary + 200
        elif self.experiance > 5:
            return self.salary*1.2 + 500

    def __repr__(self):
        #return '{} {}, manager:{}, experiance: {}'.format(self.fname, self.sname, self.experiance)
        return '{} {}, experiance: {}'.format(self.fname, self.sname, self.experiance)


class Developer(Employee):
    def __init__(self, fname, sname, salary, experiance, manager):
        Employee.__init__(self, fname, sname, salary, experiance)
        self.manager = manager


class Designer(Employee):
    def __init__(self, fname, sname, salary, experiance, manager, effCoeff):
        Employee.__init__(self, fname, sname, salary, experiance)
        self.manager = manager
        self.effCoeff = effCoeff

    def get_salary(self):
        return self.salary * self.effCoeff


class Manager(Employee):
    def __init__(self, fname, sname, salary, experiance, manager, members):
        Employee.__init__(self, fname, sname, salary, experiance)
        #self.manager = manager
        #self.members = members

    def get_salary(self):
        if self.members > 5:
            self.salary += 200
        elif self.members > 10:
            self.salary += 300
            # if self.members//2 < developers:
            #     return self.salary * 1.1


class Department(object):
    pass