#pragma once

#include<SDL2/SDL.h>
#include"types.h"


void gfxEvent(SDL_Event* event)
{
    if(SDL_PollEvent(event))
    {
        if(SDL_QUIT==event->type) {exit(0);}
        if(SDL_KEYDOWN==event->type)
        {
            
        }
    }
}

static SDL_Color tilePalette[4] = {
    {0xe0,0xf8,0xd0,0xff},
    {0x88,0xc0,0x70,0xff},
    {0x34,0x68,0x56,0xff},
    {0x08,0x18,0x20,0xff}
};

void gfxCreateTileSurface(const SDL_Surface* surface,const u8* tileData) //SDL_CreateRGBSurfaceWithFormat(0, 8, 8, 32, SDL_PIXELFORMAT_RGBA32);
{
    u32* pixels = (u32*)surface->pixels;
    /*for(int i=0;i<16;i+=2)
    {
        printf("%02X\n",tileData[i]);
    }*/
    for (int y = 0; y < 8; y++)
    {
        u8 loByte = tileData[y * 2];
        u8 hiByte = tileData[y * 2 + 1];
        for (int x = 0; x < 8; x++)
        {
            u8 loBit = (loByte >> (7 - x)) & 1;
            u8 hiBit = (hiByte >> (7 - x)) & 1;
            u8 colorIndex = (hiBit << 1) | loBit;
            //printf("%01d",colorIndex);
            u32 color = SDL_MapRGBA(surface->format, tilePalette[colorIndex].r, tilePalette[colorIndex].g, tilePalette[colorIndex].b, tilePalette[colorIndex].a);
            pixels[y*8+x] = color;
        }
        //printf("\n");
    }
    //printf("ENDIMG\n");
}

void gfxUpdate(SDL_Renderer *renderer, u8* bus, SDL_Surface* surface) //TAKES 5MS ON RTX, NOT VERY GOOD..
{
    SDL_SetRenderDrawColor(renderer,0,0,0,255);
    SDL_RenderClear(renderer);
    SDL_Rect rect;
    rect.w=8; rect.h=8;
    
    SDL_Texture* texture;

    for(u8 y=0;y<32;y++)
    {
        for(u8 x=0;x<32;x++)
        {
            u8 tileID=bus[0x9800+(y*32+x)];
            gfxCreateTileSurface(surface,&bus[0x9000+tileID*16]);
            texture = SDL_CreateTextureFromSurface(renderer, surface);
            if (!texture)
            {
                printf("Texture creation failed: %s\n", SDL_GetError());
                continue;
            }
            rect.x=x*8; rect.y=y*8;
            SDL_RenderCopy(renderer, texture, NULL, &rect);
            SDL_DestroyTexture(texture);
        }
    }
    SDL_RenderPresent(renderer);
}