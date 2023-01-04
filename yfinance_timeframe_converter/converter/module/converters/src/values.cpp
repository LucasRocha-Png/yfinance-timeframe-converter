#include <vector>
#include <string>
#include "../includes/values.hpp"
#include "../includes/utils.hpp"

std::vector<double> convert_values_(std::vector<double>& values, std::vector<std::string>& index, std::vector<std::string>& converted_index, std::vector<std::string>& list_mask){

    // Get lenghts
    int lenght_mask = list_mask.size();

    // Divide values vector by the lenght of masks, returning a 2d matrix
    std::vector<std::vector<double>> matrix_values = to_matrix(values, lenght_mask);
    int lenght_line = index.size();

    // Create some variable for the loop
    std::string mask;


    // Creates index to add
    int i;
    std::string current_converted_index;
    std::string current_index;
    double value;
    double converted_value;
    std::vector<double> temp_vector;
    std::vector<double> result;


    for (int column = 0; column < lenght_mask; column++){
        mask = list_mask[column]; // Get the operation maks
        i = 0;
        for (int line = 0; line < lenght_line; line++){
            current_converted_index = converted_index[i];
            current_index = index[line];
            value = matrix_values[column][line];

            if (current_converted_index == current_index){
                if (current_index != converted_index.back()){
                    i++;
                }

                if (current_index == converted_index[0]){
                    temp_vector.push_back(value);          
                    continue;
                }
        
                converted_value = return_value_based_on_mask(temp_vector, mask);
                result.push_back(converted_value);
            }
            temp_vector.push_back(value);            
        }
        converted_value = return_value_based_on_mask(temp_vector, mask);
        result.push_back(converted_value);

    }


    // Print matrix if you want
    /*
    std::vector<std::vector<double>> matrix_result = to_matrix(result, lenght_mask);
    matrix_result = transpose(matrix_result);

    std::cout << "\n                 ";
    for (int column = 0; column < lenght_mask; column++){
        std::cout << list_mask[column] << "          ";
    }
    std::cout << "\n";


    int i_converted = 0;
    int gap;

    for (int column = 0; column < int(matrix_result.size()); column++){
        for (int row = 0; row < int(matrix_result[0].size()); row++){
            if (row == 0){
                std::cout << converted_index[i_converted] << "         ";
                i_converted++;
            }

            gap = 20 - int(std::to_string(matrix_result[column][row]).size());
            std::string space(gap, ' ');
            std::cout << matrix_result[column][row] << space;
        }
        std::cout << "\n";
    }
    */

   return result;
}
