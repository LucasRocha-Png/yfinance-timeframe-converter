#include <vector>
#include <string>

#include "../includes/index.hpp"
#include "../includes/utils.hpp"
#include "../includes/global_variables.hpp"


std::vector<std::string> convert_index_(std::vector<std::string>& index, std::string& timeframe_output){
    /*
    Converts the index
    */


    // Gets keymap from index
    std::pair<std::string, std::string> key_map_ = key_map[timeframe_output]; // Returns the period of the timeframe and the division: {"minute", "2"}
    std::pair<int, int> location_value_ = location_value[key_map_.first]; // Returns the location at the string of the period; Starts at 14 and ends 2 values after: {14,2}  

    // Create vector for the filtered index
    std::vector<std::string> filtered_index; 

    // Get type of output
    std::string output_type = key_map_.first;          

    // Get the type of convertion {"change", "week", divisor: "2, 3"...}                
    std::string type_of_convertion = key_map_.second;

    // Create divisor if type_of_convertion != of change and converter    
    int divisor;
    if (type_of_convertion != "change" && type_of_convertion != "converter"){
        divisor = std::stoi(type_of_convertion);
    }

    // Create day of week if its a week
    std::vector<int> list_day_week;
    if (output_type == "week"){
        int day;
        int month;
        int year;
        int day_of_week;
        for (std::string& date : index){
            day = std::stoi(date.substr(8, 2));
            month = std::stoi(date.substr(5, 2));
            year = std::stoi(date.substr(0, 4));
            day_of_week = getDayOfWeek(day, month, year);
            list_day_week.push_back(day_of_week);
        }
    }

    // Last value of the loop
    int last_value = -1;
    int last_day_of_week = 1;
    int current_minute = -1;
    int inicial_minute;
    unsigned long loop = 0;
    int day_of_week;
    bool should_add;

    for (std::string& date : index){
        int value = std::stoi(date.substr(location_value_.first, location_value_.second));
        should_add = false;

        // If the type of convertion is when the value changes
        // If its to convert (week)
        if (type_of_convertion == "converter"){
            continue;
        }

        // If it a divisor
        else{
            // If its a month!
            if (output_type == "month"){
                if (((value % divisor == 0 && value != last_value) && value != 12) || (value == 1 && value != last_value)){
                    should_add = true;
                    last_value = value;
                }
            }

            // If its a week!
            else if(output_type == "week"){
                day_of_week = list_day_week[loop];
                if (day_of_week <= last_day_of_week && value != last_value){
                    should_add = true;
                    last_value = value;
                }
                last_day_of_week = day_of_week;
            }

            // If its a hour
            else if (output_type == "hour"){
                current_minute = std::stoi(date.substr(14, 2));

                if (((loop == 0) && (value % divisor == 0 && value != last_value)) || (value % divisor == 0 && value != last_value && current_minute == inicial_minute)){
                    should_add = true;
                    last_value = value;
                }

                if (loop == 0){
                    inicial_minute = std::stoi(date.substr(14, 2));
                }
            }

            // If its a Year, Day or minute
            else {
                if (value % divisor == 0 && value != last_value){
                    should_add = true;
                    last_value = value;
                }
            }
        }

        if (should_add){
            filtered_index.push_back(date);
        }

        loop += 1;
    }


    filtered_index.insert(filtered_index.begin(), std::to_string(filtered_index.size()));

    return filtered_index;
}