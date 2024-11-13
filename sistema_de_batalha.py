import personagens as pers

def criar_aliado(): # CRIADOR DE HERÓI
    print('DE QUAL CLASSE SEU PERSONAGEM SERÁ?')
    print('''          [1] GUERREIRO
          [2] ASSASSINO
          [3] TANQUE
          [4] CURANDEIRO
          [5] MAGO
          [6] BARDO''')
    
    classes = [pers.Guerreiro, pers.Assassino, pers.Tanque, pers.Curandeiro, pers.Mago, pers.Bardo]
    
    while True:
        escolha = int(input("ESCOLHA UMA CLASSE: ")) - 1
        if 0 <= escolha <= 5:
            classe = classes[escolha]
            break
        else:
            print("ESCOLHA INVÁLIDA. TENTE NOVAMENTE. ")
    
    nome = input("ESCOLHA O NOME DO PERSONAGEM: ")

    return classe(nome)

def criar_aliados(): # GERADOR DO TIME DE HERÓIS

    Aliados = []

    for i in range(3):
        print('CRIE O ALIADO ' + str(i + 1))
        Aliados.append(criar_aliado())
        Aliados[i].mostrarStats()
        input('APERTE QUALQUER BOTÃO...')

    return Aliados

def criar_inimigos(): # GERADOR DOS INIMIGOS

    Inimigos = []

    for i in range(3):
        Nome = 'Inimigo ' + str(i + 1)
        Inimigos.append(pers.Inimigo(Nome))

    return Inimigos

def ordenaVelocidade(personagens): # ORDENADOR DA ORDEM DA BATALHA
    personagens.sort(reverse = True, key= lambda p: p.velocidade)
    print([str(personagem) for personagem in personagens])

def verificaVivos(personagens): # VERIFICA QUAIS PERSONAGENS ESTÃO VIVOS
    for i in personagens[:]:
        if i.vida <= 0:
            print(f'{i.nome} MORREU')
            personagens.remove(i)

def verificar(personagens): # VERIFICAÇÃO DE VIVOS E DA SITUAÇÃO DA BATALHA. USADO PARA DEFINIR A VITÓRIA/DERROTA
    
    verificaVivos(personagens)

    AliadosVivos = 0
    InimigosVivos = 0
    Resultado = 0

    for i in personagens:
        if i.ehInimigo == False:
            AliadosVivos += 1
        else:
            InimigosVivos += 1
    
    if AliadosVivos == 0:
        Resultado = 1
    if InimigosVivos == 0:
        Resultado = 2

    if Resultado == 1 or 2:
        fimBatalha(Resultado)
        return True
    else:
        return False
        

def fimBatalha(resultado):
    if resultado == 1:
        print('INIMIGOS VENCERAM! VOCÊ FOI DERROTADO!')
    elif resultado == 2:
        print('HERÓIS VENCERAM! VOCÊ VENCEU!')
    else:
        return None
    

    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CLASSES ^ ~~~~ CÓDIGO v ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


def simular():
    Aliados = criar_aliados()
    Inimigos = criar_inimigos()

    Personagens = Aliados + Inimigos # JUNTA TODOS OS PERSONAGENS EM UMA SÓ LISTA. USADA TAMBÉM PARA SABER QUEM ESTÁ VIVO
    print([str(personagem) for personagem in Personagens])
    ordenaVelocidade(Personagens)

    while True:

        # INÍCIO DE UMA RODADA

        ordenaVelocidade(Personagens)

        for personagem in Personagens: # PARA CADA PERSONAGEM VIVO

            personagem.vida = 0
            
            # rodar escolha de ação

            if verificar(Personagens):
                break

        else: 
            continue

        break

    return None

simular()
