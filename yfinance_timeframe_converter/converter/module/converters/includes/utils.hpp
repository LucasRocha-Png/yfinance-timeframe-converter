#pragma once

bool isin(std::string& object, std::vector<std::string>& list);

int getDayOfWeek(int day, int month, int year);

int get_index(std::vector<std::string>& list, std::string& word);

char** vector_to_p(std::vector<std::string>& list);

double return_value_based_on_mask(std::vector<double>& list, std::string& mask);

std::vector<std::vector<double>> to_matrix(const std::vector<double>& list, int num_rows);
