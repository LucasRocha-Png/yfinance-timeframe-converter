#pragma once

#ifdef _WIN32
    #define API __declspec(dllexport)
#else
    #define API __attribute__((__visibility__("default")))
#endif


extern "C"
{
    API int* checker(char** index, int len_index, char** columns, int len_columns, char** timeframes);

    API void free_array(int* array);
}