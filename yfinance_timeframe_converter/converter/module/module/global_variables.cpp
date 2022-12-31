#include <string>
#include <map>
#include "global_variables.hpp"


/*
Creates the keymap from each timeframe
*/
std::map<std::string, std::pair<std::string, std::string>> key_map = {
  {"2m", {"minute", "2"}},
  {"3m", {"minute", "3"}},
  {"5m", {"minute", "5"}},
  {"15m", {"minute", "15"}},
  {"30m", {"minute", "30"}},
  {"60m", {"hour", "change"}},
  {"1h", {"hour", "change"}},
  {"2h", {"hour", "2"}},
  {"3h", {"hour", "3"}},
  {"4h", {"hour", "4"}},
  {"1d", {"day", "change"}},
  {"1wk", {"day", "convert"}},
  {"1mo", {"month", "change"}},
  {"3mo", {"month", "3"}},
  {"6mo", {"month", "6"}},
  {"1yr", {"year", "change"}},
};

/*
Creates de location of the value at the string from each type of time.

Test string was: "2022-12-19 09:30:00"
*/
std::map<std::string, std::pair<int, int>> location_value = {
  {"minute", {14,2}},
  {"hour", {11,2}},
  {"day", {8,2}},
  {"month", {5,2}},
  {"year", {0, 4}}
};