#include"sm83.hpp"
#include<assert.h>
#include<time.h>

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
        cpu.bus[0xFF44]+=1;
        cpu.bus[0xFF44]%=154;
        cpu.execute();
    }
    return 0;
}