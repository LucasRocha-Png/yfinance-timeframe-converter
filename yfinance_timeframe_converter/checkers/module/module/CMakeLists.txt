add_library(
	    checker
	    timeframe_exists.cpp
	    timeframe_exists.hpp
	    columns.cpp
	    columns.hpp
	    conversion.cpp
	    conversion.hpp
		timeframe_equal_dataframe.cpp
		timeframe_equal_dataframe.hpp
		timeframe_lower.cpp
		timeframe_lower.hpp
		global_variables.cpp
		global_variables.hpp
	    utils.cpp
	    utils.hpp
		)
			
target_compile_features(checker PUBLIC cxx_std_17)		
