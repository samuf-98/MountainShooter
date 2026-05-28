from entity import Entity
from player import Player
from enemy import Enemy
from background import Background

class EntityFactory:
    def get_entity(self, entity_type: str, surf: 'Surface' = None, rect: 'Rect' = None) -> Entity:
        if entity_type == "Player":
            return Player(name="Player", surf=surf, rect=rect)
        elif entity_type == "Enemy":
            return Enemy(name="Enemy", surf=surf, rect=rect)
        elif entity_type == "Background":
            return Background(name="Background", surf=surf, rect=rect)
        else:
            raise ValueError(f"Tipo de entidade não suportado: {entity_type}")