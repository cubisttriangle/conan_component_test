cmake_minimum_required(VERSION 3.15)
project(my_unicode_lib CXX)

if (WIN32)
  message(FATAL "Unsupported OS, Windows. Use linux.")
endif()

find_package(ICU REQUIRED i18n)
add_library(my_unicode_lib src/my_unicode_lib.cpp)
target_include_directories(my_unicode_lib PUBLIC include)
target_link_libraries(my_unicode_lib PRIVATE ICU::i18n)

set_target_properties(my_unicode_lib PROPERTIES PUBLIC_HEADER "include/my_unicode_lib.h")
install(TARGETS my_unicode_lib)
