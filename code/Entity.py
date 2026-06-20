from abc import ABC, abstractmethod

import pygame

from code.const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name] #05.02
        self.score = ENTITY_SCORE[self.name] #06.03
        self.last_dmg = 'None' #05.02

    @abstractmethod
    def move(self):
        pass