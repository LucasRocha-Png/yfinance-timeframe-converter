#include <vector>
#include <string>
#include "../includes/timeframe_exists.hpp"
#include "../includes/global_variables.hpp"
#include "../includes/utils.hpp"

int checks_if_timeframes_exists(std::vector<std::string>& timeframes){
    for (std::string timeframe : timeframes){
        int index_timeframe = get_index(available_timeframes, timeframe);
        if (index_timeframe == -1){
            return 1;
        }
    }
    return 0;
}
