#include <vector>
#include <string>

#include "main.hpp"
#include "module/timeframe_exists.hpp"
#include "module/timeframe_equal_dataframe.hpp"
#include "module/timeframe_lower.hpp"
#include "module/columns.hpp"
#include "module/conversion.hpp"


extern "C"
{
    //[index, columns, values, timeframes]
    __attribute__((__visibility__("default"))) int* checker(char** index, int len_index, char** columns, int len_columns, char** timeframes){

        // =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        // Index    
        std::vector<std::string> v_index(index, index+len_index);

        // Columns
        std::vector<std::string> v_columns(columns, columns+len_columns);

        // Timeframe
        std::vector<std::string> v_timeframe(timeframes, timeframes+2);
        // =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

        

        // Checks if values are correct -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        std::vector<int> list_error = {};

        // Checks if all timeframes exists
        list_error.push_back(checks_if_timeframes_exists(v_timeframe));

        // Checks if timeframe_input is lower than output
        list_error.push_back(checks_if_input_is_lower_than_output(v_timeframe));

        // Checks if columns exists
        list_error.push_back(checks_if_columns_exists(v_columns));

        // Checks if index are equal than timeframe
        list_error.push_back(checks_if_index_is_equal_than_timeframe(v_index, v_timeframe[0]));

        // Checks if convertion is valid
        list_error.push_back(checks_if_convertion_is_valid(v_timeframe));

        int *list_error_ = new int[5];

        for (int i = 0; i < 5; i++){
            list_error_[i] = list_error[i];
        }

        return list_error_;
    }


    __attribute__((__visibility__("default"))) void free_array(int* array){
        delete[] array;
    }

}