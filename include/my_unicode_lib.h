#pragma once


#ifdef _WIN32
  #define MY_UNICODE_LIB_EXPORT __declspec(dllexport)
#else
  #define MY_UNICODE_LIB_EXPORT
#endif

MY_UNICODE_LIB_EXPORT void my_unicode_lib();
