

extern "C"{
    __attribute__((__visibility__("default"))) void convert_timeframe(char** index, int len_index, char** columns, int len_columns, double* values, int len_values, char** timeframes);

    __attribute__((__visibility__("default"))) void convert_index(char** index, int len_index, char** columns, int len_columns, double* values, int len_values, char** timeframes);
}