# EXERCÍCIO: Criar um jogo Pong em pygame.
# ALUNAS: Sophia Santos e Lorena Luvizotto

import pygame
import random
import math

width = 800  #Largura Janela
height = 600 #Altura Janela

def load():
    global clock, px, player, box, velocidade, angulo, vidas, font, tempo_fim, pontos, fontp
    clock = pygame.time.Clock()

    velocidade = [0.3, 0.5, 0.8]
    angulo = [135, 180, 225]
    vidas = 3 
    tempo_fim = 2000
    pontos = 0
    font = pygame.font.Font(None, 48)
    fontp = pygame.font.Font(None, 35)
    
    player = {
      "x": 700,
      "y": 250,
      "width": 30,
      "height": 150,
      "speed": 0.5,
      "collided": False
    }
    
    box = {
      "x": 100,
      "y": 75,
      "width": 30,
      "height": 30,
      "vx": 0.1,
      "vy": 0.2,
      "collided": False
    }


def check_box_collision(x1, y1, w1, h1, x2, y2, w2, h2):
   return (x1 < x2 + w2) and (x2 < x1 + w1) and (y1 < y2 + h2) and (y2 < y1 + h1)


def update(dt):
    global player, box, angulo, velocidade, vidas, tempo_fim, pontos
         
    dy_player = 0
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
       dy_player = -(player["speed"] * dt)
    if keys[pygame.K_DOWN]:
       dy_player = (player["speed"] * dt)
    #player["y"] = max(0, min(height - player["height"], player["y"]))
    
    player["y"] = player["y"] + dy_player

    box["x"] += box["vx"] * dt
    box["y"] += box["vy"] * dt
    box["collided"] = False
    player["collided"] = False

    if box["y"] <= 0:
        box["y"] = 0
        box["vy"] = abs(box["vy"])
    elif box["y"] + box["height"] >= height:
        box["y"] = height - box["height"]
        box["vy"] = -abs(box["vy"])
    
    if box["x"] <= 0:
        box["x"] = 0
        box["vx"] = abs(box["vx"])


    if check_box_collision(player["x"], player["y"], player["width"], player["height"], box["x"], box["y"], box["width"], box["height"]):
        player["collided"] = True
        box["collided"] = True
        pontos += 1
        ang = math.radians(random.choice(angulo))
        vel = random.choice(velocidade)
        box["vx"] = vel * math.cos(ang)   # sempre negativo (volta pra esquerda)
        box["vy"] = vel * math.sin(ang)
        box["x"] = player["x"] - box["width"]

    elif box["x"] > width:
        box["x"], box["y"] = 100, 75
        box["vx"], box["vy"] = 0.3, 0.2
        vidas -= 1

    if vidas <= 0:
        tempo_fim -= dt
        return

        

def draw_screen(screen):
    screen.fill((0,0,0))
    
    
    color_box = (255,255,255)
    color_vidas = (200, 0, 0)

    
    pygame.draw.rect(screen,color_box,(box["x"], box["y"], box["width"], box["height"]))
    pygame.draw.rect(screen,color_box,(player["x"], player["y"], player["width"], player["height"]))

    text_surface = fontp.render(f'Pontos: {pontos}', True, (255, 255, 255))  # True = antialias
    text_rect = text_surface.get_rect(center=(400, 550))
    screen.blit(text_surface, text_rect)
    
    dC = 0
    for v in range(1, vidas + 1):
        pygame.draw.rect(screen,color_vidas,(100 + dC, 540, 20, 20))
        dC += 50

    if vidas == 0:
        text_surface = font.render("FIM DE JOGO", True, (255, 255, 255))  # True = antialias
        text_rect = text_surface.get_rect(center=(400, 400))
        screen.blit(text_surface, text_rect)

    
def main_loop(screen):  
    global clock, vidas, tempo_fim
    running = True
    while running:
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                running = False
                break
        
        clock.tick(60) 			# Define FPS máximo
 
        # Calcula tempo transcorrido desde
        # a última atualização 
        dt = clock.get_time()
         
        draw_screen(screen)		# Desenha objetos na tela
        
        update(dt) 			# Atualiza posição dos objetos da tela

        pygame.display.update() 	# Pygame atualiza o seu estado

        if vidas <= 0 and tempo_fim <= 0:
            running = False


pygame.init()
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()
