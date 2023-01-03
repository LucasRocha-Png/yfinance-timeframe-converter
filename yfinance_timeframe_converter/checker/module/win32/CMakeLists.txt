#Set the version of cmake
cmake_minimum_required(VERSION 3.22)

#Set the name of the project and the name
project(checkers VERSION 1.0.0)

#Imports the subdirectory folder of print vector
add_subdirectory(checkers)

#Create Shared Library of main
add_library(${PROJECT_NAME} SHARED
				main.cpp
				main.hpp)

#Links print_vector library to the project
target_link_libraries(${PROJECT_NAME}
                      checker) 


target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_17)	                      

