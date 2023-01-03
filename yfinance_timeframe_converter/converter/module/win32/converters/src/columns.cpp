#include <vector>
#include <string>
#include "../includes/columns.hpp"

std::map<std::string, std::string> columns_mask = {
    {"Open", "first"},
    {"High", "max"},
    {"Low", "min"},
    {"Close", "last"},
    {"Adj Close", "last"},
    {"Volume", "sum"}
};


std::vector<std::string> create_columns_mask(std::vector<std::string>& columns){
    std::vector<std::string> vector_mask;
    std::string mask;
    for (std::string& column : columns){
        mask = columns_mask[column];
        vector_mask.push_back(mask);
    }

    return vector_mask;
}