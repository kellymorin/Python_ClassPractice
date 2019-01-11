# Create a class that contains information about employees of a company and define methods to get/set employee name, job title, and start date.

class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = []

    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name

    def set_employee(self, employee):
        self.employees.append(employee)

    def get_employee_list(self):
        employee_names = []
        for employee in self.employees:
            employee_names.append(employee.employee_name)
        return (" & ").join(employee_names)

    def __str__(self):
        return f'{self.company_name} has {len(self.employees)} employees, they are {self.get_employee_list()}'

    # Add the remaining methods to fill the requirements above



# Create a class that contains information about employees of a company and define methods to get/set employee name, job title, and start date.

class Employee:
    def __init__(self, name, job_title, start_date):
        self.employee_name = name
        self.job_title = job_title
        self.start_date = start_date

    def get_employee_name(self):
        return self.employee_name

    def set_employee_name(self, name):
        self.employee_name = name

    def get_employee_job_title(self):
        return self.job_title

    def set_employee_job_title(self, job_title):
        self.job_title = job_title

    def get_employee_start_date(self):
        return self.start_date

    def set_employee_start_date(self, start_date):
        self.start_date = start_date

    def __str__(self):
        return f'{self.employee_name} works as {self.job_title} they started {self.start_date}'

abc_company = Company("ABC Company", "January 11, 2019")
sebastian = Employee("Sebastian Civarolo", "Penguin Sweater", "January 11, 2019")
abc_company.set_employee(sebastian)
print(abc_company)
kelly = Employee("Kelly Morin", "Founder & Chief Organizing Officer", "January 11, 2019")
abc_company.set_employee(kelly)
print(abc_company)
bryan = Employee("Bryan Nilsen", "Rock Star", "January 11, 2019")
abc_company.set_employee(bryan)
kelly.set_employee_name("Organizer")
print(abc_company)
