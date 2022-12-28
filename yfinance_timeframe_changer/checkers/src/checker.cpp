#include <iostream>
#include <vector>
#include <string>

int get_index(std::vector<std::string> list, std::string word){
    long int index = 0;
    for (std::string word_ : list){
        index++;
        if (word_ == word){return index;}
    }
    return 0;
}


int checks_if_inputs_exists(std::vector<std::string> timeframes){
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


int checks_if_input_is_lower_than_output(std::vector<std::string> timeframes){
    std::vector<std::string> timeframes_available = {"1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"};

    std::string timeframe_input = timeframes[0];
    std::string timeframe_output = timeframes[1];


    int index_input = get_index(timeframes_available, timeframe_input);
    int index_output = get_index(timeframes_available, timeframe_output);

    if (index_input > index_output){
        return 2;
    }

    else {
        return 0;
    }
}