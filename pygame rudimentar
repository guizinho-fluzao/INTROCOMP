import pygame

pygame.init()

#"Relógio" in-code
clock = pygame.time.Clock()

class Window:
    width = 1024  #largura
    height = 768  #altura
    color = (0, 0, 0)  #cor

    def __init__(self, largura, altura):  #construtor
        self.width = largura
        self.height = altura

#abre a janela com as dimensões corretas
w = Window(1024, 768)
win = pygame.display.set_mode((w.width, w.height))
pygame.display.set_caption('JOGO INTROCOMP')

background = pygame.image.load('teste 7.jpg')  #Imagem de fundo
background = pygame.transform.scale(background, (w.width, w.height))

running = True
while running: #GAME LOOP
    #Checagem de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #Clicar no 'X' pra fechar
            running = False

    win.fill(w.color)
    win.blit(background, (0, 0)) #Desenha o fundo a cada tick

    #Atualização display e fps
    pygame.display.update()
    clock.tick(30)  #limitar 30 fps

#propriamente fecha o jogo e para o código
pygame.quit()
