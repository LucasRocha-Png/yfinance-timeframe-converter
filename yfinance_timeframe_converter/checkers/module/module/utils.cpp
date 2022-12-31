#include <vector>
#include <string>
#include "utils.hpp"

int 
get_index(std::vector<std::string>& list, std::string& word){
    /*
    Get the index of the value from list, if not found, return -1
    */

    long int index = 0;
    for (std::string word_ : list){
        index++;
        if (word_ == word){return index;}
    }
    return -1;
}
