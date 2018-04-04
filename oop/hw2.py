class Department(object):
    def __init__(self, dname):
        self.dname = dname
        self.managers = []

    def add_manager(self, manager):
        self.managers.append(manager)

    def give_salary(self, worker):
        """Message for each employee when he is given a salary:
        '@firstName@ @secondName@: got salary: @salaryValue@'"""
        print('{} {} got salary: ${:.2f}'.format(worker.fname, worker.sname, worker.get_salary()))


class Employee(object):
    def __init__(self, fname, sname, salary=500., experiance=0):
        """Each employee must have a first and a second name.
        The minimum salary in the company is 500$."""
        self.fname = fname
        self.sname = sname
        self.salary = salary
        self.experiance = experiance

    def get_salary(self):
        """If experiance is > 2 years => salary + 200$, > 5 years => salary*1.2 + 500$"""
        if self.experiance > 2:
            return self.salary + 200
        elif self.experiance > 5:
            return self.salary*1.2 + 500
        else:
            return self.salary

    def __repr__(self):
        """Representation in the form
        '@firstName@ @secondName@, manager:@manager secondName@, experiance:@experiance@'"""
        # return '{} {}, manager:{}, experiance: {}'.format(self.fname, self.sname, self.experiance)
        return '{} {}, experiance: {}'.format(self.fname, self.sname, self.experiance)


class Manager(Employee):
    def __init__(self, fname, sname, salary, experiance):
        Employee.__init__(self, fname, sname, salary, experiance)
        self.members = []

    def add_member(self, *members):
        for i in members:
            self.members.append(i)

    def get_salary(self):
        self.salary = Employee.get_salary(self)
        """Each manager gets salary:
        200$ if his team has >5 members
        300$ if his team has >10 members"""
        if len(self.members) > 5:
            self.salary += 200
        elif len(self.members) > 10:
            self.salary += 300
        """If more than half of team members are developers => salary*1.1"""
        # {x for i in isinstance(self.mambers(i), Developer)}
        if len(self.members)//2 < 5: # 5 have to be changed later
            return self.salary * 1.1
        else:
            return self.salary


class Developer(Employee):
    """Each developer has a manager"""
    def __init__(self, fname, sname, salary, experiance):
        Employee.__init__(self, fname, sname, salary, experiance)

    def get_salary(self):
        return Employee.get_salary(self)


class Designer(Employee):
    """Each designer has a manager.
    If the designer did the work well, he gets a full salary (effCoeff = 1)"""
    def __init__(self, fname, sname, salary, experiance, effCoeff=1.0):
        Employee.__init__(self, fname, sname, salary, experiance)
        self.effCoeff = effCoeff

    def get_salary(self):
        self.test_var = Employee.get_salary(self)
        return self.test_var * self.effCoeff


# ------ TESTING ------ #
des_tony = Designer('Tony', 'Gold', 500, 1, 0.9)
dev_mark = Developer('Mark', 'Silver', 1000, 2)
man_tina = Manager('Tina', 'Stone', 1200, 3)

# add employees to manager team
man_tina.add_member(des_tony, dev_mark)

# add managers to department
ss = Department('SoftServe')
ss.add_manager(man_tina)

# employee salary
print(des_tony.get_salary())
print(dev_mark.get_salary())
print(man_tina.get_salary())

# department give a salary to each employee
ss.give_salary(des_tony)
ss.give_salary(dev_mark)
ss.give_salary(man_tina)
