
class Person:
    """ A class
    """

    kind = 'Person'
    
    def __init__(self, name, age):
        """
        All classes contain an __init__ function that is always executed when the class is instantiated.
        
        Python does not support constructor overloading. Only the last defined __init__
        will be used. If a user needs to instantiate a class in different ways,
        then a *args argument should be used (or a similar design).
        
        Instantiation is when a class is created.
        
        Data attributes:        
        The data attributes are name and age (first). They are set and accessed internally
        in the class using self. They are public.
        
        The __init__ function accepts arguments which allow data to be passed into the function.
        
        Args:
            name (string): Name of the Person
            age (int): Age of the Person
        """
        self.name = name
        self.age = age
    
    def getHasGlasses(self):
        return False
    
class Engineer(Person):  
    """
    The Engineer class inherits from the Person class

    Args:
        Person (class): The Engineer class inherits from the Person base class
    """
    
    # Class variable that is shared by all instances. This variable is mutable.
    kind = 'Engineer'
               
    def __init__(self, name, age):
        """
        Called when an Engineer class is instantiated.
        
        The super() function will allow this class to access the base class

        Args:
            name (string): Name of the Person
            age (int): Age of the Person
        """
        super().__init__(name, age)
        
        self.testdict = {
            "String": "test",
            "Int": 1,
            "Float": 1.5
        }
        
        # Data attributes that are prefixed with two underscores __ is a convention for
        # private variables. These should only be accessed via methods of this class.
        self.__languages = {}
    
    def __call__(self, f):
        """
        Overriding the __call__ Python method to allow a functor to be used
        """
        return f()
    
    def showDict(self):
        """
        Functions that are part of a Class are referred to as Methods. A method is
        a function that belongs to a class.
        
        Class methods can access the Class data attributes by declaring self as the first
        argument to the method.
        
        Args:
            self (class instance): The instance of the Engineer class. Whenever you call
            a method of an object created from a class, the object is automatically passed
            as the first argument using the “self” parameter. 
        """
        
        print ("Dictionary Values:")
        # Iterate over keys
        print("    key:")
        for key in self.testdict:
            print("    ", key)

        # Iterate over values
        print("    value:")
        for value in self.testdict.values():
            print("    ", value)

        # Iterate over key-value pairs
        print("    key, value:")
        for key, value in self.testdict.items():        
            print("    ", key, ", ", value)
            
        print ("The showDict documentation:")
        print (Engineer.showDict.__doc__)
        
        # Example of creating a dict using a constructor
        thisdict = dict(name = "John", age = 36, country = "Norway")
        print(thisdict)
        
    def getHasGlasses(self):
        """
        This method overrides the method in the base.

        Returns:
            bool: Returns True since all Engineers have glasses :)
        """
        return True
    
    @staticmethod
    def staticMethod():
        """
        Static methods do not require the self parameter and can be called directly
        from the class name without creating an instance (ie..  Static methods are bound
        to the class, not the instance). Static methods cannot access instance attributes.
        
        Static methods are often used for utility functions that don't need access to instance-specific data. 
        """
        print("This is a static method")