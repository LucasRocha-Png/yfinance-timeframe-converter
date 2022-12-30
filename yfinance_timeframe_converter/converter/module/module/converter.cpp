#include <vector>
#include <string>
#include <map>

#include "converter.hpp"
#define VECTOR_ std::vector<std::string>
#define PAIR_ std::pair<std::string, VECTOR_>


std::vector<std::string> convert_index_(std::vector<std::string>& index, std::string& timeframe_input, std::string& timeframe_output){
    /*
    Converts the index
    */

                                          //                                                   
    std::map<std::string, PAIR_> key_map; // Dict with key_maps. Structure = "Name" - ("firt, second, day...", ["0", "1"])

    key_map["2m"] = PAIR_("minute", VECTOR_{"0", "2", "4", "6", "8"});
    key_map["5m"] = PAIR_("minute", VECTOR_{"0", "5"});
    key_map["15m"] = PAIR_("double minute", VECTOR_{"00", "15", "30"});
    key_map["30m"] = PAIR_("double minute", VECTOR_{"00", "30"});
    key_map["60m"] = PAIR_("hour", VECTOR_{"change"});
    key_map["1h"] = PAIR_("hour", VECTOR_{"change"});
    key_map["4h"] = PAIR_("hour", VECTOR_{"00", "04", "08", "12", "16", "20"});



    return index;
}