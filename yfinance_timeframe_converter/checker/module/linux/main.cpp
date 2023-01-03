#include <vector>
#include <string>

#include "checkers/includes/timeframe_exists.hpp"
#include "checkers/includes/timeframe_equal_dataframe.hpp"
#include "checkers/includes/timeframe_lower.hpp"
#include "checkers/includes/columns.hpp"
#include "checkers/includes/utils.hpp"
#include "main.hpp"

#ifdef _WIN32
    #define API __declspec(dllexport)
#else
    #define API __attribute__((__visibility__("default")))
#endif


extern "C"
{
    //[index, columns, values, timeframes]
    API int* checker(char** index, int len_index, char** columns, int len_columns, char** timeframes){

        // Converts values to vector =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 
        std::vector<std::string> v_index(index, index+len_index);
        std::vector<std::string> v_columns(columns, columns+len_columns);
        std::vector<std::string> v_timeframe(timeframes, timeframes+2);

        // Checks if values are correct -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        std::vector<int> list_error = {};

        // Pushes the result to the list of errors
        list_error.push_back(checks_if_timeframes_exists(v_timeframe));
        list_error.push_back(checks_if_input_is_lower_than_output(v_timeframe));
        list_error.push_back(checks_if_columns_exists(v_columns));
        list_error.push_back(checks_if_index_is_equal_than_timeframe(v_index, v_timeframe[0]));


        // Creates pointer
        int* list_error_ = vector_to_p(list_error);
        return list_error_;
    }


    API void free_array(int* array){
        delete[] array;
    }

}