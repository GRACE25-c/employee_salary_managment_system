from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def  calculate_salary(self):
        pass
    def display_details(self):
        pass
    def __init__(self,name,id,roll,work_mode,basic_salary):
        self.name=name
        self.id=id
        self.roll=roll
        self.work_mode=work_mode
        self.__basic_salary=basic_salary  #private
    @property
    def basic_salary(self):
        return self.__basic_salary

        