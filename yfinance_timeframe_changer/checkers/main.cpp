#include <iostream>
#include <vector>
#include <string>

#include "main.hpp"
#include "src/checker.hpp"

extern "C"
{

    //[index, columns, values, timeframes]
    __attribute__((__visibility__("default"))) void checker(char** index, int len_index, char** columns, int len_columns, float* values, int len_values, char** timeframes){
        // Index    
        std::vector<std::string> v_index(index, index+len_index);

        // Columns
        std::vector<std::string> v_columns(columns, columns+len_columns);

        // Values
        std::vector<float> v_values(values, values+len_values);

        // Timeframe
        std::vector<std::string> v_timeframe(timeframes, timeframes+2);



        //
        checks_if_inputs_exists(v_timeframe);
        

        // 
        checks_if_input_is_lower_than_output(v_timeframe);










    }

}