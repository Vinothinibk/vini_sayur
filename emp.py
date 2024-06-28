class employee:
    def __init__(self,name,designation,salary):
        self.name=name
        self.designation=designation
        self.salary=salary
        self.manager=None

def print_employee(emp):
    print(f"emp name={emp.name}")
    print(f"emp designation={emp.designation}")
    print(f"emp salary={emp.salary}")
   

emp1=employee("bharathi","software engineer",70000)
emp2=employee("kannan","Team lead",80000)
emp3=employee("vinothini","junior software engineer",50000)
emp4=employee("sahithyan","ceo",300000)

emp1.manager=emp2
emp3.manager=emp2
emp2.manager=emp4

emp_list=[emp1,emp2,emp3,emp4]
for each_emp in emp_list:
    while each_emp != None:   
        print_employee(each_emp)
        each_emp = each_emp.manager
    print('\n')
