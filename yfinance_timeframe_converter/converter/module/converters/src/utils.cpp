#include <vector>
#include <string>
#include <cstring>
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