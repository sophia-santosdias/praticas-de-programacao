# EXERCÍCIO: Movimentar um elemento do cenário com o teclado.
# ALUNAS: Sophia Santos e Lorena Luvizotto

import pygame
width = 800 #Largura Janela
height = 600 #Altura Janela

def load():
    global clock, dx, fator
    dx = 0
    clock = pygame.time.Clock()
    fator = 1

def draw_screen(screen):
    #céu
    pygame.draw.rect(screen, (173*fator, 216*fator, 230*fator), (0, 0, 800, 600))
    #grama
    pygame.draw.rect(screen, (0*fator, 150*fator, 0*fator), (0, 500, 800, 600))
    #casa
    pygame.draw.rect(screen, (232*fator, 195*fator, 79*fator), (100, 350, 300, 150))
    pygame.draw.polygon(screen,(255*fator, 77*fator, 63*fator), [(70, 350), (100, 250),
(400, 250), (430, 350)])
    #chamine
    pygame.draw.rect(screen, (232*fator, 195*fator, 79*fator), (130, 220, 50, 30))
    pygame.draw.rect(screen, (232*fator, 161*fator, 44*fator), (120, 220, 70, 10))
    #sacada
    pygame.draw.rect(screen, (232*fator, 195*fator, 79*fator), (230, 220, 120, 80))
    pygame.draw.polygon(screen,(232*fator, 195*fator, 79*fator), [(230, 220), (290, 160),
(350, 220)])
    pygame.draw.lines(screen, (255*fator, 77*fator, 63*fator), False, [(230, 220),(290,
160) ,(350, 220)], 12)
    pygame.draw.lines(screen, (232*fator, 161*fator, 44*fator), False, [(230, 220),(230,
300) ,(350, 300), (350, 220)])
    pygame.draw.line(screen, (232*fator, 161*fator, 44*fator), (230, 270), (350, 270), 3)
    pygame.draw.line(screen, (232*fator, 161*fator, 44*fator), (260, 270), (260, 300), 3)
    pygame.draw.line(screen, (232*fator, 161*fator, 44*fator), (290, 270), (290, 300), 3)
    pygame.draw.line(screen, (232*fator, 161*fator, 44*fator), (320, 270), (320, 300), 3)
    pygame.draw.line(screen, (232*fator, 161*fator, 44*fator), (350, 270), (350, 300))
    pygame.draw.rect(screen, (235*fator, 230*fator, 223*fator), (250, 220, 80, 30))
    pygame.draw.line(screen, (255*fator,255*fator,255*fator), (250, 235), (330, 235), 3)
    pygame.draw.line(screen, (255*fator,255*fator,255*fator), (290, 220), (290, 248), 3)
    #entrada e janela
    pygame.draw.rect(screen, (232*fator, 161*fator, 44*fator), (300, 400, 70, 100))
    pygame.draw.circle(screen, (0, 0, 0), (360, 460), 5)
    pygame.draw.rect(screen, (245*fator, 20*fator, 30*fator), (290, 490, 90, 10))
    pygame.draw.rect(screen, (235*fator, 230*fator, 223*fator), (130, 370, 50, 50))
    pygame.draw.line(screen, (255*fator,255*fator,255*fator), (155, 370), (155, 420), 3)
    pygame.draw.line(screen, (255*fator,255*fator,255*fator), (130, 395), (180, 395), 3)
    pygame.draw.rect(screen, (235*fator, 230*fator, 223*fator), (210, 390, 50, 50))
    pygame.draw.line(screen, (255*fator,255*fator,255*fator), (235, 390), (235, 440), 3)
    pygame.draw.line(screen, (255*fator,255*fator,255*fator), (210, 415), (260, 415), 3)
    #árvore
    pygame.draw.rect(screen, (102*fator, 69*fator, 7*fator), (550, 370, 40, 130))
    pygame.draw.rect(screen, (102*fator, 69*fator, 7*fator), (670, 420, 40, 80))
    pygame.draw.circle(screen, (123*fator, 232*fator, 39*fator), (570, 350), 50)
    pygame.draw.circle(screen, (123*fator, 232*fator, 39*fator), (690, 400), 50)
    #sol
    pygame.draw.circle(screen, (255, 255, 0), (100+dx, 100), 40)
    pygame.draw.line(screen, (255,255,0), (40+dx, 100), (160+dx, 100), 6)
    pygame.draw.line(screen, (255,255,0), (100+dx, 40), (100+dx, 160), 6)
    pygame.draw.line(screen, (255,255,0), (50+dx, 50), (150+dx, 150), 6)
    pygame.draw.line(screen, (255,255,0), (50+dx, 150), (150+dx, 50), 6)
    #nuvem
    pygame.draw.circle(screen, (255*fator, 255*fator, 255*fator), (400, 100), 50)
    pygame.draw.circle(screen, (255*fator, 255*fator, 255*fator), (450, 100), 50)
    pygame.draw.circle(screen, (255*fator, 255*fator, 255*fator), (500, 100), 50)
    


def update(dt):
    global dx
    global fator
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:    
        dx += 0.1*dt
    if keys[pygame.K_LEFT]:
        dx -= 0.1*dt
    
    if 40 + dx >= 800:
        dx = -300
    if 40 + dx <= -300:
        dx = 750

    if dx >= 230 and dx <= 430:
        fator = 0.9
    elif dx > 750 or dx < -70:
        fator = 0.5
    else:
        fator = 1
    
    
def main_loop(screen):
    global clock
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                break
        # Define FPS máximo
        clock.tick(60)        
 
        # Calcula tempo transcorrido desde
        # a última atualização 
        dt = clock.get_time()

        #cenário       
        draw_screen(screen)

        update(dt)
    
        pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()
