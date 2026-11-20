from abc import ABC,abstractmethod
class Employee(ABC):  #this is a perent class
    #polymorphisam
    @abstractmethod
    def  calculate_salary(self):  #this is an abstraction methode . in this methord we dont code anything. jest for define a methord
        pass                       # pass will help to escape from errors
        #polymorphisam
    def display_details(self):     # this is not an abstract metord . jest for define a methord
        pass                        # pass will help to escape from errors
    def __init__(self,name,id,roll,work_mode,basic_salary):
        self.name=name
        self.id=id
        self.roll=roll
        self.work_mode=work_mode
        self.__basic_salary=basic_salary  #private
        #encapsulation###
    @property                                                #convert  privet atribute into property. property means 
                                                            #the data can't modify but we can display where we want
    def basic_salary(self):                
        return self.__basic_salary

        