#include <vector>
#include <string>
#include "timeframe_equal_dataframe.hpp"
#include "global_variables.hpp"

int checks_if_index_is_equal_than_timeframe(std::vector<std::string>& index, std::string& timeframe){
    std::string last_index = index[index.size()-1];
    int len_last_index = last_index.length();

    bool is_in_minutes_timeframe = false;
    for (std::string i : minutes_timeframes){
        if (i == timeframe){
            is_in_minutes_timeframe = true;
            break;
        }
    }

    if (len_last_index == 10 && is_in_minutes_timeframe == false){
        return 0;
    }
    else if (len_last_index != 10 && is_in_minutes_timeframe == true){
        return 0;
    }
    return 1;
}
