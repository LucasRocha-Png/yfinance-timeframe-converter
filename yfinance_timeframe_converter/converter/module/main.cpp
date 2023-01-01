#include <vector>
#include <string>
#include <iterator>

#include "main.hpp"
#include "converters/includes/index.hpp"
#include "converters/includes/utils.hpp"


#ifdef _WIN32
    #define API __declspec(dllexport)
#else
    #define API __attribute__((__visibility__("default")))
#endif

extern "C"{
    API char** convert_index(char** index, int len_index, char** timeframes){
        /*
        Threats the data and pass it to the convert_index_ function 
        */
        
        std::vector<std::string> v_index(index, index+len_index);         
        std::vector<std::string> v_timeframe(timeframes, timeframes+2); 

        std::string timeframe_input = timeframes[0];
        std::string timeframe_output = timeframes[1];
        
        std::vector<std::string> new_index = convert_index_(v_index, timeframe_input, timeframe_output);

        char** p_index = vector_to_p(new_index);

        return p_index;
    }

    API void convert_values(double** values, char** index, char** converted_index, char** columns){

    }


    API void free_array_char(char** array){
        delete[] array;
    }

    API void free_array_double(double** array){
        delete[] array;
    }

}