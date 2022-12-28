#include <iostream>
#include <vector>
#include <string>

#include "main.hpp"
#include "src/checker.hpp"

extern "C"
{
    //[index, columns, values, timeframes]
    __attribute__((__visibility__("default"))) void checker(char** index, int len_index, char** columns, int len_columns, char** timeframes){
        // Index    
        std::vector<std::string> v_index(index, index+len_index);

        // Columns
        std::vector<std::string> v_columns(columns, columns+len_columns);

        // Timeframe
        std::vector<std::string> v_timeframe(timeframes, timeframes+2);

        //
        checks_if_inputs_exists(v_timeframe);

        // 
        checks_if_input_is_lower_than_output(v_timeframe);

        //
        checks_if_columns_exists(v_columns);

        //
        std::cout << checks_if_index_is_equal_than_timeframe(v_index, v_timeframe[1]);

    }

}