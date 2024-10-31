#include <iostream>
#include <cstring>
#include <format>

// Forward declaration of the templates
template<typename T>
T addAny(T, T);

extern "C" {

void printHello()
{
    std::cout << "C Print with std::cout\n";
}

/** A wrapper to use the addAny template from external code */
int addInt(const int a, const int b)
{
    return addAny(a, b);
}

/** Returns a pointer to a null-terminated byte string, which is a duplicate of the
 * string created in this function. The returned pointer must be passed to free to avoid
 * a memory leak. 
 */
const char* createNewString(const char* str)
{
    std::string newStr {"The new string = "};
    newStr += str;
    std::cout << "C: " << newStr << "\n";
    return strdup(newStr.data());
}

/** Pointers should be deleted in the environment they were created in. */
void deleteCharPointer(char* pChar)
{
    if (pChar)
	    std::free(pChar);
        std::cout << "Freed\n";
}

/** Calling this function from Python requires the return type and arguments to be
 * defined, like this:
 *   libName.addFloat.restype = c_float
 *   libName.addFloat.argtypes = c_float, c_float
 */
float addFloat(const float a, const float b)
{
    return addAny(a, b);
}

} // extern "C"

/** C++ templates are resolved at compile time, so they cannot simply be added to 'extern "c"'.
 * 
 * To get around this, a wrapper is needed inside the 'extern "C"' which will instantiate the
 * template. 
 */
template<typename T>
T addAny(T a, T b)
{
    return a + b;
}

