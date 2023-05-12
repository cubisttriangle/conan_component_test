cmake_minimum_required(VERSION 3.15)
project(PackageTest CXX)

find_package(my_unicode_lib CONFIG REQUIRED)

add_executable(example src/example.cpp)
target_link_libraries(example my_unicode_lib::my_unicode_lib)
