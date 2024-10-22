#include"z80.hpp"


int main()
{
    z80 cpu;
    cpu.loadFile("Tetris.gb");

    while(true)
    {
        getchar();
        cpu.execute();
    }
}