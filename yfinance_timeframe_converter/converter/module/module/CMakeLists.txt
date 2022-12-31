add_library(converter
            converter.cpp
            converter.hpp
            utils.cpp
            utils.hpp
            global_variables.cpp
            global_variables.hpp)
			
target_compile_features(converter PUBLIC cxx_std_17)		
