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
CMAKE_SOURCE_DIR = "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/build"

# Include any dependencies generated for this target.
include CMakeFiles/checkers.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/checkers.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/checkers.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/checkers.dir/flags.make

CMakeFiles/checkers.dir/main.cpp.o: CMakeFiles/checkers.dir/flags.make
CMakeFiles/checkers.dir/main.cpp.o: ../main.cpp
CMakeFiles/checkers.dir/main.cpp.o: CMakeFiles/checkers.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/checkers.dir/main.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/checkers.dir/main.cpp.o -MF CMakeFiles/checkers.dir/main.cpp.o.d -o CMakeFiles/checkers.dir/main.cpp.o -c "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/main.cpp"

CMakeFiles/checkers.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/checkers.dir/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/main.cpp" > CMakeFiles/checkers.dir/main.cpp.i

CMakeFiles/checkers.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/checkers.dir/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/main.cpp" -o CMakeFiles/checkers.dir/main.cpp.s

# Object files for target checkers
checkers_OBJECTS = \
"CMakeFiles/checkers.dir/main.cpp.o"

# External object files for target checkers
checkers_EXTERNAL_OBJECTS =

libcheckers.so: CMakeFiles/checkers.dir/main.cpp.o
libcheckers.so: CMakeFiles/checkers.dir/build.make
libcheckers.so: src/libchecker.a
libcheckers.so: CMakeFiles/checkers.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library libcheckers.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/checkers.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/checkers.dir/build: libcheckers.so
.PHONY : CMakeFiles/checkers.dir/build

CMakeFiles/checkers.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/checkers.dir/cmake_clean.cmake
.PHONY : CMakeFiles/checkers.dir/clean

CMakeFiles/checkers.dir/depend:
	cd "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/build" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers" "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers" "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/build" "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/build" "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/build/CMakeFiles/checkers.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/checkers.dir/depend

