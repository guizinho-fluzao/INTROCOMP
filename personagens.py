import random

# BIBLIOTECA DOS PERSONAGENS
class Personagem():
    
    def __init__(self, NOME, PDV, ATK, DEF, VEL):

        self.nome = NOME
        self.vida = PDV
        self.atk = ATK
        self.dfs = DEF  
        self.vel = VEL
        self.mod = [0, 0, 0] # MODIFICADORES DOS ATRIBUTOS ATK, DEF E VEL DOS PERSONAGENS

    @property
    def ataque(self):
        return self.atk + self.mod[0]
    
    @property
    def defesa(self):
        return self.dfs + self.mod[1]
    
    @property
    def velocidade(self):
        return self.vel + self.mod[2]
    
    def atacar(self, target):
        dano = round((self.ataque) * (50 / (50 + self.defesa)))
        target.mudar_pv(dano)
        self.mod_clear

    def defender(self): # FUNÇÃO PARA DEIXAR O PERSONAGEM SE DEFENDENDO
        self.mod_clear
        self.mod[1] += self.dfs

    def mudar_pv(self, dano): # MUDANÇA NA VIDA DOS PERSONAGENS
        self.vida -= dano

    def mod_clear(self):
     self.mod = [0, 0, 0]

    def mostrarStats(self):
        print(f'{self.nome}: PV: {self.vida} ATK: {self.ataque} DEF: {self.defesa} VEL: {self.velocidade}')


class Guerreiro(Personagem):

    def __init__(self):
        super().__init__(NOME='GUERREIRO', PDV=10 , ATK=5, DEF=3, VEL=1)
        self.charging = False # BOOLEAN DE CARREGAMENTO DO Guerreiro
        self.lastVida = 0


    def ataque_carregado(self, target): # ATAQUE CARREGADO: ADICIONA AO ATK METADE DO DANO SOFRIDO ATÉ DESCARREGAR
        if not self.charging:
            self.charging = True
            self.lastVida = self.vida
            print('CARREGANDO ATAQUE')
            return None

        if self.charging:
            self.mod[0] = self.lastVida - self.vida
            self.charging = False
            dano = self.atacar(target)

class Assasino(Personagem):

    def __init__(self):
        super().__init__(NOME='ASSASSINO', PDV=10 , ATK=5, DEF=1, VEL=3)

class Tanque(Personagem):

    def __init__(self):
        super().__init__(NOME='TANQUE', PDV=10 , ATK=3, DEF=5, VEL=1)

class Curandeiro(Personagem):

    def __init__(self):
        super().__init__(NOME='CURANDEIRO', PDV=10 , ATK=1, DEF=5, VEL=3)

    def cura(self, target):
        cura = (3 + target.defesa) * -1
        if cura > -3:
            cura = -3
        target.mudar_pv(cura) 

class Mago(Personagem):

    def __init__(self):
        super().__init__(NOME='MAGO', PDV=10 , ATK=3, DEF=1, VEL=5)

    def incendio(self, inimigos):
        for inimigo in inimigos:
            dano = (self.ataque) * ((self.velocidade) + 1 - (inimigo.velocidade))
            if dano > 0:
                inimigo.mudar_pv(dano)
                print(f'{inimigo.nome} tomou {dano} de dano!')
            else:
                print(f'{inimigo.nome} não tomou dano!')

        self.mudar_pv(self.ataque + self.velocidade)
        print(f'{self.nome} se queimou com sua magia, tomando {self.ataque + self.velocidade} de dano!!')

class Bardo(Personagem):

    def __init__(self):
        super().__init__(NOME='BARDO', PDV=10 , ATK=1, DEF=3, VEL=5)

    def inspiration(self, target): # INSPIRAÇÃO: ADICIONA 5 DE MOD EM UM STAT ALEATÓRIO EM UM ALIADO
        #stat = random.randint(0,2)
        stat = 2
        target.mod[stat] += 5
        stats = ['ATAQUE', 'DEFESA', 'VELOCIDADE']
        print(f'{target.nome} GANHOU +5 EM {stats[stat]}')    

class Inimigo(Personagem):

    def __init__(self):
        super().__init__(NOME='INIMIGO', PDV=6, ATK= 2, DEF=2, VEL=3)

    def insanidade(self): # INSANIDADE: A CADA RODADA OS INIMIGOS GANHAM MODIFICADORES NOVOS NOS STATS DELE+S
        regulador = 6
        for i in range(len(self.mod)):
            modificador = random.randint(0, 3)
            if regulador < modificador:
                modificador = regulador
            self.mod[i] += modificador
            regulador -= modificador

bardo = Bardo()
guerreiro = Guerreiro()
mago = Mago()
curandeiro = Curandeiro()

ruim1 = Inimigo()
ruim2 = Inimigo()
ruim3 = Inimigo()

Inimigos = [ruim1, ruim2, ruim3]


def simular():
    guerreiro.mostrarStats()
    guerreiro.ataque_carregado(ruim1)
    for inimigo in Inimigos:
        inimigo.insanidade()
        inimigo.mostrarStats()
        inimigo.atacar(guerreiro)
    guerreiro.mostrarStats()
    guerreiro.ataque_carregado(ruim1)
    ruim1.mostrarStats()




simular()
