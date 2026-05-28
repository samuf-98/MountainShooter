from menu import Menu
from level import Level

class Game:
    def __init__(self, window: 'Surface'):
        self.window = window
        
        # Composição: Game possui 1 Menu (+own)
        self.menu = Menu(self.window)
        
        # Composição: Game possui 1..* Levels (+owns)
        # Inicializando como uma lista vazia que receberá instâncias de Level
        self.levels = [] 

    def run(self) -> None:
        # Loop principal do jogo
        pass