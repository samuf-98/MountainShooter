import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, K_RETURN, K_BACKSLASH, K_BACKSPACE, KEYDOWN, K_ESCAPE
from pygame.font import Font

from code.DBProxy import DBProxy
from code.const import C_YELLOW, SCORE_POS, MENU_OPTION, C_WHITE


class Score:

    #08.01.01
    def __init__(self, window): #metodo construtor da classe Score
        self.window = window #variavel da janela do jogo
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha() #variavel que recebe a imagem do background
        self.rect = self.surf.get_rect(left=0, top=0) #get_rect cria uma caixa de colisao invisivel do tamanho da imagem carregada acima, left=0 e right=0 diz para pegar essa caixa e grudar no canto supeior esquerdo



    #08.01.04
    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        #08.02.05
        db_proxy = DBProxy('DBScore') #Variavel que receberá a classe DBScore
        name = ''

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            #08.01.06 - INICIO
            self.score_text(48, 'YOU WIN!!', C_YELLOW, SCORE_POS['Title'])
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
                text = 'Enter Player 1 name (4 caracters)'
            #08.01.06 - FIM
            self.score_text(20, text, C_WHITE, SCORE_POS['EnterName'])


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    sys.exit()  # end pygame

                #08.02.07 - INICIO
                elif event.type == KEYDOWN: #Se o tipo de evento for uma tecla pressionada, faça...
                    if event.key == K_RETURN and len(name) == 4: #se a tecla pressiona for K_RETURN e variavel nome igual a 4, faça...
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()}) #Chama o metodo save que salva os dados no banco de dados, passando os parametros de nome, score e data
                        self.show()
                    elif event.key == K_BACKSPACE: #Se a evento de tecla for K_BACKSPACE (deletar), faça...
                        name = name[:-1] #Apague a ultima letra no name
                    else:
                        if len(name) < 4: #se o tamanho de nome for menor que 4, faça...
                            name += event.unicode #Adicione a tecla pressionada a name
            self.score_text(20, name, C_WHITE, SCORE_POS['Name']) #Faz o print na tela

            #08.02.07 - FIM
            pygame.display.flip() #atualiza a tela
            pass

    #08.01.02
    def show(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(self.surf, self.rect)

        #08.01.09 - INICIO
        self.score_text(48, 'TOP 10 SCORE', C_YELLOW, SCORE_POS['Title'])
        self.score_text(20, 'NAME     SCORE          DATE      ', C_YELLOW, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10() #Salva os dados vindos do metodo retrieve_top10 na variavel list_score
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f' {name}     {score :05d}   {date}', C_YELLOW, SCORE_POS[list_score.index(player_score)])

        #08.01.09 - FIM

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()



    #08.01.05
    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)

#08.02.08
def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%Y")
    return f'{current_time} - {current_date}'


