#include <vector>
#include <string>
#include "utils.hpp"


bool isin(std::string& object, std::vector<std::string>& list){
    for (std::string& value : list){
        if (object == value){
            return true;
        }
    }
    return false;
}

int string_to_int(std::string& string, std::pair<int,int> slicing){

    

    return std::stoi(string);
}