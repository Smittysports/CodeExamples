# Main.py

# import allows modules (files containing Python definitions and statements) to be used
from Test import Person
from Test import Engineer
from CommandManager import CommandManager
from Mixin import MyPizza
import sys

def commandManagerTest():
    """
    Creates 2 commandManager objects. Each one will use the instance class method, since
    the CommandManager is a singleton
    """
    # The following line will fail since singletons cannot be instantiated normally
    #commandManager = CommandManager()
    
    commandManager = CommandManager.instance()
    # Note: This will not make a second instance. The commandManager and commandManager2
    # objects will both be referring to the same object. Notice how 'Creating new instance'
    # is only printed once, since there is only 1 instance of the CommandManager class.
    commandManager2= CommandManager.instance()
    commandManager.addCommand("Hello")
    # The command will be added to the same deque as commandManager since there is only 1 instance
    commandManager2.addCommand("Brian")
    commandManager.showAllCommand()
    
def mixinTest():
    pizza = MyPizza()
    pizza.prepare_pizza()
    pizza.showToppings()   
        
def main():
    # Instantiation of the Person class
    person = Person("Cam", 12)
    # Instantiation of the Engineer class, which is a derived class, or subclass, of the Person class
    engineer = Engineer("Brian", 49)
    engineer2 = Engineer("Ralph", 35)
    
    # Access the data attributes and the the class variable attribute
    print ("Person name = ", person.name)
    print ("Engineer name = ", engineer.name, ", type = ", Engineer.kind)
    print ("Engineer2 name = ", engineer2.name, ", type = ", engineer2.kind)
    
    # The data attributes of a class can be added dynamically
    engineer.address = "1 Main Street"
    print ("Address = ", engineer.address)
    # The data attributes of a class can be deleted dynamically
    del engineer.address
    # Once deleted, they no longer exist (The following line of code will fail)
    #print ("Address = ", engineer.address)
    
    # Determining types
    print (type(person))
    print (type(engineer))
    print (type(person.name))
    print (type(person.age))
    print (type(engineer.testdict))
    print("Is person a Person = ", isinstance(person, Person))
    print("Is person an Engineer = ", isinstance(person, Engineer))
    print("Is engineer a Person = ", isinstance(engineer, Person))
    print("Is engineer an Engineer = ", isinstance(engineer, Engineer))
    print("Does Engineer subclass Person = ", issubclass(Engineer, Person))
    print("Does Person subclass Engineer = ", issubclass(Person, Engineer))
      
    # If a method or function is bound to a variable without using parenthesis, it is not called
    # but instead stored in a new variable for use later
    showDictReference = engineer.showDict
    shouldShowDict = 0
    if (shouldShowDict == 1):
        showDictReference()
    elif (shouldShowDict == 2):
        # Calling showDictReference using engineer as a functor (function object)
        engineer(showDictReference)
        
    engineer.staticMethod()
    
    commandManagerTest()
    
    mixinTest()
    
    str1 = "Hello"
    upper = lambda string: string.upper()
    print(upper(str1))

        
if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit