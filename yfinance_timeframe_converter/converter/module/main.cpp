#include <vector>
#include <string>
#include <iterator>

#include "main.hpp"
#include "module/converter.hpp"

#ifdef _WIN32
    #define API __declspec(dllexport)
#else
    #define API __attribute__((__visibility__("default")))
#endif

extern "C"{
    API void convert_index(char** index, int len_index, char** timeframes){
        /*
        Threats the data and pass it to the convert_index_ function 
        */

        
        std::vector<std::string> v_index(index, index+len_index); // Index            
        std::vector<std::string> v_timeframe(timeframes, timeframes+2); // Timeframe

        // New Timeframe
        std::string timeframe_input = timeframes[0];
        std::string timeframe_output = timeframes[1];
        
        std::vector<std::string> new_index = convert_index_(v_index, timeframe_input, timeframe_output);
    }

}