#include <vector>
#include <string>
#include "utils.hpp"

int get_index(std::vector<std::string>& list, std::string& word){
    long int index = 0;
    for (std::string word_ : list){
        index++;
        if (word_ == word){return index;}
    }
    return -1;
}
