extern "C"
{
__attribute__((__visibility__("default"))) int* checker(char** index, int len_index, char** columns, int len_columns, char** timeframes);

__attribute__((__visibility__("default"))) void free_array(int* array);
}