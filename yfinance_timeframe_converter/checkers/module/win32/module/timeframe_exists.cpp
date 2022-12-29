#include <vector>
#include <string>
#include "timeframe_exists.hpp"

int checks_if_timeframes_exists(std::vector<std::string>& timeframes){
    std::vector<std::string> timeframes_available = {"1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"};

    for (std::string timeframe : timeframes){
        bool exists = false;
        for (std::string period : timeframes_available){
            if (period == timeframe){
                exists = true;
                break;
            }
        }
        if (exists == false){
            return 1;
        }
    }
    return 0;
}
