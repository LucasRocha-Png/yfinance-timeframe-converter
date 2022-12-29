add_library(converter
            converter.cpp
            converter.hpp
            index.cpp
            index.hpp)
			
target_compile_features(converter PUBLIC cxx_std_17)		
