#include <vector>
#include <string>
#include "utils.hpp"
#include "timeframe_lower.hpp"
#include "global_variables.hpp"

int checks_if_input_is_lower_than_output(std::vector<std::string>& timeframes){
    std::string timeframe_input = timeframes[0];
    std::string timeframe_output = timeframes[1];

    int index_input = get_index(available_timeframes, timeframe_input);
    int index_output = get_index(available_timeframes, timeframe_output);

    if (index_input > index_output){
        return 1;
    }
    else {
        return 0;
    }
}



