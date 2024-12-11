from collections import deque

class CommandManager:
    """
    The CommandManager is a Singleton. Only 1 instance of this Class can ever be
    instantiated.
    
    The instance is created and accessed via the instance method.
    """
    
    # The instance of the CommandManager
    _instance = None
    
    def __init__(self):
        """
        The __init__ method should not be used since the class should only be initialized
        once via the instance method.
        """
        raise RuntimeError('Call instance() instead')
    
    @classmethod
    def instance(cls):
        """
        With classmethods, the class of the object instance is implicitly passed as the
        first argument instead of self.
        
        This method is used to access the lone instance of the CommandManager. If the instance
        has not been created yet, it will be created and the initial data attributes
        will be created.
        
        __new__:
        In Python, n Python, cls.__new__() is a special static method that is responsible for
        creating a new instance of a class. 
        
        The __new__ is called before __init__ and is responsible for creating and returning
        a new instance of the class.
        
        __new__ and __init__ are both called when trying to create an instance of a class.
        __new__ is used when you need to control the creation of a new instance, while
        __init__ is used to control the initialization of a new instance. 
        
        By overriding __new__(), you can customize the object creation process, such as:
        - Creating singletons (classes that can only have one instance).
        - Inheriting from immutable types (like int or str).
        - Implementing custom object allocation strategies.
    
        """
        if cls._instance is None:     
            print('Creating new instance')
            # The first argument to __new__() is the class itself, conventionally named cls.
            cls._instance = cls.__new__(cls)       
            # Create a commandQueue data attribute that is a double ended queue
            cls._instance.commandQueue = deque()
        return cls._instance
    
    def addCommand(self, command: str):
        """

        Args:
            command (string): A string command to add to the commandQueue
        """
        self.commandQueue.append(command)
    
    def showAllCommand(self):
        print ("Commands are:")
        for command in self.commandQueue:
            print ("    ", command)