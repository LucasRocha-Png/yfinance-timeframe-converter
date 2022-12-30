#include <vector>
#include <string>
#include <iterator>

#include "main.hpp"
#include "module/converter.hpp"
#include "module/utils.hpp"
#include "module/minutes.hpp"

#ifdef _WIN32
    #define API __declspec(dllexport)
#else
    #define API __attribute__((__visibility__("default")))
#endif

extern "C"{
    API void convert_index(char** index, int len_index, char** timeframes){
        // =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        // Index    
        std::vector<std::string> v_index(index, index+len_index);

        // Timeframe
        std::vector<std::string> v_timeframe(timeframes, timeframes+2);
        // =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


        // New Timeframe
        std::string timeframe_input = timeframes[0];
        std::vector<std::string> minutes_timeframe = {"1m", "2m", "5m", "15m", "30m", "60m", "90m"};
        
        std::vector<std::string> new_index;
        bool timeframe_is_minutes = isin(timeframe_input, minutes_timeframe);
        if (timeframe_is_minutes){
            new_index = convert_index_minutes(v_index, timeframe_input);
        }
        else{
            new_index;
        }
    }

}