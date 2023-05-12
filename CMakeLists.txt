cmake_minimum_required(VERSION 3.15)
project(my_unicode_lib CXX)




add_library(my_unicode_lib src/my_unicode_lib.cpp)
target_include_directories(my_unicode_lib PUBLIC include)



set_target_properties(my_unicode_lib PROPERTIES PUBLIC_HEADER "include/my_unicode_lib.h")
install(TARGETS my_unicode_lib)
