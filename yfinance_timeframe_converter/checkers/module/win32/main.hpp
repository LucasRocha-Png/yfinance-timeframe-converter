extern "C"
{
__declspec(dllexport) int* __cdecl checker(char** index, int len_index, char** columns, int len_columns, char** timeframes);

__declspec(dllexport) void  __cdecl free_array(int* array);
} 