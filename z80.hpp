#pragma once
#include<iostream>
#include<fstream>
#include"types.h"
#include"header.h"
#include"opcodes.h"

struct z80
{
    u16 af,bc,de,hl;
    u16 sp,pc=0x100; //Stack Pointer and Program Counter
    u8 bus[65536];

    void decode(u8* op)
    {
        std::cout<<unprefixed[*op].mnemonic;
    }
    void next()
    {
        pc += unprefixed[bus[pc]].bytes;
    }
    void execute()
    {
        decode(&bus[pc]);
        next();
    }
    void loadFile(const char* filename)
    {
        std::ifstream f(filename, std::ios_base::binary | std::ios_base::ate);
        size_t size = f.tellg();
        if(size>sizeof(bus)) {std::cout<<"ROM TOO BEEG!!\n";return;}
        f.seekg(0);
        f.read((char*)&bus,size);
        f.close();
    }
};