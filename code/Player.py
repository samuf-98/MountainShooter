from entity import Entity

class Player(Entity):
    def __init__(self, name: str, surf: 'Surface', rect: 'Rect'):
        super().__init__(name, surf, rect)

    def move(self) -> None:
        # Lógica de movimento do jogador
        pass