#pragma once
#include <map>

extern std::map<std::string, std::string> columns_mask;

std::vector<std::string> create_columns_mask(std::vector<std::string>& columns);
