import random
import math

# BIBLIOTECA DOS PERSONAGENS
class Personagem():
    
    def __init__(self, nome, ATK, DEF, VEL):

    # ATRIBUTOS BÁSICOS DOS PERSONAGENS

        self.nome = nome
        self.vida = 30 + (DEF - 1) * 5
        self.baseAtaque = ATK
        self.baseDefesa = DEF  
        self.baseVelocidade = VEL
        
        self.vulneravel = True # VULNERÁVEL: CONDIÇÃO DAQUELE QUE PODE PERDER VIDA
        self.quebrado = False # QUEBRADO: CONDIÇÃO QUE FAZ O PERSONAGEM TOMAR O DOBRO DE DANO E NÃO CONSEGUIR ATACAR. SÓ É TRATÁVEL COM CURA. 

        self.modificador = [0, 0, 0] # MODIFICADORES DOS ATRIBUTOS BASE

    # AS PROPRIEDADES SERVEM PARA RESUMIR OS VALORES BASE COM OS MODIFICADORES EM UM LUGAR SÓ, FACILITANDO A SUA UTILIZAÇÃO NO CÓDIGO

    def __str__(self):
        return self.nome

    @property
    def ataque(self):
        return self.baseAtaque + self.modificador[0]
    
    @property
    def defesa(self):
        return self.baseDefesa + self.modificador[1]
    
    @property
    def velocidade(self):
        return self.baseVelocidade + self.modificador[2]
    
    @property
    def danoRatio(self):
        if self.quebrado:
            return 2
        return 1
    
    # ATAQUE BÁSICO

    def atacar(self, alvo):
        if not self.vulneravel: # TODOS QUE ATACAM PERDEM INVULNERABILIDADE. PERDER INVULNERABILIDADE TE DEIXA QUEBRADO. 
            self.vulneravel = True
            self.quebrado = True
        if self.quebrado:
            return print('O PERSONAGEM ESTÁ QUEBRADO!')

        if alvo.vulneravel:
            dano = round((self.ataque) * (10 / (10 + alvo.defesa)) * alvo.danoRatio)  # DANO BASE DECIDIDO VEZES UMA RAZÃO 
            print(f'{self.nome} ATACOU {alvo.nome}, CAUSANDO {dano} DE DANO!')
            alvo.mudar_pv(dano)
        else:   # ALVOS INVULNERÁVEIS NÃO PODEM SER ATACADOS E FAZEM O ATACANTE PERDER SEU ATAQUE (na vdd o atacante não poderia atacá-lo, mas ok)
            print('O ALVO ESTÁ INVULNERÁVEL!')

        self.modClear()

    # DEFESA BÁSICA

    def defender(self):
        self.modClear()
        self.mod[1] += self.baseDefesa

    # ALTERADOR DA VIDA DOS PERSONAGENS

    def mudar_pv(self, dano):
        self.vida -= dano

    # LIMPADOR DOS MODIFICADORES

    def modClear(self):
        self.modificador = [0, 0, 0]

    # FUNÇÃO USADA PARA FACILIDADE A VISUALIZAÇÃO DE ATRIBUTOS. MOSTRA OS ATRIBUTOS BASE MAIS SEUS MODIFICADORES

    def mostrarStats(self):
        print(f'''{self.nome} 
        PV: {self.vida} 
        ATK: {self.baseAtaque} + {self.modificador[0]}
        DEF: {self.baseDefesa} + {self.modificador[1]} 
        VEL: {self.baseVelocidade} + {self.modificador[2]}''')

class Guerreiro(Personagem):

    def __init__(self, nome):
        super().__init__(nome, ATK=5, DEF=3, VEL=1)

    def pancada(self, alvo): # PANCADA: ATAQUE DESCONSIDERA DEFESA, CAUSANDO 3x SEU ATAQUE, MAS DEIXA QUEBRADO
        if not self.quebrado:
            dano = round(self.ataque * 3)
            alvo.mudar_pv(dano) 
            print(f'{self.nome} ATACOU {alvo.nome}, CAUSANDO {dano} DE DANO!')
            self.quebrado = True
        else:
            print('O PERSONAGEM ESTÁ QUEBRADO!')

class Assassino(Personagem):

    def __init__(self, nome):
        super().__init__(nome, ATK=5, DEF=1, VEL=3)
        self.espreita = False

    def espreitar(self): # ESPREITAR: FICA INVULNERÁVEL E GANHA 2 DE ATAQUE A CADA RODADA INVULNERÁVEL, MAS DEIXA QUEBRADO
        if not self.quebrado:
            if self.vulneravel:
                self.vulneravel = False
            else:
                self.modificador[0] += 2
        else:
            print('O PERSONAGEM ESTÁ QUEBRADO!')

class Tanque(Personagem):

    def __init__(self, nome):
        super().__init__(nome, ATK=3, DEF=5, VEL=1)

    def sentinela(self, target): # SENTINELA: AUMENTA A PRÓPRIA DEFESA E A DE UM ALIADO
        self.modificador[1] += self.defesa + 3
        target.modificador[1] += target.defesa + 3
 
