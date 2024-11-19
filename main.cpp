#include"sm83.hpp"
#include<assert.h>
#include"gfx.hpp"
#include<SDL2/SDL.h>
#include<thread>

SDL_Window* window;
SDL_Renderer* renderer;
sm83 cpu;

void gfxStuff()
{
    SDL_Init(SDL_INIT_EVERYTHING);
    window=SDL_CreateWindow("God Save The King!",SDL_WINDOWPOS_UNDEFINED,SDL_WINDOWPOS_UNDEFINED,160*2,144*2,0);
    renderer = SDL_CreateRenderer(window, -1, 0);
    SDL_RenderSetScale(renderer, 2, 2);

    SDL_Surface* surface = SDL_CreateRGBSurfaceWithFormat(0,8,8,32,SDL_PIXELFORMAT_RGBA32);
    SDL_Event event;

    u32 gfxTime=SDL_GetTicks();
    u32 now;
    while(true)
    {
        now=SDL_GetTicks();
        u32 gfxDelta=now-gfxTime;
        if (gfxDelta >= 1000/60.0)
        {
            gfxUpdate(renderer, cpu.bus, surface);
            gfxTime=now;
        }
        gfxEvent(&event);
    }
    SDL_FreeSurface(surface);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
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

    cpu.loadFile("drmario.gb");
    cpu.bus[0xFF44] = 0x94;
    
    std::thread gfxThread(gfxStuff);

    u32 cpuTime=SDL_GetTicks();
    u32 now;
    while(true)
    {
        now=SDL_GetTicks();

        u32 cpuDelta=now-cpuTime;
        //if(cpuDelta >= 1000/200.0) //NOT QUITE RIGHT
        //{
            cpu.bus[0xFF44]+=1;
            cpu.bus[0xFF44]%=154;
            cpu.bus[0xFF85]+=1;
            cpu.bus[0xFF85]%=154;
            cpu.execute();
            cpuTime=now;
            //getchar();
        //}
    }

    return 0;
}