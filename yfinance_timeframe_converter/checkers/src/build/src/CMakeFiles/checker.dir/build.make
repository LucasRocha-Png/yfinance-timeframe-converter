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
include src/CMakeFiles/checker.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include src/CMakeFiles/checker.dir/compiler_depend.make

# Include the progress variables for this target.
include src/CMakeFiles/checker.dir/progress.make

# Include the compile flags for this target's objects.
include src/CMakeFiles/checker.dir/flags.make

src/CMakeFiles/checker.dir/checker.cpp.o: src/CMakeFiles/checker.dir/flags.make
src/CMakeFiles/checker.dir/checker.cpp.o: ../src/checker.cpp
src/CMakeFiles/checker.dir/checker.cpp.o: src/CMakeFiles/checker.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/CMakeFiles/checker.dir/checker.cpp.o"
	cd "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/build/src" && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT src/CMakeFiles/checker.dir/checker.cpp.o -MF CMakeFiles/checker.dir/checker.cpp.o.d -o CMakeFiles/checker.dir/checker.cpp.o -c "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/src/checker.cpp"

src/CMakeFiles/checker.dir/checker.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/checker.dir/checker.cpp.i"
	cd "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/build/src" && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/src/checker.cpp" > CMakeFiles/checker.dir/checker.cpp.i

src/CMakeFiles/checker.dir/checker.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/checker.dir/checker.cpp.s"
	cd "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/build/src" && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/src/checker.cpp" -o CMakeFiles/checker.dir/checker.cpp.s

# Object files for target checker
checker_OBJECTS = \
"CMakeFiles/checker.dir/checker.cpp.o"

# External object files for target checker
checker_EXTERNAL_OBJECTS =

src/libchecker.a: src/CMakeFiles/checker.dir/checker.cpp.o
src/libchecker.a: src/CMakeFiles/checker.dir/build.make
src/libchecker.a: src/CMakeFiles/checker.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX static library libchecker.a"
	cd "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/build/src" && $(CMAKE_COMMAND) -P CMakeFiles/checker.dir/cmake_clean_target.cmake
	cd "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/build/src" && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/checker.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/CMakeFiles/checker.dir/build: src/libchecker.a
.PHONY : src/CMakeFiles/checker.dir/build

src/CMakeFiles/checker.dir/clean:
	cd "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/build/src" && $(CMAKE_COMMAND) -P CMakeFiles/checker.dir/cmake_clean.cmake
.PHONY : src/CMakeFiles/checker.dir/clean

src/CMakeFiles/checker.dir/depend:
	cd "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/build" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers" "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/src" "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/build" "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/build/src" "/home/lucas/Área de Trabalho/GITHUB/yfinance-timeframe-changer/yfinance_timeframe_changer/checkers/build/src/CMakeFiles/checker.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : src/CMakeFiles/checker.dir/depend
