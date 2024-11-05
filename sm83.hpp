#pragma once
#include<iostream>
#include<fstream>
#include<stdio.h>
#include"types.h"
#include"header.h"
#include"opcodes.h"


enum sm83Flag : u8
{
    fz = 7, //Zero flag
    fn = 6, //Subtraction flag (BCD)
    fh = 5, //Half Carry flag (BCD)
    fc = 4 //Carry flag
};
enum sm83Cond : u8
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

struct sm83
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

    bool decode(u8* op);
    bool cb_decode(u8* op);
    inline void ADD(u8* reg, u8* n);
    inline void ADDHL(u16& reg);
    inline void SUB(u8* reg, u8* n);
    inline void CP(u8* reg, u8* n);
    inline void INC(u8* reg);
    inline void DEC(u8* reg);
    inline void OR(u8* other){*a|=*other; setBit(f,fz,*a==0); setBit(f,fn,0);setBit(f,fh,0);setBit(f,fc,0);}
    inline void AND(u8* other){*a&=*other; setBit(f,fz,*a==0); setBit(f,fn,0);setBit(f,fh,1);setBit(f,fc,0);}
    inline void XOR(u8* other){*a^=*other; setBit(f,fz,*a==0); setBit(f,fn,0);setBit(f,fh,0);setBit(f,fc,0);}
    void LD(u16* dst, u16* src)
    {
        *dst=*src;
    }
    void LD(u8* dst, u8* src)
    {
        *dst=*src;
    }
    inline void JR(s8 offset){pc+=offset+2;jumped=true;} //JUMP RELATIVE (+2 to include itself in the PC)
    inline bool JR(sm83Cond cond, s8* offset) // JUMP RELATIVE WITH CONDITION
    {
        if (cond == cnz && (*f & 0x80)) return false; // Check Zero flag
        if (cond == cz && !(*f & 0x80)) return false;
        if (cond == cnc && (*f & 0x10)) return false; // Check Carry flag
        if (cond == cc && !(*f & 0x10)) return false;

        //I am adding the required offset to pc in the instruction itself
        pc += (*offset);
        jumped = true;
        return true;
    }
    inline void POP(u16& to)
    {
        to=(u16)bus[sp];
        sp+=1;
        to|=((u16)bus[sp])<<8;
        sp+=1;
    }
    inline void POP(u8& to)
    {
        to=bus[sp];
        sp+=1;
    }
    inline void PUSH(u16& data)
    {
        sp-=2;
        *(u16*)&bus[sp]=data;
    }
    inline void PUSH(u8& data)
    {
        sp-=1;
        bus[sp]=data;
    }

    void printRegs()
    {
        printf("A: %02X  F: %02X  (AF: %04X)\nB: %02X  C: %02X  (BC: %04X)\nD: %02X  E: %02X  (DE: %04X)\nH: %02X  L: %02X  (HL: %04X)\nPC: %04X\n",
            *a,*f,af,*b,*c,bc,*d,*e,de,*h,*l,hl,pc);
    }

    void next()
    {
        if(bus[pc]!=0xCB) pc += unprefixed[bus[pc]].bytes;
        else pc += (cbprefixed[bus[pc+1]].bytes);
    }
    bool missing_opcode=false;
    bool EI_executed=false;
    void execute()
    {
        bool prev_EI_executed=EI_executed; //EI HANDLING
        if(bus[pc]==0x00&&pc!=0x100)
        {
            printf("Null\n");
            exit(0);
        }
        if(!decode(&bus[pc])) missing_opcode=true;
        if(prev_EI_executed != EI_executed) {IME=true; EI_executed=false;} //ALSO EI HANDLING
        
        printRegs();

        if(!jumped) next();
        else jumped=false;
        if(missing_opcode) getchar();
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

inline void sm83::ADD(u8* reg, u8* n)
{
    u8 hctest = *reg&0x0F; hctest+=*n;
    setBit(f,fh,hctest > (u8)0x0F);
    *reg+=*n;
    setBit(f,fz,*reg==0);
    setBit(f,fn,0);
    setBit(f,fc,*n>*reg); //Set if borrow
}
inline void sm83::ADDHL(u16& reg)
{
    u8 hctest = hl&0x0F; hctest+=reg;
    setBit(f,fh,hctest > (u8)0x0F);
    hl+=reg;
    setBit(f,fz,hl==0);
    setBit(f,fn,0);
    setBit(f,fc,reg>hl); //Set if borrow
}
inline void sm83::SUB(u8* reg, u8* n)
{
    u8 hctest = *reg&0x0F; hctest-=*n;
    setBit(f,fh,hctest > (u8)0x0F);
    *reg-=*n;
    setBit(f,fz,*reg==0);
    setBit(f,fn,1);
    setBit(f,fc,*n>*reg); //Set if borrow 
}
inline void sm83::CP(u8* reg, u8* n)
{
    u8 hctest = *reg&0x0F; hctest-=*n;
    setBit(f,fh,hctest > (u8)0x0F);
    u8 comparison = *reg;
    comparison-=*n;
    setBit(f,fz,comparison==0);
    setBit(f,fn,1);
    setBit(f,fc,*n>comparison); //Set if borrow (set if r8 > A)
}
inline void sm83::INC(u8* reg)
{
    u8 hctest = *reg&0x0F; hctest+=1;
    setBit(f,fh,hctest > (u8)0x0F);
    *reg+=1;
    setBit(f,fz,*reg==0);
    setBit(f,fn,0);
}
inline void sm83::DEC(u8* reg)
{
    u8 hctest = *reg&0x0F; hctest-=1;
    setBit(f,fh,hctest > (u8)0x0F);
    *reg-=1;
    setBit(f,fz,*reg==0);
    setBit(f,fn,1);
}

bool sm83::decode(u8* op)
{
    printf("%s (%02X",unprefixed[*op].mnemonic,*op);
    for(int i=1;i<unprefixed[*op].bytes;i++)
    {
        printf(" %02X",*(op+i));
    }
    printf(") %04X\n",pc);

    const u8 length = unprefixed[*op].bytes;
    switch(*op)
    {
        case 0x00: break;
        case 0x01: LD(&bc,(u16*)(op+1)); break;
        case 0x05: DEC(b); break;
        case 0x06: LD(b,op+1); break;
        case 0x0B: bc-=1; break;
        case 0x0C: INC(c); break;
        case 0x0D: DEC(c); break;
        case 0x0E: LD(c,op+1); break;
        case 0x11: LD(&de,(u16*)(op+1)); break;
        case 0x12: LD(&bus[de],a); break;
        case 0x13: de+=1; break;
        case 0x16: LD(d,op+1); break;
        case 0x19: ADDHL(de); break;
        case 0x1A: LD(a,&bus[de]); break;
        case 0x20: if(JR(cnz,(s8*)(op+1))) {pc+=2;} break;
        case 0x21: LD(&hl,(u16*)(op+1)); break;
        case 0x22: LD(&bus[hl],a); hl+=1; break; //LD [HL-] A
        case 0x23: hl+=1; break;
        case 0x2A: LD(a,&bus[hl]); hl+=1; break; //LD A, [HL+]
        case 0x2C: INC(l); break;
        case 0x2F: *a=~*a; setBit(f,fn,1); setBit(f,fh,1); break;
        case 0x31: LD(&sp,(u16*)(op+1)); break;
        case 0x32: LD(&bus[hl],a); hl-=1; break; //LD [HL-] A
        case 0x36: LD(&bus[hl],op+1); break; //LDH A, [a8]
        case 0x3E: LD(a,op+1); break;
        case 0x47: LD(b,a); break;
        case 0x4F: LD(c,a); break;
        case 0x56: LD(d,&bus[hl]); break;
        case 0x5E: LD(e,&bus[hl]); break;
        case 0x5F: LD(e,a); break;
        case 0x78: LD(a,b); break;
        case 0x79: LD(a,c); break;
        case 0x7C: LD(a,h); break;
        case 0x87: ADD(a,a); break;
        case 0xC9: printf("RET FROM: %04X ",pc); POP(pc); jumped=true; printf("TO: %04X",pc); getchar(); break;
        case 0xA1: AND(c); break;
        case 0xA3: AND(e); break;
        case 0xA9: XOR(c); break;
        case 0xAF: XOR(a); break;
        case 0xB0: OR(b); break;
        case 0xB1: OR(c); break;
        case 0xC3: pc=*(u16*)(op+1); jumped=true; break;
        case 0xCB: return cb_decode(op+1);
        case 0xCD: //This pushes the address of the instruction after the CALL on the stack, such that RET can pop it later; then, it executes an implicit JP n16 -RGBDS DOCS
        {
            u16 retaddr=pc+3;
            PUSH(retaddr);
            pc=*(u16*)(op+1);
            jumped=true;
        }
            printf("CALL FROM: %04X TO: %04X",(*(u16*)&bus[sp])-3,pc);
            getchar();
            break;
        case 0xD1: POP(de); break;
        case 0xD5: PUSH(de); break;
        case 0xE0: LD(&bus[(u16)0xFF00 + *(op+1)],a); break; //LDH [a8], A
        case 0xE1: POP(hl); break;
        case 0xE2: LD(&bus[(u16)0xFF00+*c],a); break; //LD [$FF00+C],A
        case 0xE5: PUSH(hl); break;
        case 0xE6: AND(op+1); break;
        case 0xE9: pc=hl; jumped=true; break;
        case 0xEA: LD(&bus[*(u16*)(op+1)], a); break; //LD [a16], A
        case 0xEF: {u16 retaddr=pc+1; PUSH(retaddr); pc=0x28; jumped=true;} printf("RST FROM: %04X TO: %04X",(*(u16*)&bus[sp])-1,pc); getchar(); break; //RST $28
        case 0xF0: LD(a,&bus[(u16)0xFF00 + *(op+1)]); break; //LDH A, [a8]
        case 0xF3: IME=false; break; //DI (DISABLE INTERRUPT)
        case 0xFB: EI_executed=true; break; //EI (ENABLE INTERRUPT) ONLY EXECUTED [AFTER] THE NEXT INSTRUCTION
        case 0xFE: CP(a,op+1); break; //CP A n8
        default:
            printf("Missing opcode\n");
            printf("%s (%02X",unprefixed[*op].mnemonic,*op);
            for(int i=1;i<unprefixed[*op].bytes;i++)
            {
                printf(" %02X",*(op+i));
            }
            printf(")\n");
            printRegs();
            return false;
    }
    return true;
}

bool sm83::cb_decode(u8* op)
{
    printf("%s (%02X",cbprefixed[*op].mnemonic,*op);
    for(int i=1;i<cbprefixed[*op].bytes-1;i++)
    {
        printf(" %02X",*(op+i));
    }
    printf(") %04X\n",pc);
    switch(*op)
    {
        case 0x37: *a = (*a << 4) | (*a >> 4); *f=0; setBit(f,fz,*a==0); break;
        case 0x87: setBit(a,0,0); break;
        default:
            printf("Missing opcode\n");
            printf("%s (%02X",cbprefixed[*op].mnemonic,*op);
            for(int i=1;i<cbprefixed[*op].bytes-1;i++)
            {
                printf(" %02X",*(op+i));
            }
            printf(")\n");
            printRegs();
            return false;
    }
    return true;
}