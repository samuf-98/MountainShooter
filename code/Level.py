import random
import sys

import pygame
from pygame import SurfaceType

from code.EntityFactory import EntityFactory
from code.Entity import Entity
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.Enemy import Enemy
from code.const import C_WHITE, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME, C_GREEN, EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL


class Level:
    def __init__(self, window: SurfaceType, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL  # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg')) #07.03
        player = EntityFactory.get_entity('Player1') #07.04
        player.score = player_score[0] #07.04
        self.entity_list.append(player) #07.04
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        #07.02
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP) #Cria evento para verificar o TIMEOUT a cada TIMEOUT_STEP (100ms)


    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                #04.03 - INICIO
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                #04.03 - FIM
                #06.03 - INICIO
                if ent.name == 'Player1':
                    self.level_text(text_size=14, text=f'Player1 - Health: {ent.health} | Score: {ent.score}', text_color=C_GREEN, text_pos=(10, 25))
                #06.03 - FIM

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

                #07.01 - INICIO
                if event.type == EVENT_TIMEOUT: #Se o evento 'EVENT_TIMEOUT' acontecer (acontece a cada 100ms), faça...
                    self.timeout -= TIMEOUT_STEP #Decremente o 'TIMEOUT_STEP' (100ms) da variavel 'timeout'
                    if self.timeout == 0: #Se o timeout for igual a 0, faça...
                        #07.04 - INICIO
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                        #07.04 - FIM
                        return True #Retorne verdadeiro
                #07.01 - FIM

                #07.04 - INICIO
                found_player = False
                for ent in self.entity_list: #Passe por todos os itens da lista 'entity_list'
                    if isinstance(ent, Player): #Se ent for igual a 'Player', faça...
                        found_player = True #Variavel recebe True

                if not found_player: #Se a variavel 'found_player' nao for encontrada, faça...
                    return False #Retorne Falso
                #07.04 - FIM

            #printed text
            self.level_text(text_size = 14, text = f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', text_color = C_WHITE, text_pos = (10, 5))
            self.level_text(text_size=14, text= f'fps: {clock.get_fps() :.0f}', text_color = C_WHITE, text_pos=(10, WIN_HEIGHT - 35))
            self.level_text(text_size=14, text=f'entidades: {len(self.entity_list)}', text_color = C_WHITE, text_pos=(10, WIN_HEIGHT - 20))

            pygame.display.flip()

            #Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list) #Chamar o metodo de verificar colisao do Mediator
            EntityMediator.verify_health(entity_list=self.entity_list) #Chamar o metodo de verificar vida do Mediator


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)






