import random
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

class Personagem:
    def __init__(self, nome): 
        self.nome = nome
        self.vida_atual = 100
        self.vida_maxima = 100
        self.pontos_de_ataque = 10
        self.pontos_de_defesa = 10
        self.mao_de_cartas = []
        self.energia = 10
    
    def levar_dano(self,dano):
        self.vida_atual -= dano
    
    def comprar_carta(self):
        pass
    
    def ver_cartas(self):
        for idx, carta in enumerate(self.mao_de_cartas, 1):
            print(f"┌── Carta {idx} ───────────────────────────────────┐")
            print(f"│ 📛 Nome: {carta.nome}")
            print(f"│ ⚡ Energia : {carta.energia_gasta}")
            print(f"│ 📝 Descrição : {carta.descricao}")
            print("└──────────────────────────────────────────────────────┘\n")
    
    def curar_se(self):
        pass
        
    



class Carta:
    def __init__(self, nome, energia, descricao):
        self.nome = nome
        self.energia_gasta = energia
        self.descricao = descricao
        
    def usar(self, carta, jogador):
        print("DEBUG")
            
            
        pass
    
    
class CartaAumento(Carta):
    def __init__(self, nome, energia, descricao, tipo, pontos_aumentados):
        super().__init__(nome, energia, descricao)
        self.tipo = tipo
        self.pontos_aumentados = pontos_aumentados
        
class CartaRoubo(Carta):
    def __init__(self,nome,energia,descricao):
        super().__init__(nome, energia, descricao)
    def usar():
        pass

class CartaAtordoamente(Carta):
    def __init__(self,nome,energia,descricao):
        super().__init__(nome, energia, descricao)
        
    def usar():
        pass  
    
class CartaDano(Carta):
    def __init__(self,nome,energia,descricao):
        super().__init__(nome, energia, descricao)
        
    def usar():
        pass    
    
class CartaCura(Carta):
    def __init__(self,nome,energia,descricao):
        super().__init__(nome, energia, descricao)
        
    def usar():
        pass    
    
    
    
class Partida():
    def __init__(self, player1, player2, jogador_atual):
        self.turno = 0
        self.player1 = player1
        self.player2 = player2
        self.jogador_atual = jogador_atual
                
    def listar_cartas(self):
        os.system("cls")
        print(f"\n🎮 Jogador {self.jogador_atual} inicia a partida!")
        print("🃏 Essas são suas cartas na mão:\n")

        if self.jogador_atual == 1:
            player1.ver_cartas()  
            
        if self.jogador_atual ==2:
            player2.ver_cartas() 
                
    def iniciar(self):
        limpar_tela()
        print(f"\n🎮 Jogador {self.jogador_atual} inicia a partida!")
        opcao = int(input("Escolha uma das opções\n1-Usar uma carta\n2-Atacar\n3-Pescar Uma carta\n"))
        
        match opcao:
            case 1:
                limpar_tela()
                self.listar_cartas()
                escolha = int(input("Digite o numero da carta! que você deseja usar\n"))
                limpar_tela()
                if self.jogador_atual == 1:
                    carta_escolhida = self.player1.mao_de_cartas[escolha - 1]
                    if carta_escolhida.tipo == "Utilitario":
                        player1.usar_carta(carta_escolhida)
                        

                else:
                    carta_escolhida = self.player2.mao_de_cartas[escolha - 1]
                    if carta_escolhida.tipo == "Utilitario":
                        player2.usar_carta(carta_escolhida)


    
                
            
             
if __name__ == "__main__":
    limpar_tela()
    cartas = [] 
    carta_vida = CartaAumento("Carta De Vida", 5, "Carta que aumenta em 25 a vida máxima do jogador", "Utilitario", 25 )
    carta_defesa = CartaAumento("Carta De Defesa", 5, "Carta que aumenta em 25 a defesa do jogador", "Utilitario", 25 )
    carta_ataque = CartaAumento("Carta De Ataque", 5, "Carta que aumenta em 25 o Ataque do jogador", "Utilitario", 25 )
    carta_energia = CartaAumento("Carta De Energia", 5, "Carta que aumenta em 25 a energia do jogador", "Utilitario", 25 )
    carta_roubo = CartaRoubo("Carta De Roubo", 3, "Quando jogada, ela rouba uma carta do oponente")
    carta_stun = CartaAtordoamente("Carta De Stun", 3, "Quando jogada, ela atordoa o inimigo por 2 rodadas")
    carta_dano = CartaDano("Carta que causa dano", 3, "Causa 10 de dano no adversário inimigo")
    carta_cura = CartaCura("Carta que cura vida", 3, "Cura de 10 de vida do seu Personagem")
    cartas = [carta_vida, carta_defesa, carta_ataque, carta_energia, carta_roubo, carta_stun, carta_dano, carta_cura]
    
    
    jogador1 = input("Digite seu nome jogador 1")
    limpar_tela()
    jogador2 = input("Digite seu nome jogador 2")
    limpar_tela()
    vencedor = None
    dado = random.randint(1,2)
    if dado == 1:
        vencedor = 1
        print("Jogador 1 Começa")
    else:
        vencedor = 2
        print("Jogador 2 Começa")
    player1 = Personagem(jogador1)
    player2 = Personagem(jogador2)
    partida = Partida(player1,player2,vencedor)
    cartas_aleatorias1 = random.sample(cartas,3)
    cartas_aleatorias2 = random.sample(cartas,3)
    player1.mao_de_cartas.extend(cartas_aleatorias1)
    player2.mao_de_cartas.extend(cartas_aleatorias2)
    partida.iniciar()
    

    
    
    
    
        
        