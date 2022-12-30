#include <vector>
#include <string>
#include <iterator>
#include "main.hpp"
#include "module/converter.hpp"
#include "module/index.hpp"


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

        
    }

}