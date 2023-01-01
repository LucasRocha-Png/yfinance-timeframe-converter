#pragma once

#ifdef _WIN32
    #define API __declspec(dllexport)
#else
    #define API __attribute__((__visibility__("default")))
#endif

extern "C"{
    API char** convert_index(char** index, int len_index, char** timeframes);

    API void convert_values(double** values, char** index, char** converted_index, char** columns);

    API void free_array_char(char** array);

    API void free_array_double(double** array);
}