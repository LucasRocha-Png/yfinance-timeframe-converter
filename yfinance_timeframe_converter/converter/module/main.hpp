#pragma once

#ifdef _WIN32
    #define API __declspec(dllexport)
#else
    #define API __attribute__((__visibility__("default")))
#endif

extern "C"{
    API char** convert_index(char** index, int lenght_index, char** timeframes);

    API double* convert_values(double* values, int lenght_values, char** index, int lenght_index, char** converted_index, int lenght_coverted_index, char** columns, int lenght_columns);

    API void free_array_char(char** array, int size);

    API void free_array_double(double* array);
}