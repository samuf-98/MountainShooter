from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot
from code.const import WIN_WIDTH


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity): #Metodo para verificar se os inimigos estão dentro janela do jogo
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0

        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0

        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0


    #05.02 - INICIO
    @staticmethod
    def verify_collision_entity(ent1, ent2):  #Metodo para verifiar a colisao entre as entidades, que vai receber os parametros ent1 e ent2
        valid_colision = False #variavel para confimar a colisao
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot): #Comparacao entre o Enemy e o PlayerShot
            valid_colision = True #Confirma a colisao
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_colision = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_colision = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_colision = True

        if valid_colision:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name
    #05.02 - FIM

    #06.03 - INICIO
    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]): #Metodo para pontuar no score, que receberá como parametros o Enemy e uma lista (Entity)
        if enemy.last_dmg == 'Player1Shot': #Verifica quem deu o ultimo damage na entidade foi o player 1
            for ent in entity_list: #busca as entidades na lista 'entity_list'
                if ent.name == 'Player1': #verifica se a entidade atual é o 'Player1'
                    ent.score += enemy.score #quando for o 'Player1' soma o enemy.score a ent.score
    #06.03 - FIM


    #05.01 - INICIO
    @staticmethod
    def verify_collision(entity_list: list[Entity]): #Metodo para verificar colisoes
        for i in range(len(entity_list)): #Para i (item) no range (tamanho(lista entity_list))
            entity1 = entity_list[i] #cria a variavel entity que vai receber o item (i) da lista (entity_list)
            EntityMediator.__verify_collision_window(entity1) #chama o metodo verify_collision_window e passa o parametro (entity1) que foi criada acima,
            # que vai verificar se a entidade (inimigos, tiros) estão dentro da janela do jogo
            for j in range (i + 1, len(entity_list)): #Usado i + 1 para nao comparar as entidade que sao iguais, isso diz para iniciar o item j com item seguinte do item atual i.
                entity2 = entity_list[j] #Faz a comparacao do item i com o item j
                EntityMediator.verify_collision_entity(entity1, entity2)
    #05.01 - FIM


    @staticmethod
    def verify_health(entity_list: list[Entity]): #Metodo para verificar a vida das entidades
        for ent in entity_list:
            if ent.health <= 0:
                #06.03 - INICIO
                if isinstance(ent, Enemy): #se a entidade for do tipo Enemy, faça...
                    EntityMediator.__give_score(ent, entity_list) #chama o metodo 'give_score' e passe os parametros ent e entity_list
                #06.03 - FIM
                entity_list.remove(ent)
















