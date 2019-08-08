//==============================================================================
// File: func.cpp
// Author: Cristiano Pedrassani Costa Neves
// Date:17 jul 2019
// Brief: C/C++ function.
//==============================================================================

//==============================================================================
// Compile
//g++ -fPIC -o func.o -c func.cpp
//g++ -shared -fPIC -o libfunc.so func.o -pthread

//==============================================================================
// Includes

//---------------------------------------
// Std C++
#include <iostream>

//---------------------------------------
#include "func.h"


//==============================================================================
// Public Functions

//---------------------------------------------------------------------------
int my_c_function(int var1, char * var2, my_c_type * var3)
{
    std::cout << "C/C++ Function, var1: " << var1 << " var2: " << var2 << std::endl;
    std::cout << "C/C++ Function, var3.field1: " << var3->field1 << " var3.field2: " << var3->field2 << std::endl;
    return 0;
}
