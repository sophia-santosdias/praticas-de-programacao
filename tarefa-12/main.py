# EXERCÍCIO: Implementar cenário com imagens em pygame.
# ALUNAS: Sophia Santos e Lorena Luvizotto

import pygame
width = 800 #Largura Janela
height = 600 #Altura Janela

def load():
    global q, cano, morro, chao, nuvem, clock, cogumelo, bloco, dx, dy, sys_font, music
    q = 0
    dx = 0
    dy = 0
    sys_font = pygame.font.Font(pygame.font.get_default_font(), 17)
    clock = pygame.time.Clock()
    cano = pygame.image.load('cano.png')
    cano = pygame.transform.scale(cano, (950, 950))
    chao = pygame.image.load('chao.png')
    chao = pygame.transform.scale(chao, (1250, 1250))
    morro = pygame.image.load('morro.png')
    morro = pygame.transform.scale(morro, (950, 950))
    nuvem = pygame.image.load('nuvem.png')
    nuvem = pygame.transform.scale(nuvem, (300, 150))
    cogumelo = pygame.image.load('cogumelo.png')
    cogumelo = pygame.transform.scale(cogumelo, (50, 50))
    bloco = pygame.image.load('bloco.png')
    bloco = pygame.transform.scale(bloco, (50, 50))
    pygame.mixer.music.load("super.mp3")

def check_click(x1,y1,w1,h1,x2,y2):
    return x1 < x2+1 and x2 < x1+w1 and y1 < y2+1 and y2 < y1+h1

def draw_screen(screen):
    screen.fill((173, 216, 230))
    px = 0
    py = 450
    pxM = 0
    while pxM < screen.get_width():
        screen.blit(morro, (pxM, 340))
        pxM = pxM + 180
    screen.blit(cano, (550, 390+dy))
    while px < screen.get_width():
        screen.blit(chao, (px, py))
        px = px+ 80
    screen.blit(nuvem, (300, 50))
    screen.blit(bloco, (100, 250))
    screen.blit(cogumelo, (50+dx, 400))
    #botoes
    pygame.draw.rect(screen, (150, 0, 0), (50, 560, 70, 30))
    t0 = sys_font.render("Iniciar", False, (255,255,255))
    screen.blit(t0, t0.get_rect(top = 565, left=58))
    pygame.draw.rect(screen, (150, 0, 0), (140, 560, 70, 30))
    t0 = sys_font.render("Parar", False, (255,255,255))
    screen.blit(t0, t0.get_rect(top = 565, left=150))
    pygame.draw.rect(screen, (150, 0, 0), (230, 560, 90, 30))
    t0 = sys_font.render("Continuar", False, (255,255,255))
    screen.blit(t0, t0.get_rect(top = 565, left=233))
    pygame.draw.rect(screen, (150, 0, 0), (340, 560, 70, 30))
    t0 = sys_font.render("Pausar", False, (255,255,255))
    screen.blit(t0, t0.get_rect(top = 565, left=345))
    pygame.draw.rect(screen, (0, 50, 150), (620, 560, 70, 30))
    t0 = sys_font.render("Girar", False, (255,255,255))
    screen.blit(t0, t0.get_rect(top = 565, left=635))
    
      
def update(dt):
    global dx, dy
    dx += 0.1*dt
    if 40 + dx >= 800:
        dx = -300
    if dx > 400:
        dy += 0.1*dt
        if 530 < dx:
            if dy > 0:
                dy -= 0.2*dt
                
def mouse_click_down(px_mouse, py_mouse, mouse_buttons):
    global cogumelo, bloco, nuvem, q
    if mouse_buttons[0]: # left
        if check_click(620, 560, 70, 30, px_mouse, py_mouse):
            cogumelo = pygame.transform.flip(cogumelo, False, True)
        if check_click(50,560,70,30, px_mouse, py_mouse):
            bloco = pygame.transform.scale(bloco, (70, 70))
            pygame.mixer.music.play()
        if check_click(140, 560, 70, 30, px_mouse, py_mouse):
            bloco = pygame.transform.scale(bloco, (50, 50))
            pygame.mixer.music.stop()
        if check_click(340, 560, 70, 30, px_mouse, py_mouse):
            pygame.mixer.music.pause()
        if check_click(230, 560, 70, 30, px_mouse, py_mouse):
            pygame.mixer.music.unpause()
        if check_click(300,50,300,150, px_mouse, py_mouse):
            if q == 1:
                nuvem = pygame.transform.scale(nuvem, (300, 150))
                q = 0
            else:
                q = 1
                nuvem = pygame.transform.scale(nuvem, (150, 75))
            



def mouse_click_up(px_mouse, py_mouse, mouse_buttons):
    pass

def main_loop(screen):
    global clock
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                break
            elif e.type == pygame.MOUSEBUTTONDOWN: #detecta o inicio do clique do mouse
                mouse_buttons = pygame.mouse.get_pressed()
                px_mouse, py_mouse = pygame.mouse.get_pos()
                mouse_click_down(px_mouse, py_mouse, mouse_buttons)
            elif e.type == pygame.MOUSEBUTTONUP: #detecta o fim do clique do mouse
                mouse_buttons = pygame.mouse.get_pressed()
                px_mouse, py_mouse = pygame.mouse.get_pos()
                mouse_click_up(px_mouse, py_mouse, mouse_buttons)
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
