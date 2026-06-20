import pygame

from code.Level import Level
from code.Menu import Menu
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:

            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]: #Se 'menu_return' for igual a opcao 1, opcao 2 ou opcao 3, faca...
                #07.04
                player_score = [0]
                level = Level(self.window, 'Level1', menu_return, player_score) #Cria a variavel 'level' que recebe a entidade 'Level' com os parametros self.window, level e menu_return
                level_return = level.run(player_score) #Cria uma variavel 'level_return' que recebe o metodo 'level_run' que vai fazer o jogo rodar, assim que acabar a fase 1 entrega um resultado para essa variavel
                #07.01 - Criar Fase 2 - INICIO
                if level_return: #Se o 'level_return' recebeu o resultado de que a Fase 1 acabou, faça...
                    level = Level(self.window, 'Level2', level_return, player_score) #A variavel 'level' recebe a fase 2
                    level_return = level.run(player_score) #A variavel 'level_return' recebe o metodo 'level.run' e inicia a fase 2
                #07.02 - Criar Fase 2 - FIM
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass



