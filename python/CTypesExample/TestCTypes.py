from ctypes import *
import os
import numpy as np

print("A random number is ", np.random.randint(1, 100))

print("Python print statement")

# Load the shared library created fromm the TestCTypes.cpp file
pathToSharedLibrary = os.path.relpath("lib/libTestCTypes.so")
libName = cdll.LoadLibrary(pathToSharedLibrary)
print("The path to the shared library is ", pathToSharedLibrary)

# Call a basic function that does not take any parameters
cPrint = libName.printHello()
cPrint

# Call a function that takes 2 parameters and returns a value
print ("Result of addInt(1, 2) is ", libName.addInt(1, 2))
cAdd = libName.addInt(3, 4)
print ("Result of addInt(3, 4) is " , cAdd)
cAdd2 = libName.addInt
print ("Result of addInt(5, 6) is " , cAdd2(5, 6))

# Calling into a function that is non-int needs the return type and argument types defined
libName.addFloat.restype = c_float
libName.addFloat.argtypes = c_float, c_float
print ("Result of addFloat(1.5, 2.2) is ", libName.addFloat(1.5, 2.2))

# Calling into the createNewString function requires the return and argument types to be defined
# Note: c_char_p will return a reguluar Python string type
libName.createNewString.restype = c_void_p
libName.createNewString.argtypes = [c_char_p]
# The char* argument requires a string buffer to be created and passed in
testVal = create_string_buffer(b"Test", 5)
retStr = libName.createNewString(testVal)
# Cast from void to char to use the pointer. Access .value to dereference
retStrVal = cast(retStr, c_char_p).value
print("Python: ", retStrVal)
# Since c_char_p will return a reguluar Python string type, we pass in a void instead
libName.deleteCharPointer.argtypes = [c_void_p]
libName.deleteCharPointer(retStr)
