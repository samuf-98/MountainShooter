from code.Entity import Entity
from code.const import ENTITY_SPEED


class EnemyShot(Entity): #Classe pai Entity

    def __init__(self, name: str, position: tuple): #Metodo construtor da classe EnemyShot
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name] #centerx para o tiro ir reto