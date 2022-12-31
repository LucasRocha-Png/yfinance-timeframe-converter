#include <vector>
#include <string>
#include <iostream>

#include "converter.hpp"
#include "utils.hpp"
#include "global_variables.hpp"


std::vector<std::string> convert_index_(std::vector<std::string>& index, std::string& timeframe_input, std::string& timeframe_output){
    /*
    Converts the index
    */


    // Gets keymap from index
    std::pair<std::string, std::string> key_map_ = key_map[timeframe_output]; // Returns the period of the timeframe and the division: {"minute", "2"}
    std::pair<int, int> location_value_ = location_value[key_map_.first]; // Returns the location at the string of the period; Starts at 14 and ends 2 values after: {14,2}                            


    std::vector<std::string> new_index; 
    std::string type_of_convertion = key_map_.second;

    int last_value = std::stoi(index[0].substr(location_value_.first, location_value_.second));

    // if type of convertion is change
    if (type_of_convertion == "change"){
        for (std::string& line : index){
            int time = std::stoi(line.substr(location_value_.first, location_value_.second)); // Takes the time in the string and converts it to int
            if (time != last_value){
                new_index.push_back(line);
                last_value = time;
            }
        }
    }

    // If is convert "to weak"
    else if (type_of_convertion == "convert"){
    }

    // If it's a number "division"
    else {
        int divisior = std::stoi(type_of_convertion);
        long int loop = 0;
        for (std::string& line : index){
            int time = std::stoi(line.substr(location_value_.first, location_value_.second)); // Takes the time in the string and converts it to int
            if (time == 0 || time % divisior == 0 || loop == 0){
                new_index.push_back(line);
            }
            loop += 1;
        }
    }


    for (std::string line : new_index){
        std::cout << line << "\n";
    }

    return index;
}