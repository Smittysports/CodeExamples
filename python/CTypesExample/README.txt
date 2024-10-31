# This section of the README describes pipenv

# Run TestCTypes.py
python TestCTypes.py
    # This should fail since numpy is a dependency and pipenv shell has not been called yet

# Prepare the virtual environment (only needed first time)
pipenv install
    # This will create a Pipfile and Pipfile.lock
    # The Pipfile is used to keep track of the dependencies your project needs
    # The Pipfile.lock declares all dependencies (and sub-dependencies) of your project, their latest available versions, and the current hashes for the downloaded files. This ensures repeatable, and most importantly deterministic, builds.

# Location where pipenv stores modules
pipenv --venv
- Local packages, such as numpy used here, are stored in the location shown from the ‘pipenv --venv’ command in Lib\version\site-packages

# Update the virtual environment so it uses the numpy module (only needed first time the module is added)
pipenv install numpy
    # This will update the Pipfile so that it now has numpy as one of the packages
    # It will update the Pipfile.lock file as well
    # NOTE: 'pipenv uninstall numpy' will remove the package, make sure to remove it from requirements.txt if permanent

# Run TestCTypes.py in a virtual environment
pipenv shell
    # This creates a virtual environment that will contain the packages that
    # are not standard in Python and only needed for this program
    # TestCTypes will fail if this is not run, since numpy is not in the regular Python installation

# Run TestCTypes.py
python TestCTypes.py
    # This will now work

exit
    # This will exit the virtual environment

# Run TestCTypes.py
python TestCTypes.py
    # This will fail since the virtual environment has been closed

# Save a requirements file
pipenv requirements > requirements.txt
    # This will create a new file that can be used anywhere to reproduce the Pipfile
    # Now, we can simply run 'pipenv install' and the Pipfile will contain the numpy module
    # The requirements.txt file must just be in the same folder

# Remove the venv
pipenv --rm
- This is only needed if the virtual environment is no longer needed.
- It can always be recreated if needed though

# --------------------- END SECTION -------------------------------

VSCode section

In order to use the virtual environment in VSCode
- Press F1 in VSCode
- Type 'Python Interpreter'
- Choose the pipenv associated with this project

If using the "(gdb) Launch Python and debug C++" debugger to debug C
- Modify the .json to point to the path that is show with 'pipenv --venv'
- For me, it is "/home/guest/.local/share/virtualenvs/CTypesExample-MywxcaGb/bin/python3"
# --------------------- END SECTION -------------------------------


This section of the README is used to describe how to create a c++ shared library and use it in a Python script.

1) Create the C++ file, see TestCTypes.cpp
2) Compile it into a shared library (.so)
   g++ -shared -o libTestCTypes.so -fPIC TestCTypes.cpp
3) Create a Python script to call the .so, see TestCTypes.py
4) The following imports in the Python file are needed for importing the C++ shared library
   from ctypes import *
   import os
5) The following line will load the library. Note that the os.path.abspath is used to tell the
   LoadLibrary command where the dll is (it will translate to /home/guest/Robotics/HelloWorld/python/CTypesExample/libTestCTypes.so)
     libname = cdll.LoadLibrary(os.path.abspath("libTestCTypes.so"))
6) The following line will create a python binding so that the cPrint variable will refer to the 
   printHello() function in the TestCTypes.cpp file.
     cPrint = libname.printHello()
7) The following line will run the cPrint function
     cPrint

# For clang
1) clang -std=c++20 -c -fPIC TestCTypes.cpp -o TestCTypes.o
   - The -c will compile the source files into an object file without linking
   - The -fPIC generates position-independent code, which is required for shared libraries
   - Creates TestCTypes.o
2) clang -lstdc++ -shared -o libTestCTypes.so TestCTypes.o
   - The -lstdc++ tells the linker to use the C++ standard library
   - The -shared creates a shared library (.so)
   - The -o libTestCTypes.so specifies the output file name for the shared library

