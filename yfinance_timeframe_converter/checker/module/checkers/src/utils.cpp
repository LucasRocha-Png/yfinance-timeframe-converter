#include <vector>
#include <string>
#include "../includes/utils.hpp"

int get_index(std::vector<std::string>& list, std::string& word){
    /*
    Get the index of the value from list, if not found, return -1
    */

    long int index = 0;
    for (std::string word_ : list){
        if (word_ == word){return index;}
        index++;
    }
    return -1;
}

int* vector_to_p(std::vector<int>& list){
    int lenght_list = list.size();

    int* new_list = (int*) malloc(lenght_list * sizeof(int));
    for (int i = 0; i < lenght_list; i++){
        new_list[i] = list[i];
    }
    return new_list;
}
