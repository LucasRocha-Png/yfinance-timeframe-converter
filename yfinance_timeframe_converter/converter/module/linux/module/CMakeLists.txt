add_library(converter
            converter.cpp
            converter.hpp
            convert_timeframe.cpp
            convert_timeframe.hpp)
			
target_compile_features(converter PUBLIC cxx_std_17)		
