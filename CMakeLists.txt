cmake_minimum_required(VERSION 3.2)
PROJECT(STag VERSION 0.0.0 LANGUAGES CXX)

set(THREADS_PREFER_PTHREAD_FLAG ON)

find_package(OpenCV REQUIRED)

FILE(GLOB all_source_files src/*.cpp)
FILE(GLOB ED_sources src/ED/*.cpp)

LIST(APPEND all_source_files ${ED_sources})

add_library(stag_lib ${all_source_files})
target_link_libraries(stag_lib ${OpenCV_LIBS})

add_executable(stag_main src/main.cpp)
target_link_libraries(stag_main ${OpenCV_LIBS} stag_lib)
