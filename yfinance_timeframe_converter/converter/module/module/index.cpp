#include <vector>
#include <string>
#include <iostream>

#include "index.hpp"
#include "utils.hpp"
#include "global_variables.hpp"


std::vector<std::string> convert_index_(std::vector<std::string>& index, std::string& timeframe_input, std::string& timeframe_output){
    /*
    Converts the index
    */


    // Gets keymap from index
    std::pair<std::string, std::string> key_map_ = key_map[timeframe_output]; // Returns the period of the timeframe and the division: {"minute", "2"}
    std::pair<int, int> location_value_ = location_value[key_map_.first]; // Returns the location at the string of the period; Starts at 14 and ends 2 values after: {14,2}  

    // Create vector for the filtered index
    std::vector<std::string> filtered_index; 

    // Get the type of convertion {"change", "weak", divisor: "2, 3"...}                          
    std::string type_of_convertion = key_map_.second;

    // Create divisor if type_of_convertion != of change and converter    
    int divisor;
    if (type_of_convertion != "change" && type_of_convertion != "converter"){
        divisor = std::stoi(type_of_convertion);
    }

    // Last value of the loop
    int last_value = -1;
    int current_minute = -1;
    int inicial_minute;
    int loop = 0;
    bool should_add;
    for (std::string& line : index){
        int time = std::stoi(line.substr(location_value_.first, location_value_.second));
        should_add = false;

        // If the type of convertion is when the value changes
        // If its to convert (weak)
        if (type_of_convertion == "converter"){
            continue;
        }

        // If it a divisor
        else{
            // If its a month!
            if (location_value_.first == 5){
                if (((time % divisor == 0 && time != last_value) && time != 12) || (time == 1 && time != last_value)){
                    should_add = true;
                    last_value = time;
                }
            }

            // If its a hour
            else if (location_value_.first == 11){
                current_minute = std::stoi(line.substr(14, 2));

                if (((loop == 0) && (time % divisor == 0 && time != last_value)) || (time % divisor == 0 && time != last_value && current_minute == inicial_minute)){
                    should_add = true;
                    last_value = time;
                }

                if (loop == 0){
                    inicial_minute = std::stoi(line.substr(14, 2));
                }
            }

            // If its a Year, Day or minute
            else {
                if (time % divisor == 0 && time != last_value){
                    should_add = true;
                    last_value = time;
                }
            }
        }

        if (should_add){
            filtered_index.push_back(line);
        }

        loop += 1;
    }


    filtered_index.insert(filtered_index.begin(), std::to_string(filtered_index.size()));

    for (std::string line : filtered_index){
        std::cout << line << "\n";
    }

    return filtered_index;
}