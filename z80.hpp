#pragma once
#include<iostream>
#include<fstream>
#include<stdio.h>
#include"types.h"
#include"header.h"
#include"opcodes.h"

enum z80Flag : u8
{
    fz = 7, //Zero flag
    fn = 6, //Subtraction flag (BCD)
    fh = 5, //Half Carry flag (BCD)
    fc = 4 //Carry flag
};
enum z80Cond : u8
{
    cnz,
    cz,
    cnc,
    cc
};

char setBit(u8 byte, u8 bit, bool value)
{
    return value ? (byte | (1<<bit)) : (byte & ~(1<<bit));
}

struct z80
{
    u16 af=0x0100,bc=0,de=0,hl=0;
    u16 sp,pc=0x100; //Stack Pointer and Program Counter
    u8 bus[65536];

    u8* a=(u8*)&af+1;
    u8* b=(u8*)&bc+1;
    u8* c=(u8*)&bc;
    u8* d=(u8*)&de+1;
    u8* e=(u8*)&de;
    u8* h=(u8*)&hl+1;
    u8* l=(u8*)&hl;
    u8* f=(u8*)&af;

    bool jumped=false;

    void decode(u8* op);
    inline void INC(u8* reg);
    inline void INC(u16* reg){*reg++;}
    inline void DEC(u8* reg);
    inline void XOR(u8* reg){*a^=*reg;};
    inline void LD(u16* reg, u16* n16)
    {
        *reg=*n16;
    }
    inline void LD(u8* reg, u8* n8)
    {
        *reg=*n8;
    }
    inline void JR(s8 offset){pc+=offset+2;jumped=true;} //JUMP RELATIVE (+2 to include itself in the PC)
    inline void JR(z80Cond cond,s8* offset) //JUMP RELATIVE WITH CONDITION
    {
        if(cond==cnz&&*f&fz) return;
        if(cond==cz&&!(*f&fz)) return;
        if(cond==cnc&&*f&fc) return;
        if(cond==cc&&!(*f&fc)) return;
        pc+=*offset+2;  jumped=true;
    }

    void printRegs()
    {
        printf("A: %02X  F: %02X  (AF: %04X)\nB: %02X  C: %02X  (BC: %04X)\nD: %02X  E: %02X  (DE: %04X)\nH: %02X  L: %02X  (HL: %04X)\nPC: %04X\n",
            *a,*f,af,*b,*c,bc,*d,*e,de,*h,*l,hl,pc);
    }

    void next()
    {
        pc += unprefixed[bus[pc]].bytes;
    }
    void execute()
    {
        decode(&bus[pc]);
        if(!jumped) next();
        else jumped=false;
        printRegs();
    }
    void loadFile(const char* filename)
    {
        std::ifstream f(filename, std::ios_base::binary | std::ios_base::ate);
        size_t size = f.tellg();
        if(size>sizeof(bus)) {std::cout<<"ROM TOO BEEG!!\n";return;}
        f.seekg(0);
        f.read((char*)&bus,size);
        f.close();
        std::cout<<"Name: "<<headerFromBus(bus).title<<" size: "<<size<<"B "<<((float)size/sizeof(bus))*100<<"\% usage of total memory\n";
    }
};

inline void z80::INC(u8* reg)
{
    setBit(*f,fh,(*reg&0x0F + 1) > 0x0F);
    *reg++;
    setBit(*f,fz,*reg==0);
    setBit(*f,fn,0);
}
inline void z80::DEC(u8* reg)
{
    setBit(*f,fh,(*reg&0x0F + 1) > 0x0F);
    *reg-=1;
    setBit(*f,fz,*reg==0);
    setBit(*f,fn,1);
}

//LD HL n16 (0x21) DONE
//LD C n8 (0x0E) DONE
//LD B n8 (0x06) DONE
//LD [HL-] A (0x32) DONE
//DEC B (0x05) DONE
//JR NZ e8 (0x20) DONE

void z80::decode(u8* op)
{
    printf("%s (%02X)\n",unprefixed[*op].mnemonic,*op); 
    const u8 length = unprefixed[*op].bytes;
    switch(*op)
    {
        case 0x00: break;
        case 0x05: DEC(b); break;
        case 0x06: LD(b,op+1); break;
        case 0x0E: LD(c,op+1); break;
        case 0x20: JR(cnz,(s8*)(op+1));
        case 0x21: LD(&hl,(u16*)(op+1)); break;
        case 0x2C: INC(l); break;
        case 0x32: LD(&bus[hl],a); hl--; break; //LD [HL-] A (0x32)
        case 0xC3:
        {
            pc=*(u16*)(op+1);
            jumped=true;
            break;
        }
        case 0xAF: XOR(a); break;
        default:
            printf("Missing code");
    }
}