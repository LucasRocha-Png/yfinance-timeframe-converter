#include <vector>
#include <string>
#include "utils.hpp"
#include "timeframe_lower.hpp"

int checks_if_input_is_lower_than_output(std::vector<std::string>& timeframes){
    std::vector<std::string> timeframes_available = {"1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"};

    std::string timeframe_input = timeframes[0];
    std::string timeframe_output = timeframes[1];


    int index_input = get_index(timeframes_available, timeframe_input);
    int index_output = get_index(timeframes_available, timeframe_output);

    if (index_input > index_output){
        return 1;
    }
    else {
        return 0;
    }
}



