cmake_minimum_required(VERSION 3.16)
PROJECT(STag VERSION 0.0.0 LANGUAGES CXX)

set(THREADS_PREFER_PTHREAD_FLAG ON)

find_package(Threads REQUIRED)
find_package( OpenCV REQUIRED )

FILE(GLOB all_source_files src/*.cpp)
FILE(GLOB ED_sources src/ED/*.cpp)

LIST(APPEND all_source_files ${ED_sources})

include_directories(modules/thread-pool-cpp/include)

add_executable(main ${all_source_files})
target_link_libraries(main ${OpenCV_LIBS} Threads::Threads)
