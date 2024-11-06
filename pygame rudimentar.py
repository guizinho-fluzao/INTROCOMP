import pygame
from personagens import Guerreiro, Curandeiro, Tanque, Assasino, Mago, Bardo, Inimigo

#inicia pygame, informações de janela e fps
pygame.init()
largura_tela, altura_tela = 1024, 768
fps = 30

# Setup screen
screen = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("introbattle")
clock = pygame.time.Clock()

#plano de fundo e ajuste pro tamanho correto
fundo = pygame.image.load('imagens/teste 7.jpg').convert_alpha()
tamanho_escala = (1024, 768)
fundo = pygame.transform.scale(fundo, tamanho_escala)

def desenha_plano_fundo():
    screen.blit(fundo, (0, 0))

#renderizar os personagens (não está funcionando por algum motivo)
imagem_guerreiro = pygame.image.load('imagens/Paladino.png').convert_alpha()
tamanho_escala = (1024, 768)
imagem_guerreiro = pygame.transform.scale(imagem_guerreiro, tamanho_escala)

def desenha_guerreiro():
	screen.blit(imagem_guerreiro, (0, 0))

# Main Game Loop
running = True
while running:
    desenha_plano_fundo()

    #identifica eventos 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # velocidade de atualização
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
