from entity_factory import EntityFactory

class Level:
    def __init__(self, window: 'Surface', name: str, entity_list: list):
        self.window = window
        self.name = name
        self.entity_list = entity_list
        # Relação de uso com a Factory
        self.factory = EntityFactory()

    def run(self) -> None:
        # Lógica de execução do nível
        pass