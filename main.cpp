#include"sm83.hpp"
#include<assert.h>

int main()
{
    sm83 cpu;
    s8 sigma = -1;
    setBit(cpu.f,fz,false);
    cpu.JR(cnz, &sigma);
    assert(cpu.pc==255);
    assert(((s8)0x2F)>0);

    cpu.pc = 0x100;
    cpu.loadFile("Tetris (World) (Rev A).gb");
    cpu.bus[0xFF44] = 0x94;

    while(true)
    {
        cpu.execute();
    }
    return 0;
}