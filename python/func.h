//==============================================================================
// File: func.h
// Author: Cristiano Pedrassani Costa Neves
// Date:17 jul 2019
// Brief: C/C++ function.
//==============================================================================

//==============================================================================
#ifndef __FUNC_H__
#define __FUNC_H__

//==============================================================================
// Types, Defines

typedef struct my_c_struct
{
    unsigned int field1;
    int field2;
} my_c_type;

//==============================================================================
// Public Functions

extern "C" {

int my_c_function(int var1, char * var2, my_c_type * var3);

}

#endif  // __FUNC_H__
