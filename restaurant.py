from menu import Menu


class Restaurant:
    def __init__(self,name):
        self.name=name
        self.employees=[]
        self.menu=Menu()



    def add_employee(self,emp):
        self.employees.append(emp)


    def view_employee(self):
            print("Employee List!")
            for emp in self.employees:
                print(emp.name, emp.email, emp.phone, emp.address)