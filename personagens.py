import random

# BIBLIOTECA DOS PERSONAGENS
class Personagem():
    
    def __init__(self, NOME, PDV, ATK, DEF, VEL):

        self.nome = NOME
        self.vida = PDV
        self.ataque = ATK 
        self.defesa = DEF
        self.velocidade = VEL
        self.modificador = [0, 0, 0] # MODIFICADORES DOS ATRIBUTOS ATK, DEF E VEL DOS PERSONAGENS

        self.defendendo = False

    def atacar(self, target):
        dano = round((self.ataque + self.modificador[0]) * (50 / (50 + target.defesa + target.modificador[1])))
        return dano

    def defender(self): # FUNÇÃO PARA DEIXAR O PERSONAGEM SE DEFENDENDO
        self.modificador[1] += self.defesa * 0.1
        self.defendendo = True

    def parar_defender(self): # FAZ O PERSONAGEM PARAR DE SE DEFENDER
        if self.defendendo:
            self.modificador[1] -= self.defesa * 0.1
            self.defendendo = False

    def mudar_pv(self, dano): # MUDANÇA NA VIDA DOS PERSONAGENS
        self.vida -= dano


class Guerreiro(Personagem):

    def __init__(self):
        super().__init__(NOME='AMIGO', PDV=10 , ATK=5, DEF=3, VEL=1)
        self.charging = False # BOOLEAN DE CARREGAMENTO DO Guerreiro
        self.lastVida = 0


    def ataque_carregado(self, target): # ATAQUE CARREGADO: ADICIONA AO ATK METADE DO DANO SOFRIDO ATÉ DESCARREGAR
        if not self.charging:
            self.charging = True
            self.lastVida = self.vida
            print('CARREGANDO ATAQUE')
            return None

        if self.charging:
            self.modificador[0] = self.lastVida - self.vida
            self.charging = False
            dano = self.atacar(target)
            print(dano)
            target.mudar_pv(dano)

# class Curandeiro(Personagem):
# 
#     def __init__(self):
#         super().__init__(PDV=5, ATK=1, DEF)

class Inimigo(Personagem):

    def __init__(self):
        super().__init__(NOME='ELEMIGO', PDV=6, ATK= 2, DEF=2, VEL=3)

    def flutuacao(self): # FLUTUAÇÃO: A CADA RODADA OS INIMIGOS GANHAM MODIFICADORES NOVOS NOS STATS DELES
        regulador = 0
        for i in range(len(self.modificador)):
            mod = random.randint(0, 3)
            self.modificador[i] = regulador + mod
            regulador = mod * -1 

def ataque(atacante, defensor):
    print(f'{atacante.nome} VAI ATACAR {defensor.nome}')
    damage = atacante.atacar(defensor)
    defensor.mudar_pv(damage)
    print(f'E CAUSOU {damage} DE DANO')
    print(f'DEIXANDO {defensor.nome} COM {defensor.vida} DE VIDA')

def simuCHARGE(amg, ele):
    amg.ataque_carregado(ele)
    ataque(ele, amg)
    amg.ataque_carregado(ele)


amigo = Guerreiro()
elemigo = Inimigo()
print(f'A VIDA DO AMIGO É:{amigo.vida}')
print(f'A VIDA DO ELEMIGO É:{elemigo.vida}')

#simuCHARGE(amigo, elemigo)
simuCHARGE(amigo, elemigo)

print(f'A VIDA DO ELEMIGO É DE {elemigo.vida}')
