#pragma once

#include <stdio.h>
#include <stdlib.h>

typedef unsigned char u8;

void __stdcall setup (const u8 *skey);
void __stdcall crypt (u8 *pt, int r);
void __stdcall decrypt (u8 *ct, int r);
