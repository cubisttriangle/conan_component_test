cmake_minimum_required(VERSION 3.15)
project(my_unicode_lib CXX)

if (WIN32)
  message(FATAL "Unsupported OS, Windows. Use linux.")
endif()

find_package(ICU REQUIRED i18n)
add_library(uni src/my_unicode_lib.cpp)
target_include_directories(uni PUBLIC include)
target_link_libraries(uni PRIVATE ICU::i18n)

set_target_properties(uni PROPERTIES PUBLIC_HEADER "include/my_unicode_lib.h")
install(TARGETS uni)
