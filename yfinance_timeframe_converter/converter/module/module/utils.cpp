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