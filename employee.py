"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contracttype, contractnum, commissiontype, hours):
        self.name = name
        pay = 0
        self.contracttype = contracttype
        self.contractnum = contractnum
        self.commissiontype = commissiontype
        self.hours = hours
    

    #input value based on type of contract type
    def paywage(self, value):
        
        if self.contracttype == "salary":

            pay += value

        
        if self.contracttype == "hourly":

            pay += (self.hours * value)
        
        else:
            pass


    #assign value based on the specific 

    def paycommission(self, value):
        
        if self.commissiontype == "fixed":
            pay += value

        
        if self.commissiontype == "contract":

            pay += (self.contractnum * value)


        else:
            pass

    def get_pay(self):


        return self.pay
        

       




    def __str__(self):
        return self.name




# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "salary", 0, "unknown", 50)



# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "hourly", 0, "unknown", 100  )

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
