#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>
#include "../includes/utils.hpp"


bool isin(std::string& object, std::vector<std::string>& list){
    /*
    Checks if value is in list
    */
    for (std::string& value : list){
        if (object == value){
            return true;
        }
    }
    return false;
}

int get_index(std::vector<std::string>& list, std::string& word){
    /*
    Get the index of the value from list, if not found, return -1
    */

    long int index = 0;
    for (std::string word_ : list){
        if (word_ == word)
            {return index;}
        index++;
    }
    return -1;
}

int getDayOfWeek(int day, int month, int year) {
    /*
    Get day of the weak after passed day, month and year
    */

    int t[] = { 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 };
    year -= month < 3;

    int dayOfWeek = (year + year/4 - year/100 + year/400 + t[month-1] + day) % 7;

    return dayOfWeek;
}


char** vector_to_p(std::vector<std::string>& list){
    // Aloca a memória para a char**
    char** arr = new char*[list.size() + 1];

    // Copia os elementos da vector para a char**
    for (size_t i = 0; i < list.size(); i++) {
        arr[i] = new char[list[i].size() + 1];
        strcpy(arr[i], list[i].c_str());
    }

    // Adiciona um elemento NULL no final da char**
    arr[list.size()] = NULL;

    return arr;
}


double return_value_based_on_mask(std::vector<double>& list, std::string& mask){
    double returned_value;
    if (mask == "first"){
        returned_value = list.front();
    }

    else if (mask == "max"){
        std::vector<double>::iterator it = std::max_element(list.begin(), list.end());
        returned_value = *it;
    }

    else if (mask == "min"){
        std::vector<double>::iterator it = std::min_element(list.begin(), list.end());
        returned_value = *it;
    }

    else if (mask == "last"){
        returned_value = list.back();
    }

    else if (mask == "sum"){
        double sum = std::accumulate(list.begin(), list.end(), 0.0);
        returned_value = sum;
    }

    list.clear();
    return returned_value;
}

std::vector<std::vector<double>> to_matrix(const std::vector<double>& list, int num_cols) {

    // Lenght list
    int lenght_list = list.size();

    // Values per column
    int quantity_values_per_column = lenght_list / num_cols;

    // Resized vector
    std::vector<std::vector<double>> resized_vector;


    for (int i = 0; i < lenght_list; i++) {
        if (i % quantity_values_per_column == 0) {
            resized_vector.emplace_back(); // Adds a blank line
        }
        resized_vector.back().push_back(list[i]);
    }
    return resized_vector;
}



