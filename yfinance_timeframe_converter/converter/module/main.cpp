#include <vector>
#include <string>
#include <iterator>

#include "main.hpp"
#include "converters/includes/index.hpp"
#include "converters/includes/utils.hpp"
#include "converters/includes/columns.hpp"
#include "converters/includes/values.hpp"


#ifdef _WIN32
    #define API __declspec(dllexport)
#else
    #define API __attribute__((__visibility__("default")))
#endif

extern "C"{
    API char** convert_index(char** index, int lenght_index, char** timeframes){

        // Converts values to vector
        std::vector<std::string> v_index(index, index+lenght_index);         
        std::vector<std::string> v_timeframe(timeframes, timeframes+2); 
        
        // Get output timeframe
        std::string timeframe_output = timeframes[1];
        
        // Get the converted index based on timeframe
        std::vector<std::string> new_index = convert_index_(v_index, timeframe_output);

        // Converts the new index to pointer
        char** p_index = vector_to_p(new_index);

        return p_index;
    }

    API double* convert_values(double* values, int lenght_values, char** index, int lenght_index, char** converted_index, int lenght_coverted_index, char** columns, int lenght_columns){
        // Converts values to vector
        std::vector<double> v_values(values, values + (lenght_values));
        std::vector<std::string> v_index(index, index+lenght_index);
        std::vector<std::string> v_converted_index(converted_index + 1, converted_index+lenght_coverted_index+1); // The +1 is for removing the len of the index that was added to the array
        std::vector<std::string> v_columns(columns, columns+lenght_columns);

        // Create mask for columns
        std::vector<std::string> mask = create_columns_mask(v_columns);

        // Converts values
        std::vector<double> conveted_values = convert_values_(v_values, v_index, v_converted_index, mask);

        double* converted_values_p = vector_to_p(conveted_values);

        return converted_values_p;
    }


    API void free_array_char(char** array, int size){
        for (int i = 0; i < size; i++) {
            free(array[i]);
        }
        free(array);
    }

    API void free_array_double(double* array){
        free(array);
    }

}