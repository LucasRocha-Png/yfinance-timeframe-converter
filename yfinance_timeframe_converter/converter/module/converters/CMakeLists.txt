set(SOURCES
    src/global_variables.cpp
    src/index.cpp
    src/values.cpp
    src/columns.cpp
    src/utils.cpp)
 
set(HEADERS
    includes/global_variables.hpp
    includes/index.hpp
    includes/values.hpp	
    includes/columns.hpp
    includes/utils.hpp)
    
add_library(converter ${SOURCES} ${HEADERS})        
    
