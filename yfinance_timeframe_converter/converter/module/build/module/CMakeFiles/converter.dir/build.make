# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/build"

# Include any dependencies generated for this target.
include module/CMakeFiles/converter.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include module/CMakeFiles/converter.dir/compiler_depend.make

# Include the progress variables for this target.
include module/CMakeFiles/converter.dir/progress.make

# Include the compile flags for this target's objects.
include module/CMakeFiles/converter.dir/flags.make

module/CMakeFiles/converter.dir/index.cpp.o: module/CMakeFiles/converter.dir/flags.make
module/CMakeFiles/converter.dir/index.cpp.o: ../module/index.cpp
module/CMakeFiles/converter.dir/index.cpp.o: module/CMakeFiles/converter.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object module/CMakeFiles/converter.dir/index.cpp.o"
	cd "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/build/module" && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT module/CMakeFiles/converter.dir/index.cpp.o -MF CMakeFiles/converter.dir/index.cpp.o.d -o CMakeFiles/converter.dir/index.cpp.o -c "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/module/index.cpp"

module/CMakeFiles/converter.dir/index.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/converter.dir/index.cpp.i"
	cd "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/build/module" && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/module/index.cpp" > CMakeFiles/converter.dir/index.cpp.i

module/CMakeFiles/converter.dir/index.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/converter.dir/index.cpp.s"
	cd "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/build/module" && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/module/index.cpp" -o CMakeFiles/converter.dir/index.cpp.s

module/CMakeFiles/converter.dir/utils.cpp.o: module/CMakeFiles/converter.dir/flags.make
module/CMakeFiles/converter.dir/utils.cpp.o: ../module/utils.cpp
module/CMakeFiles/converter.dir/utils.cpp.o: module/CMakeFiles/converter.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object module/CMakeFiles/converter.dir/utils.cpp.o"
	cd "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/build/module" && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT module/CMakeFiles/converter.dir/utils.cpp.o -MF CMakeFiles/converter.dir/utils.cpp.o.d -o CMakeFiles/converter.dir/utils.cpp.o -c "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/module/utils.cpp"

module/CMakeFiles/converter.dir/utils.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/converter.dir/utils.cpp.i"
	cd "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/build/module" && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/module/utils.cpp" > CMakeFiles/converter.dir/utils.cpp.i

module/CMakeFiles/converter.dir/utils.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/converter.dir/utils.cpp.s"
	cd "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/build/module" && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/module/utils.cpp" -o CMakeFiles/converter.dir/utils.cpp.s

module/CMakeFiles/converter.dir/global_variables.cpp.o: module/CMakeFiles/converter.dir/flags.make
module/CMakeFiles/converter.dir/global_variables.cpp.o: ../module/global_variables.cpp
module/CMakeFiles/converter.dir/global_variables.cpp.o: module/CMakeFiles/converter.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object module/CMakeFiles/converter.dir/global_variables.cpp.o"
	cd "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/build/module" && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT module/CMakeFiles/converter.dir/global_variables.cpp.o -MF CMakeFiles/converter.dir/global_variables.cpp.o.d -o CMakeFiles/converter.dir/global_variables.cpp.o -c "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/module/global_variables.cpp"

module/CMakeFiles/converter.dir/global_variables.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/converter.dir/global_variables.cpp.i"
	cd "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/build/module" && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/module/global_variables.cpp" > CMakeFiles/converter.dir/global_variables.cpp.i

module/CMakeFiles/converter.dir/global_variables.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/converter.dir/global_variables.cpp.s"
	cd "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/build/module" && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/module/global_variables.cpp" -o CMakeFiles/converter.dir/global_variables.cpp.s

# Object files for target converter
converter_OBJECTS = \
"CMakeFiles/converter.dir/index.cpp.o" \
"CMakeFiles/converter.dir/utils.cpp.o" \
"CMakeFiles/converter.dir/global_variables.cpp.o"

# External object files for target converter
converter_EXTERNAL_OBJECTS =

module/libconverter.a: module/CMakeFiles/converter.dir/index.cpp.o
module/libconverter.a: module/CMakeFiles/converter.dir/utils.cpp.o
module/libconverter.a: module/CMakeFiles/converter.dir/global_variables.cpp.o
module/libconverter.a: module/CMakeFiles/converter.dir/build.make
module/libconverter.a: module/CMakeFiles/converter.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX static library libconverter.a"
	cd "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/build/module" && $(CMAKE_COMMAND) -P CMakeFiles/converter.dir/cmake_clean_target.cmake
	cd "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/build/module" && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/converter.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
module/CMakeFiles/converter.dir/build: module/libconverter.a
.PHONY : module/CMakeFiles/converter.dir/build

module/CMakeFiles/converter.dir/clean:
	cd "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/build/module" && $(CMAKE_COMMAND) -P CMakeFiles/converter.dir/cmake_clean.cmake
.PHONY : module/CMakeFiles/converter.dir/clean

module/CMakeFiles/converter.dir/depend:
	cd "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/build" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module" "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/module" "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/build" "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/build/module" "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-converter/yfinance_timeframe_converter/converter/module/build/module/CMakeFiles/converter.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : module/CMakeFiles/converter.dir/depend

