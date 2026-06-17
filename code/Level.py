import random
import sys

import pygame

from code.EntityFactory import EntityFactory
from code.Entity import Entity
from code.EntityMediator import EntityMediator
from code.const import COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000  # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)



    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            #printed text
            self.level_text(text_size = 14,text = f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s',text_color = COLOR_WHITE, text_pos = (10, 5))
            self.level_text(text_size=14, text= f'fps: {clock.get_fps() :.0f}', text_color = COLOR_WHITE, text_pos=(10, WIN_HEIGHT - 35))
            self.level_text(text_size=14, text=f'entidades: {len(self.entity_list)}', text_color = COLOR_WHITE, text_pos=(10, WIN_HEIGHT - 20))

            pygame.display.flip()

            #Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list) #Chamar o metodo de verificar colisao do Mediator
            EntityMediator.verify_health(entity_list=self.entity_list) #Chamar o metodo de verificar vida do Mediator

        pass


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)






