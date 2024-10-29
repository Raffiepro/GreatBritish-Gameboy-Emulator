#include"sm83.hpp"


int main()
{
    sm83 cpu;
    cpu.loadFile("Tetris.gb");
    cpu.bus[0xFF44] = 0x94;

    while(true)
    {
        // THE REASON I HAVE COMMENTED OUT NEARLY ALL DEBUG INFO IS BECAUSE I AM TRYING TO CODE THE MISSING OPCODES AS FAST AS I CAN
        //getchar();
        cpu.execute();
    }
}