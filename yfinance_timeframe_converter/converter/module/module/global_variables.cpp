#include <string>
#include <map>
#include "global_variables.hpp"


/*
Creates the keymap from each timeframe
*/
std::map<std::string, std::pair<std::string, std::string>> key_map = {
  {"2m", {"minute", "2"}},
  {"3m", {"minute", "3"}},
  {"4m", {"minute", "4"}},
  {"5m", {"minute", "5"}},
  {"6m", {"minute", "6"}},
  {"10m", {"minute", "10"}},
  {"12m", {"minute", "12"}},
  {"15m", {"minute", "15"}},
  {"20m", {"minute", "20"}},
  {"30m", {"minute", "30"}},
  {"60m", {"hour", "1"}},
  {"90m", {"hour", "90"}},

  {"1h", {"hour", "1"}},
  {"2h", {"hour", "2"}},
  {"3h", {"hour", "3"}},
  {"4h", {"hour", "4"}},
  {"6h", {"hour", "6"}},
  {"8h", {"hour", "8"}},
  {"12h", {"hour", "12"}},


  {"1d", {"day", "1"}},
  {"2d", {"day", "2"}},
  {"3d", {"day", "3"}},
  {"5d", {"day", "5"}},
  {"6d", {"day", "6"}},
  {"10d", {"day", "10"}},
  {"15d", {"day", "15"}},

  {"1wk", {"day", "convert"}},
  {"1mo", {"month", "1"}},
  {"2mo", {"month", "2"}},
  {"3mo", {"month", "3"}},
  {"4mo", {"month", "4"}},
  {"6mo", {"month", "6"}},
  {"1yr", {"year", "1"}},
  {"2yr", {"year", "2"}},
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