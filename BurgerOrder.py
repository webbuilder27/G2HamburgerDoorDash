"""Doordash Hamburger Team 2 Project
Dawn Smith
Kaden Cheshire
Emma Coles
Sean Watson
Elijah Aken
Lelanie (Eliza) Tuinei
"""
#This program creates customer orders of boogers and sorts them in an descending order.

#We left print statments in that we used to test our code and just commented them out after.

#Don't forget to import the random module
import random


#list was provided from the homework assingment
lst_asCustomer = ["Jefe","El Guapo","Lucky Day","Ned Nederlander","Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman","Singing Bush"]

#Make a class of orders, these people need to eat less burgers.
class Order :
    def __init__(self) :
        self.burger_count = self.randomBurgers()
        
    #make a method to return random number of burgers. wow!   
    def randomBurgers(self):
        return random.randint(1,20)
        

 #Make a person class.
class Person :
    def __init__(self) :
        self.name = self.randomName()

    #method to pick a random name from a list of nine names.
    def randomName (self):
        return random.choice(lst_asCustomer)
        
        
#Customer class inherits from person class. Be sure to use the SUPER () constructor
class Customer (Person):
       def __init__(self):
        super(). __init__() 
        self.myOrder = Order()
   
        
#Create variable for empty Customer queue out side of the class.
#create variable for the dictionary.
queueCustomer = []    
dictCustomer = {}    
   
#append 100 customers to the queue
for iCount in range (100):
    queueCustomer.append(Customer())

 #take customers from the queue and add them and their burger count to the dictionary. If the name exists only add more burgers.
for customer in queueCustomer:
    #print(customer.name,customer.myOrder.burger_count)
    if customer.name in dictCustomer : 
        dictCustomer[customer.name] += customer.myOrder.burger_count
    else:
        dictCustomer[customer.name] = customer.myOrder.burger_count

#This is where we remove each customer from the queue after they order extraordinary amounts of boogers.
for qCustomer in range (len(queueCustomer)):
    queueCustomer.pop(0)


#print(dictCustomer)
# You can use a statement similar to: listSortedCustomers = sorted(dictCustomers.items(), key=lambda x: x[1], reverse=True) 
listSortedCustomers = sorted(dictCustomer.items(), key=lambda x:x[1],reverse=True)

#The pring('\n') adds space so that it prints prettier.
print("\n") 
#print(listSortedCustomers)

#This prints the customers along with their burger totals.
for customer in listSortedCustomers :
    custName = customer [0]
    iBurgerCount = customer [1]
    print ((custName).ljust(30) + str(iBurgerCount) + "\n")


#print(queueCustomer)
