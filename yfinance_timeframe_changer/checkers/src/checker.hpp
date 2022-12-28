#pragma once

#include <string>
#include <vector>

// Checks if the inputs passed by the user exists
int checks_if_timeframes_exists(std::vector<std::string>& timeframes);

// Checks if the input is lower than output, if no, it will cause an error
int checks_if_input_is_lower_than_output(std::vector<std::string>& timeframes);

// Checks if columns exists
int checks_if_columns_exists(std::vector<std::string>& columns);

// Checks if index is equal than timeframe
int checks_if_index_is_equal_than_timeframe(std::vector<std::string>& index, std::string& timeframe);