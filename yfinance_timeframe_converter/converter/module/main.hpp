#pragma once

#ifdef _WIN32
    #define API __declspec(dllexport)
#else
    #define API __attribute__((__visibility__("default")))
#endif

extern "C"{
    API void convert_index(char** index, int len_index, char** timeframes);
}