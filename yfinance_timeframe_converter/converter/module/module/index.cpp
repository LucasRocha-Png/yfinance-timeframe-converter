#include <vector>
#include <string>
#include "index.hpp"


int dayofweek(int d, int m, int y){
    static int t[] = { 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 };
    y -= m < 3;
    return ( y + y/4 - y/100 + y/400 + t[m-1] + d) % 7;
}

std::vector<std::string> index_to_day(std::vector<std::string>& index){

    std::vector<std::string> new_index;

    for (std::string index_date : index){
        std::string day = index_date.substr(8,2);
        std::string month = index_date.substr(5,2);
        std::string year = index_date.substr(0,4);

        new_index.push_back(year);
    }

    return new_index;

}