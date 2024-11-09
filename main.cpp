#include"sm83.hpp"
#include<assert.h>
#include"gfx.hpp"
#include<SDL2/SDL.h>
#include<thread>

SDL_Window* window;
SDL_Renderer* renderer;
sm83 cpu;

void SDLStuff()
{
    SDL_Init(SDL_INIT_EVERYTHING);
    window=SDL_CreateWindow("God Save The King!",SDL_WINDOWPOS_UNDEFINED,SDL_WINDOWPOS_UNDEFINED,160*2,144*2,0);
    renderer = SDL_CreateRenderer(window, -1, 0);
    SDL_RenderSetScale(renderer, 2, 2);
    SDL_Event event;
    while(true)
    {
        gfxUpdate(renderer, cpu.bus);
        gfxEvent(&event);
    }
}

int main()
{
    //TESTS
    u8 cpl[] = {0x2F};
    *cpu.a = 1;
    cpu.decode(cpl);
    assert(*cpu.a==254);
    cpu.af = 0x0180;
    
    cpu.JR(cz,-3);
    assert(cpu.pc==0xFF);
    cpu.pc+=1;
    cpu.JR(cnz,-3);
    assert(cpu.pc==0x100);

    cpu.loadFile("world.gb");
    cpu.bus[0xFF44] = 0x94;
    
    std::thread graphx(SDLStuff);

    while(true)
    {
        cpu.bus[0xFF44]+=1;
        cpu.bus[0xFF44]%=154;
        cpu.execute();
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}