#include <vector>
#include <string>
#include <iostream>
#include "../includes/values.hpp"
#include "../includes/utils.hpp"

std::vector<int> get_index_two_vectors(std::vector<std::string>& smaller_vector, std::vector<std::string>& bigger_vector){
    std::vector<int> result;

    for (std::string& value : smaller_vector){
        result.push_back(get_index(bigger_vector, value));
    }

    return result;
}


void convert_values_(std::vector<double>& values, std::vector<std::string>& index, std::vector<std::string>& converted_index, std::vector<std::string>& list_mask){

    // Get lenghts
    int lenght_mask = list_mask.size();

    // Divide values vector by the lenght of masks, returning a 2d matrix
    std::vector<std::vector<double>> matrix_values = to_matrix(values, lenght_mask);
    int lenght_line = matrix_values[0].size();

    // Create some variable for the loop
    std::string mask;
    std::vector<double> temp_vec;
    double value;
    double value_filtered;

    // Creates index to add
    std::vector<int> indexes_to_add = get_index_two_vectors(converted_index, index);
    int i;
    int current_index_to_add;
    std::vector<double> result;


    // For each column
    for (int column = 0; column < lenght_mask; column++){
        mask = list_mask[column]; // Get the operation maks

        i = 0;

        for (int line = 0; line < lenght_line; line++){
            current_index_to_add = indexes_to_add[i];

            if (current_index_to_add == line){
                i += 1;
                if(line == indexes_to_add[0]){ // If is the first loop
                    value = matrix_values[column][line];
                    temp_vec.push_back(value);
                    continue;
                }

                value_filtered = return_value_based_on_mask(temp_vec, mask);
                result.push_back(value_filtered);
            }
            value = matrix_values[column][line];
            temp_vec.push_back(value);
        }

    }

  

}
