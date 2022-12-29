#include <vector>
#include <string>
#include "utils.hpp"
#include "columns.hpp"

int checks_if_columns_exists(std::vector<std::string>& columns){
    std::vector<std::string> columns_available = {"Open", "High", "Low", "Close", "Adj Close", "Volume"};
    for (std::string column : columns){
        int index = get_index(columns_available, column);
        if (index == -1){
            return 1;
        }
    }
    return 0;
}
