class Department(object):
    def __init__(self, dname):
        self.dname = dname
        self.managers = []

    def add_manager(self, manager):
        self.managers.append(manager)

    @staticmethod
    def give_salary(worker):
        """Message for each employee when he is given a salary:
        '@firstName@ @secondName@: got salary: @salaryValue@'"""
        print('{} {} got salary: ${:.2f}'.format(worker.fname, worker.sname, worker.get_salary()))


class Employee(object):
    def __init__(self, fname, sname, salary=500., experiance=0.):
        """Each employee must have a first and a second name.
        The minimum salary in the company is 500$."""
        self.fname = fname
        self.sname = sname
        self.salary = salary
        self.experiance = experiance

    def get_salary(self):
        """If experiance is > 2 years => salary + 200$, > 5 years => salary*1.2 + 500$"""
        if self.experiance > 5:
            return self.salary*1.2 + 500.
        elif self.experiance > 2:
            return self.salary + 200.
        else:
            return float(self.salary)

    def __repr__(self):
        """Representation in the form
        '@firstName@ @secondName@, manager:@manager secondName@, experiance:@experiance@'"""
        # return '{} {}, manager:{}, experiance: {}'.format(self.fname, self.sname, self.experiance)
        return '{} {}, experiance: {}'.format(self.fname, self.sname, self.experiance)


class Manager(Employee):
    def __init__(self, fname, sname, salary, experiance):
        Employee.__init__(self, fname, sname, salary, experiance)
        self.members = {'num_members': 0}

    def add_member(self, *workers):
        """Create dictionary members =>
        {@name of the first class of employees@: [member1, member2, ...],
        @name of the second class of employees@: [member1, member2, ...],
        ...,
        'num_members': @number of members@}"""
        for i in workers:
            _cls = i.__class__.__name__
            if self.members.__contains__(_cls):
                self.members[_cls].append(i)
            else:
                self.members[_cls] = [i]
            self.members['num_members'] += 1

    def get_salary(self):
        self.msalary = Employee.get_salary(self)
        """Each manager gets salary:
        200$ if his team has >5 members
        300$ if his team has >10 members"""
        if self.members['num_members'] > 10:
            self.msalary += 300
        elif self.members['num_members'] > 5:
            self.msalary += 200
        """If more than half of team members are developers => salary*1.1"""
        if self.members['num_members']//2 < len(self.members['Developer']):
            return self.msalary * 1.1
        else:
            return self.msalary


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
        return Employee.get_salary(self) * self.effCoeff


# ------ TESTING ------ #
des_tony = Designer('Tony', 'Gold', 500, 1, .9)
dev_mark = Developer('Mark', 'Silver', 1000, 2)
dev_mina = Developer('Mina', 'Iron', 3000, 6)
man_tina = Manager('Tina', 'Stone', 1200, 3)

# add employees to manager team
man_tina.add_member(des_tony, dev_mark, dev_mina)

# add managers to department
ss = Department('SoftServe')
ss.add_manager(man_tina)

# employee salary
print('Salary: {:.2f}'.format(des_tony.get_salary()))
print('Salary: {:.2f}'.format(dev_mark.get_salary()))
print('Salary: {:.2f}'.format(dev_mina.get_salary()))
print('Salary: {:.2f}'.format(man_tina.get_salary()))

# department give a salary to each employee
ss.give_salary(des_tony)
ss.give_salary(dev_mark)
ss.give_salary(dev_mina)
ss.give_salary(man_tina)
