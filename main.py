from PermanentEmployee import PermanentEmployee   #import the PermenentEmpolyee class

permanentemployee=PermanentEmployee("Grace Jacob","GH1234","Web Developer","Permenent Employee",500000) #created object for PermenentEmployee  class 
permanentemployee.display_details() #call display details methord
permanentemployee.calculate_salary() #call calculate salary methord



#output
# Name:  Grace Jacob
# Id:  GH1234
# Job Roll:  Web Developer
# Work Mode:  Permenent Employee
# Basic Salary:  500000
# Permanent Employee Salary including allowence:  600000.0



from ContractEmployee import ContractEmployee  #imported the ContractEmployee class
contractemployee=ContractEmployee("Nice Jacob","CHG1002","Web Developer","Contract Employee",200000)  #create object for ContractEmployee
contractemployee.display_details()   #call display details
contractemployee.calculate_salary()   #call calculate salary


#output
# Name:  Nice Jacob
# Id:  CHG1002
# Job Roll:  Web Developer
# Work Mode:  Contract Employee
# Basic Salary:  200000
# Contract Employee Salary including allowence:  210000.0