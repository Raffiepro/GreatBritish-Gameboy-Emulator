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

void setBit(u8* byte, u8 bit, bool value)
{
    *byte = value ? (*byte | (1<<bit)) : (*byte & ~(1<<bit));
}

struct z80
{
    u16 af=0x0100,bc=0,de=0,hl=0;
    u16 sp,pc=0x100; //Stack Pointer and Program Counter
    u8 bus[65536];

    //CPU INTERNAL FLAGS
    bool IME=true;   //Interrupt master enable flag [write only] affected by: ei, di, reti

    // The 8-bit registers of the Gameboy are actually the same 16-bit ones but cut in half :) The more you know!
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
    inline void SUB(u8* reg, u8* n, bool affect_reg);
    inline void INC(u8* reg);
    inline void INC(u16* reg){*reg++;}
    inline void DEC(u8* reg);
    inline void XOR(u8* reg){*a^=*reg;};
    inline void LD(u16* dst, u16* src)
    {
        *dst=*src;
    }
    inline void LD(u8* dst, u8* src)
    {
        *dst=*src;
    }
    inline void JR(s8 offset){pc+=offset+2;jumped=true;} //JUMP RELATIVE (+2 to include itself in the PC)
    void JR(z80Cond cond,s8* offset) //JUMP RELATIVE WITH CONDITION
    {
        //if(cond==cnz) printf("MOMOMOMO %02X %02X\n",*f,*f&0x80);
        if(cond==cnz&&*f&0x80) return; //Hacky way of checking zero flag :)
        if(cond==cz&&!(*f&80)) return;
        if(cond==cnc&&*f&0x10) return; //Hacky way of checking carry flag :)
        if(cond==cc&&!(*f&0x10)) return;
        pc+= *offset+2;  jumped=true;
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
        //printRegs();
    }
    void loadFile(const char* filename)
    {
        std::ifstream f(filename, std::ios_base::binary | std::ios_base::ate);
        size_t size = f.tellg();
        if(size>sizeof(bus)) {std::cout<<"ROM TOO BEEG!!\n";return;}
        f.seekg(0);
        f.read((char*)&bus,size);
        f.close();
        std::cout<<"Name: "<<headerFromBus(bus).title<<" size: "<<size<<"b "<<((float)size/sizeof(bus))*100<<"\% usage of total memory\n";
    }
};

inline void z80::SUB(u8* reg, u8* n, bool affect_reg=true)
{
    u8 hctest = *reg&0x0F; hctest-=*n;
    setBit(f,fh,hctest > (u8)0x0F);
    if(affect_reg)
    {
        *reg-=*n;
        setBit(f,fz,*reg==0);
        setBit(f,fn,1);
        setBit(f,fc,*n>*reg); //Set if borrow (set if r8 > A)
    }
    else
    {
        u8 test = *reg;
        test -= *n;
        setBit(f,fz,test==0);
        setBit(f,fn,1);
        setBit(f,fc,*n>test); //Set if borrow (set if r8 > A)
    }
}
inline void z80::INC(u8* reg)
{
    setBit(f,fh,(*reg&0x0F + 1) > 0x0F);
    *reg+=1;
    setBit(f,fz,*reg==0);
    setBit(f,fn,0);
}
inline void z80::DEC(u8* reg)
{
    u8 hctest = *reg&0x0F; hctest-=1;
    setBit(f,fh,hctest > (u8)0x0F);
    *reg-=1;
    setBit(f,fz,*reg==0);
    setBit(f,fn,1);
}

void z80::decode(u8* op)
{
    /*printf("%s (%02X",unprefixed[*op].mnemonic,*op);
    for(int i=1;i<unprefixed[*op].bytes;i++)
    {
        printf(" %02X",*(op+i));
    }
    printf(")\n");*/
    printf("%s (%02X)\n",unprefixed[*op].mnemonic,*op);

    const u8 length = unprefixed[*op].bytes;
    switch(*op)
    {
        case 0x00: break;
        case 0x05: DEC(b); break;
        case 0x06: LD(b,op+1); break;
        case 0x0D: DEC(c); break;
        case 0x0E: LD(c,op+1); break;
        case 0x20: JR(cnz,(s8*)(op+1)); break;
        case 0x21: LD(&hl,(u16*)(op+1)); break;
        case 0x2C: INC(l); break;
        case 0x32: LD(&bus[hl],a); hl-=1; break; //LD [HL-] A
        case 0x3E: LD(a,op+1); break;
        case 0xC3:
        {
            pc=*(u16*)(op+1);
            jumped=true;
            break;
        }
        case 0xAF: XOR(a); break;
        case 0xE0: LD(&bus[0xFF00 + *(op+1)],a); break; //LDH [a8], A
        case 0xF0: LD(a,&bus[0xFF00 + *(op+1)]); break; //LDH A, [a8]
        case 0xF3: IME=false; break; //DI (DISABLE INTERRUPTS)
        case 0xFE: SUB(a,op+1); break; //CP A n8
        default:
            printf("Missing opcode\n");
            printf("%s (%02X)\n",unprefixed[*op].mnemonic,*op);
            exit(-1);
    }
}