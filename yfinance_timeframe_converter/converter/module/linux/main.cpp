#include <vector>

#include <string>
#include "main.hpp"
#include "module/converter.hpp"
#include "module/index.hpp"

extern "C"{
    __attribute__((__visibility__("default"))) void convert_timeframe(char** index, int len_index, char** columns, int len_columns, double* values, int len_values, char** timeframes){
        // =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        // Index    
        std::vector<std::string> v_index(index, index+len_index);

        // Columns
        std::vector<std::string> v_columns(columns, columns+len_columns);

        // Values
        std::vector<double> v_values(values, values+len_values);

        // Timeframe
        std::vector<std::string> v_timeframe(timeframes, timeframes+2);
        // =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        


    }
}