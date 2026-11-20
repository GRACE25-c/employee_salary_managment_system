from Employee import Employee      #import Employee class

class PermanentEmployee(Employee):   #child class 
    def  calculate_salary(self):
        total_salary=self.basic_salary+(self.basic_salary*0.2)    #total salary including allowence
        print("Permanent Employee Salary including allowence: ",total_salary)
        return total_salary   #return the total salary into the calculate_salary methord
    def display_details(self):  #created a display_details methord 
        print("Name: ",self.name)
        print("Id: ",self.id)
        print("Job Roll: ",self.roll)
        print("Work Mode: ",self.work_mode)
        print("Basic Salary: ",self.basic_salary)
