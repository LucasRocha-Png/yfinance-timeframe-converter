#include <vector>
#include <string>
#include "../includes/timeframe_equal_dataframe.hpp"
#include "../includes/global_variables.hpp"

int checks_if_index_is_equal_than_timeframe(std::vector<std::string>& index, std::string& timeframe){
    std::string last_index = index[index.size()-1];
    int lenght_last_index = last_index.length();

    bool is_in_minutes_timeframe = false;
    for (std::string i : minutes_timeframes){
        if (i == timeframe){
            is_in_minutes_timeframe = true;
            break;
        }
    }

    if (lenght_last_index == 10 && is_in_minutes_timeframe == false){
        return 0;
    }
    else if (lenght_last_index != 10 && is_in_minutes_timeframe == true){
        return 0;
    }
    return 1;
}
