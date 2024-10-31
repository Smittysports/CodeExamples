cmake_minimum_required(VERSION 3.5.0)
project(TestCTypes VERSION 0.1.0 LANGUAGES C CXX)

add_library(TestCTypes SHARED TestCTypes.cpp)


set_target_properties(TestCTypes 
    PROPERTIES
    OUTPUT_NAME "TestCTypes"
    CXX_STANDARD 20
    COMPILE_FLAGS "-g -Wall -Wextra"
    CMAKE_POSITION_INDEPENDENT_CODE ON
)