class Curandeiro(Personagem):

    def __init__(self, nome):
        super().__init__(nome, ATK=1, DEF=5, VEL=3)

    def cura(self, target): # CURA: REGENERA VIDA E LIMPA A CONDIÇÃO "QUEBRADO"
        cura = (3 + target.defesa) * -1
        if cura > -3:
            cura = -3
        target.mudar_pv(cura)
        if target.quebrado:
            target.quebrado = False

class Mago(Personagem):

    def __init__(self, nome):
        super().__init__(nome, ATK=3, DEF=1, VEL=5)

    def fogo(self, inimigos): # FOGO: CAUSA DANO A TODOS OS INIMIGOS, MAS TOMA DANO DO PRÓPRIO ATAQUE
        for inimigo in inimigos:
            dano = (self.ataque) * ((self.velocidade) + 1 - (inimigo.velocidade))
            if dano > 0:
                inimigo.mudar_pv(dano)
                print(f'{inimigo.nome} TOMOU {dano} DE DANO!')
            else:
                print(f'{inimigo.nome} NÃO TOMOU DANO!')

        self.mudar_pv(self.ataque + self.velocidade)
        print(f'{self.nome} SE QUEIMOU COM SUA MAGIA, TOMANDO {self.ataque + self.velocidade} DE DANO!')

class Bardo(Personagem):

    def __init__(self, nome):
        super().__init__(nome, ATK=1, DEF=3, VEL=5)

    def inspirar(self, target): # INSPIRAR: ADICIONA 5 DE MOD EM UM STAT ALEATÓRIO DE UM ALIADO
        stat = random.randint(0,2)
        target.modificador[stat] += 5
        stats = ['ATAQUE', 'DEFESA', 'VELOCIDADE']
        print(f'{target.nome} GANHOU +5 EM {stats[stat]}')    

class Inimigo(Personagem):

    def __init__(self, nome):
        super().__init__(nome, ATK= 2, DEF=2, VEL=3)
        self.insanidadeModificador = [0, 0, 0]

    def insanidade(self): # INSANIDADE: A CADA RODADA OS INIMIGOS GANHAM MODIFICADORES NOVOS NOS STATS DELES
        regulador = 6
        for mod in range(3):
            self.modificador[mod] -= self.insanidadeModificador[mod]

            i = random.randint(1, 3)
            if regulador < i:
                i = regulador
            self.insanidadeModificador[mod] += i
            regulador -= i

            self.modificador[mod] += self.insanidadeModificador[mod]
        
def criar_aliado():
    print('DE QUAL CLASSE SEU PERSONAGEM SERÁ?')
    print('''          [1] GUERREIRO
          [2] ASSASSINO
          [3] TANQUE
          [4] CURANDEIRO
          [5] MAGO
          [6] BARDO''')
    
    classes = [Guerreiro, Assassino, Tanque, Curandeiro, Mago, Bardo]
    
    while True:
        escolha = int(input("ESCOLHA UMA CLASSE: ")) - 1
        if 0 <= escolha <= 5:
            classe = classes[escolha]
            break
        else:
            print("ESCOLHA INVÁLIDA. TENTE NOVAMENTE. ")
    
    nome = input("ESCOLHA O NOME DO PERSONAGEM: ")

    return classe(nome)

def criar_aliados():

    Aliados = []

    for i in range(3):
        print('CRIE O ALIADO ' + str(i + 1))
        Aliados.append(criar_aliado())
        Aliados[i].mostrarStats()
        input('APERTE QUALQUER BOTÃO...')

    return Aliados

def criar_inimigos():

    Inimigos = []

    for i in range(3):
        Nome = 'Inimigo ' + str(i + 1)
        Inimigos.append(Inimigo(Nome))

    return Inimigos

def ordemBatalha(personagens):
    personagens.sort(key= lambda p: p.velocidade)
    print(personagens)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CLASSES ^ ~~~~ CÓDIGO v ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def simular():
    #Aliados = criar_aliados()
    #Inimigos = criar_inimigos()
#
    #Personagens = Aliados + Inimigos
    #
    #for i in Personagens:
    #    i.mostrarStats()
    #ordemBatalha(Personagens)

    amigo = Guerreiro('amigo')
    desamigo = Assassino('desamigo')
    amigona = Curandeiro('amigona')

    Personagens = [amigo, desamigo]

    desamigo.mostrarStats()
    amigo.pancada(desamigo)
    desamigo.mostrarStats()

    amigona.cura(amigo)

    while True:

        amigo.mostrarStats()
        desamigo.atacar(amigo)
        amigo.mostrarStats()


        if amigo.vida <= 0:
            print('Desamigo Venceu!')
            break

        desamigo.mostrarStats()
        amigo.atacar(desamigo)
        desamigo.mostrarStats()
    
        if desamigo.vida <= 0:
            print("Amigo Venceu!")
            break
        

    return None

simular()
