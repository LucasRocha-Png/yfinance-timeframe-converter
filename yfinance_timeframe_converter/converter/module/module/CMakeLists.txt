add_library(converter
            converter.cpp
            converter.hpp
            minutes.cpp
            minutes.hpp
            utils.cpp
            utils.hpp)
			
target_compile_features(converter PUBLIC cxx_std_17)		
