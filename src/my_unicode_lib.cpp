#include "my_unicode_lib.h"

#include <iostream>

#define U_USING_ICU_NAMESPACE 1
#include <unicode/coll.h>
#include <unicode/locid.h>


void my_unicode_lib()
{
    std::cout << "start" << std::endl;

    Locale locale = Locale::getUS();
    UErrorCode status = U_ZERO_ERROR;
    Collator* collator = Collator::createInstance(locale, status);
    if (U_SUCCESS(status))
        std::cout << "Successfully created collator" << std::endl;
    else
        std::cerr << "Failed to create collator: " << status << std::endl;
    delete collator;

    std::cout << "end" << std::endl;
}
