set(SOURCE
    src/columns.cpp
    src/global_variables.cpp
    src/timeframe_equal_dataframe.cpp
    src/timeframe_exists.cpp
    src/timeframe_lower.cpp
    src/utils.cpp)
    
set(HEADERS
    includes/columns.hpp
    includes/global_variables.hpp
    includes/timeframe_equal_dataframe.hpp
    includes/timeframe_exists.hpp
    includes/timeframe_lower.hpp
    includes/utils.hpp)    

add_library(checker ${SOURCE} ${HEADERS})
			
target_compile_features(checker PUBLIC cxx_std_17)		
