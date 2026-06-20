import pygame

from code.Entity import Entity
from code.PlayerShot import PlayerShot
from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY


class Player(Entity):

    def __init__(self, name: str, position: tuple): #metodo construtor
        super().__init__(name, position) #herda nome e posicao da classe pai
        self.shot_delay = ENTITY_SHOT_DELAY[self.name] #cria uma propriedade shot_delay que recebe uma constante que vai puxar o valor (20) pelo nome que está na constante


    def move(self):
        pressed_key = pygame.key.get_pressed()

        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

        pass

    def shoot(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
            PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))




        #self.shot_delay -= 1
        #if self.shot_delay == 0:
        #    self.shot_delay = ENTITY_SHOT_DELAY[self.name]
         #   pressed_key = pygame.key.get_pressed()
         #   if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
         #       return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))



