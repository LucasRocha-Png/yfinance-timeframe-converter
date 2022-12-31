#include <vector>
#include <string>
#include "timeframe_exists.hpp"
#include "global_variables.hpp"
#include "utils.hpp"

int checks_if_timeframes_exists(std::vector<std::string>& timeframes){
    for (std::string timeframe : timeframes){
        int index_timeframe = get_index(available_timeframes, timeframe);
        if (index_timeframe == -1){
            return 1;
        }
    }
    return 0;
}
