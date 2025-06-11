import random


class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.vida_atual = 100
        self.vida_maxima = 100
        self.pontos_de_ataque = 10
        self.pontos_de_defesa = 10
        self.mao_de_cartas = []
        self.energia = 10
    
    def levar_dano(self):
        self.vida_atual -= self.pontos_de_ataque
    
    def usar_carta(self):
        pass
        
    
    
        



class Carta:
    def __init__(self, nome, energia, descricao):
        self.nome = nome
        self.energia_gasta = energia
        self.descricao = descricao
        
    def usar():
        pass
    
    
class CartaAumento(Carta):
    def __init__(self, nome, energia, descricao, tipo, pontos_aumentados):
        super().__init__(nome, energia, descricao)
        self.tipo = tipo
        self.pontos_aumentados = pontos_aumentados
        
        
        
    
    
    
class Partida:
    def __init__(self, player1, player2, jogador_atual):
        self.turno = 0
        self.player1 = player1
        self.player2 = player2
        self.jogador_atual = jogador_atual
        
    def iniciar(self):
        print(f"{self.jogador_atual} Inicia a partida")
        
        
        

if __name__ == "__main__":
    carta_vida = CartaAumento("Carta De Vida", 5, "Carta que aumenta em 25 a vida máxima do jogador", "Vida", 25 )
    carta_defesa = CartaAumento("Carta De Defesa", 5, "Carta que aumenta em 25 a defesa do jogador", "Defesa", 25 )
    carta_ataque = CartaAumento("Carta De Ataque", 5, "Carta que aumenta em 25 o Ataque do jogador", "Ataque", 25 )
    carta_energia = CartaAumento("Carta De Energia", 5, "Carta que aumenta em 25 a energia do jogador", "Energia", 25 )


    jogador1 = input("Digite seu nome jogador 1")
    jogador2 = input("Digite seu nome jogador 2")
    vencedor = None
    dado = random.randint(1,2)
    if dado == 1:
        vencedor = jogador1
        print("Jogador 1 Começa")
    else:
        vencedor = jogador2
        print("Jogador 2 Começa")
    player1 = Personagem(jogador1)
    player2 = Personagem(jogador2)
    partida = Partida(player1,player2,vencedor)
    partida.iniciar
    
    
    
        
        