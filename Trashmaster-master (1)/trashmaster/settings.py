import pygame as pg

#colors
LIGHTGREY = (100, 100, 100)
CYAN = (0, 255, 255)
RED = (255, 0, 0)


#game settings
WIDTH = 1024
HEIGHT = 768
FPS = 60

TILESIZE = 64
GRIDWIDTH = WIDTH/TILESIZE
GRIDHEIGHT = HEIGHT/TILESIZE


WALL_IMG = 'buliding\GTA2_TILE_26.bmp'

#player settings
PLAYER_SPEED = 280
PLAYER_ROT_SPEED = 200
PLAYER_IMG = 'garbagetruck/trashmaster_v2.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 50, 50)
PLAYER_WIDTH = 64
PLAYER_HEIGHT = 32

#map settings x 16 y 12
MAP_WIDTH = 25
MAP_HEIGHT = 25

TILE_SIZE_PX = 64
MAP_WIDTH_PX = MAP_WIDTH * TILE_SIZE_PX
MAP_HEIGHT_PX = MAP_HEIGHT * TILE_SIZE_PX

TRASHBIN_NUMBER = 70
WALL_NUMBER = 50