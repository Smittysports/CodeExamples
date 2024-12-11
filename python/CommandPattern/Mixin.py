class PlainPizza:
    def __init__(self):
        self.toppings = []
    
    def showToppings(self):
        for topping in self.toppings:
            print (topping)

class OlivesMixin:
    def addOlives(self):
        print("Adding olives!")
        self.toppings += ['olives']
        
class PepperoniMixin:
    def addPepperoni(self):
        print("Adding pepperoni!")
        self.toppings += ['pepperoni']
        
class MyPizza(OlivesMixin, PepperoniMixin, PlainPizza):
    """
    This class uses mixins. The mixins are inherited using multiple inheritence.
    Notice how the mixins can work with each other but are not very useful by
    themselves.
    
    The PlainPizza is not a mixin. It is a basic pizza with a list for all the toppings.
    The OlivesMixin and PepperoniMixin are classes that when added to the MyPizza
    class extend the amount of toppings allowed.

    Args:
        OlivesMixin (class): A mixin to add olives to a toppings list
        PepperoniMixin (class): A mixin to add pepperoni to a toppings list
        PlainPizza (class): A class containing the pizza, which contains the toppings list
    """
    def prepare_pizza(self):
        self.addOlives()
        self.addPepperoni()
