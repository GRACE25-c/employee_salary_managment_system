from Employee import Employee

class PermanentEmployee(Employee):
    def  calculate_salary(self):
        total_salary=self.basic_salary+(self.basic_salary*0.2)
        print("Permanent Employee Salary including allowence: ",total_salary)
        return total_salary
    def display_details(self):
        print("Name: ",self.name)
        print("Id: ",self.id)
        print("Job Roll: ",self.roll)
        print("Work Mode: ",self.work_mode)
        print("Basic Salary: ",self.basic_salary)
