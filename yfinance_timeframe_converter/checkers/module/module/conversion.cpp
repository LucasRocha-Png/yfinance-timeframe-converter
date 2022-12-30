#include <vector>
#include <string>
#include "conversion.hpp"

int checks_if_convertion_is_valid(std::vector<std::string>& timeframes){
    std::string timeframe_input = timeframes[0];
    std::string timeframe_output = timeframes[1];

    if (timeframe_input == "2m"){
        if (timeframe_output == "5m"){
            return 1;
        }

        else if (timeframe_output == "15m"){
            return 1;
        }
    }

    else if (timeframe_input == "3m"){
        if (timeframe_output == "5m"){
            return 1;
        }
    }

    else if (timeframe_input == "90m"){
        if (timeframe_output == "1h"){
            return 1;
        }
        else if (timeframe_output == "4h"){
            return 1;
        }
    }

    else if (timeframe_input == "5d"|| timeframe_input == "3h" || timeframe_output == "5d"){
        return 1;
    }

    return 0;
}
