#C
import pygame

C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_GREEN = (0, 128, 0) #05.03
C_CYAN = (0, 128, 128) #05.03

#E

EVENT_ENEMY = pygame.USEREVENT + 1


ENTITY_DAMAGE = { #05.02
    'Level1Bg0' : 0,
    'Level1Bg1' : 0,
    'Level1Bg2' : 0,
    'Level1Bg3' : 0,
    'Level1Bg4' : 0,
    'Level1Bg5' : 0,
    'Level1Bg6' : 0,
    'Player1' : 1,
    'Player1Shot': 25,
    'Enemy1' : 1,
    'Enemy1Shot': 20,
    'Enemy2' : 1,
    'Enemy2Shot' : 20
}

ENTITY_SCORE = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 0,
    'Level1Bg2' : 0,
    'Level1Bg3' : 0,
    'Level1Bg4' : 0,
    'Level1Bg5' : 0,
    'Level1Bg6' : 0,
    'Player1' : 0,
    'Player1Shot' : 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0
}

ENTITY_SPEED = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 1,
    'Level1Bg2' : 2,
    'Level1Bg3' : 3,
    'Level1Bg4' : 4,
    'Level1Bg5' : 5,
    'Level1Bg6' : 6,
    'Player1' : 3,
    'Player1Shot': 5,
    'Enemy1' : 2,
    'Enemy1Shot': 5,
    'Enemy2' : 1,
    'Enemy2Shot' : 2
}

ENTITY_HEALTH = {
    'Level1Bg0' : 999,
    'Level1Bg1' : 999,
    'Level1Bg2' : 999,
    'Level1Bg3' : 999,
    'Level1Bg4' : 999,
    'Level1Bg5' : 999,
    'Level1Bg6' : 999,
    'Player1' : 300,
    'Player1Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Enemy1': 100,
    'Enemy2': 200
}

#M
MENU_OPTION = ( 'NEW GAME 1P',
                'NEW GAME 2P - COOPERATIVE',
                'NEW GAME 2P - COMPETITIVE',
                'SCORE',
                'EXIT')

#P

PLAYER_KEY_SHOOT = {
    'Player1' : pygame.K_k,
}

#S
SPAWN_TIME = 4000

#W
WIN_WIDTH = 576
WIN_HEIGHT = 324
