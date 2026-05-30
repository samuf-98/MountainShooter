import pygame

class Game:
    def __init__(self, window):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self) -> None:

        while True:

            game = Game(self.window)
            game.run()
            pass







            #check for all events
#            for event in pygame.event.get():
#                if event.type == pygame.QUIT:
#                    pygame.quit() #close window
#                    quit() #end pygame
