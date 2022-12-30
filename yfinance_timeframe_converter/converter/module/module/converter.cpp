#include <vector>
#include <string>
#include <map>

#include "converter.hpp"
#define PAIR_ std::pair<std::string, std::string>


std::vector<std::string> convert_index_(std::vector<std::string>& index, std::string& timeframe_input, std::string& timeframe_output){
    /*
    Converts the index
    */

                                          //                                                   
    std::map<std::string, PAIR_> key_map; // Dict with key_maps. Structure = "Name" - ("minutes", "hour"..., divided by ["0", "1"])

    key_map["2m"] = PAIR_("minute", "2");
    key_map["3m"] = PAIR_("minute", "3");
    key_map["5m"] = PAIR_("minute", "5"); 
    key_map["15m"] = PAIR_("minute", "15");
    key_map["30m"] = PAIR_("minute", "30");
    key_map["60m"] = PAIR_("hour", "change");
    key_map["1h"] = PAIR_("hour", "change");
    key_map["2h"] = PAIR_("hour", "2");
    key_map["3h"] = PAIR_("hour", "3");
    key_map["4h"] = PAIR_("hour", "4");
    key_map["1d"] = PAIR_("day", "change");
    key_map["1mo"] = PAIR_("month", "change");
    key_map["3mo"] = PAIR_("month", "3");
    key_map["6mo"] = PAIR_("month", "6");
    key_map["1yr"] = PAIR_("year", "change");

    for (std::string _ : index){
        continue;
    }

    return index;
}