import pygame
width = 800 #Largura Janela
height = 600 #Altura Janela

def load():
    global clock, dx
    dx = 0
    clock = pygame.time.Clock()

def draw_screen(screen):
    #céu
    pygame.draw.rect(screen, (173, 216, 230), (0, 0, 800, 600))
    #grama
    pygame.draw.rect(screen, (0, 150, 0), (0, 500, 800, 600))
    #predio
    pygame.draw.rect(screen, (255, 49, 224), (100, 200, 250, 300))
    #sol
    pygame.draw.circle(screen, (255, 255, 0), (100+dx, 100), 40)
    pygame.draw.line(screen, (255,255,0), (40+dx, 100),
(160+dx, 100), 6)
    pygame.draw.line(screen, (255,255,0), (100+dx, 40),
(100+dx, 160), 6)
    pygame.draw.line(screen, (255,255,0), (50+dx, 50),
(150+dx, 150), 6)
    pygame.draw.line(screen, (255,255,0), (50+dx, 150),
(150+dx, 50), 6)

def update(dt):
    global dx
    dx += 0.1*dt
    if 40 + dx >= 800:
        dx = -300
    
    

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
