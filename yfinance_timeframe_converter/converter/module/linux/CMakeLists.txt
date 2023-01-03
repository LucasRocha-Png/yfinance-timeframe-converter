#Set the version of cmake
cmake_minimum_required(VERSION 3.22)

#Set the name of the project and the name
project(convert_timeframe VERSION 1.0.0)


set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Werror -fPIC -std=c++17")


#Imports the subdirectory folder of print vector
add_subdirectory(converters)

#Create Shared Library of main
add_library(${PROJECT_NAME} SHARED
	    main.cpp
	    main.hpp)

#Links print_vector library to the project
target_link_libraries(${PROJECT_NAME}
                      converter) 


target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_17)	                      

