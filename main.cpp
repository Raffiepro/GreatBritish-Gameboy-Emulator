#include"sm83.hpp"
#include<assert.h>

int main()
{
    sm83 cpu;
    s8 sigma = -1;
    setBit(cpu.f,fz,false);
    std::cout<<cpu.pc<<'\n';
    cpu.JR(cnz, &sigma);
    assert(cpu.pc==255);
    assert(((s8)0x2F)>0);

    cpu.pc = 0x100;
    cpu.loadFile("Tetris (World) (Rev A).gb");
    cpu.bus[0xFF44] = 0x94;

    while(true)
    {
        // THE REASON I HAVE COMMENTED OUT NEARLY ALL DEBUG INFO IS BECAUSE I AM TRYING TO CODE THE MISSING OPCODES AS FAST AS I CAN
        //getchar();
        cpu.execute();
    }
    return 0;
}