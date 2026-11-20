from Employee import Employee  #import perent class

class ContractEmployee(Employee):  #child class
    def  calculate_salary(self):  #polymorphisam  #same method but different functions
        total_salary=self.basic_salary+(self.basic_salary*0.05)  
        print("Contract Employee Salary including allowence: ",total_salary)
        return total_salary
    def display_details(self):          #same method but different functions
        print("Name: ",self.name)
        print("Id: ",self.id)
        print("Job Roll: ",self.roll)
        print("Work Mode: ",self.work_mode)
        print("Basic Salary: ",self.basic_salary)