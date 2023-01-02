#pragma once

bool isin(std::string& object, std::vector<std::string>& list);

int getDayOfWeek(int day, int month, int year);

char** vector_to_p(std::vector<std::string>& list);

double* vector_to_p(std::vector<double>& list);

double return_value_based_on_mask(std::vector<double>& list, std::string& mask);

std::vector<std::vector<double>> to_matrix(const std::vector<double>& list, int num_rows);

std::vector<std::vector<double>> transpose(const std::vector<std::vector<double>>& matrix);
