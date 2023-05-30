#Dawn Smith
#Burger Order

import random

lst_asCustomer = ["Jefe","El Guapo","Lucky Day","Ned Nederlander","Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman","Singing Bush"]

class Order :
    def __init__(self) :
        self.burger_count = self.randomBurgers()
       
    def randomBurgers(self):
        return random.randint(1,20)
        

    
class Person :
    def __init__(self) :
        self.name = self.randomName()


    def randomName (self):
        return random.choice(lst_asCustomer)
        
        

class Customer (Person):
       def __init__(self):
        super(). __init__() 
        self.myOrder = Order()
   
        
        
queueCustomer = []    
dictCustomer = {}    
   

for iCount in range (100):
    queueCustomer.append(Customer())

for customer in queueCustomer:
    #print(customer.name,customer.myOrder.burger_count)
    if customer.name in dictCustomer : 
        dictCustomer[customer.name] += customer.myOrder.burger_count
    else:
        dictCustomer[customer.name] = customer.myOrder.burger_count


for qCustomer in range (len(queueCustomer)):
    queueCustomer.pop(0)


#print(dictCustomer)
# You can use a statement similar to: listSortedCustomers = sorted(dictCustomers.items(), key=lambda x: x[1], reverse=True) 
listSortedCustomers = sorted(dictCustomer.items(), key=lambda x:x[1],reverse=True)

print("\n") 
#print(listSortedCustomers)

for customer in listSortedCustomers :
    custName = customer [0]
    iBurgerCount = customer [1]
    print ((custName).ljust(30) + str(iBurgerCount) + "\n")


#print(queueCustomer)