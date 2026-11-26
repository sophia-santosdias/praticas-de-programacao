# EXERCÍCIO: Criar um jogo completo em pygame.
# ALUNAS: Sophia Santos e Lorena Luvizotto

import math
import random
import pygame

scale = 2
tile_size = 16 * scale
width = tile_size * 34
height = tile_size * 18
mapa = []

# Letras do mapa
#   #  moldura de pedra
#   .  vazio (só o fundo)
#   ^  espinho (mata o personagem)
#   S  espinho escondido (aparece quando o personagem chega perto)
#   M  maçã
#   B  onde a corrente da bola fica presa
#   O  ponto mais alto da serra (ela desce e sobe a partir daqui)
#   P  onde o personagem nasce
#   q w e   topo esquerdo, topo, topo direito (com grama)
#   a s d   meio esquerdo, meio, meio direito
#   z x c   base esquerda, base, base direita
#   r t     terra de cima do tufo (esquerda, direita)
#   f g     tufo de grama (esquerda, direita)
#
# Terra rosa (areia com pingos rosa), mesmo desenho do bloco de grama:
#   1 2 3   topo esquerdo, topo, topo direito
#   4 5 6   meio esquerdo, meio, meio direito
#   7 8 9   base esquerda, base, base direita
#   u i     terra de cima do tufo (esquerda, direita)
#   j k     tufo rosa (esquerda, direita)

tiles_grama = {
    "q": (6, 0), "w": (7, 0), "e": (8, 0),
    "a": (6, 1), "s": (7, 1), "d": (8, 1),
    "z": (6, 2), "x": (7, 2), "c": (8, 2),
    "r": (9, 0), "t": (10, 0),
    "f": (9, 1), "g": (10, 1),
    "1": (6, 8), "2": (7, 8), "3": (8, 8),
    "4": (6, 9), "5": (7, 9), "6": (8, 9),
    "7": (6, 10), "8": (7, 10), "9": (8, 10),
    "u": (9, 8), "i": (10, 8),
    "j": (9, 9), "k": (10, 9),
}

# Tamanho da caixa de colisão do personagem
hit_x = 14
hit_y = 8
hit_w = 36
hit_h = 56

gravidade = 0.0018
vel = 0.25
forca_pulo = -0.6
forca_pulo2 = -0.55

# Spiked ball
pivo_x = 0                 
pivo_y = 0
comprimento = 150          # tamanho da corrente
angulo_max = 0.98          # ângulo máximo do balanço
vel_bola = 0.0025          # velocidade do balanço
raio_bola = 24             # raio usado na colisão
tem_bola = False           # só desenha a bola se a fase tiver a letra B

# Serra 
tem_serra = False          # só aparece se a fase tiver a letra O
serra_x = 0                
serra_topo = 0
serra_percurso = 200       # quanto ela desce
vel_serra = 0.002          # velocidade do sobe e desce
raio_serra = 30            # raio usado na colisão 
serra_y = 0

inicio_x = 0               # vem da letra P do mapa
inicio_y = 0

# Maçãs: posição (x, y)
lista_macas = []
total_macas = 0
macas = 0                  # quantas já pegou

fases = ["fase1.txt", "fase2.txt"]
fase_atual = 0
terminou = False           # True quando pegou todas as maçãs da fase
max_vidas = 3              # cada fase começa com 3 vidas
vidas = max_vidas

tela = "menu"              # "menu" ou "jogando"

bonecos = ["Mask Dude", "Ninja Frog", "Pink Man", "Virtual Guy"]
boneco = 0                 # índice do boneco escolhido

# Ordem dos quadros da fonte (10 por linha). Os 4 espaços completam a linha do U ao Z
letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ    0123456789.,:?!()+-"


def load_mapa(filename): #Lê o conteúdo do arquivo para a matriz
    global mapa
    mapa = []
    file = open(filename, "r")
    i = 0
    for line in file.readlines():
        mapa.append([])
        for j in line:
            if j != "\n":
                mapa[i].append(j)
        i = i + 1
    file.close()


def load_tiles(filename):
    global tileset_image, background_image
    tileset_image = pygame.image.load(filename).convert_alpha()
    tileset_image = pygame.transform.scale(tileset_image, (tileset_image.get_width() * scale, tileset_image.get_height() * scale))
    background_image = pygame.image.load("assets/Background/Gray.png").convert()
    background_image = pygame.transform.scale(background_image, (64 * scale, 64 * scale))


def load_frames(filename, quantidade, tamanho=32): #Corta a imagem em quadros quadrados
    imagem = pygame.image.load(filename).convert_alpha()
    frames = []
    for i in range(quantidade):
        frame = imagem.subsurface((i * tamanho, 0, tamanho, tamanho))
        frame = pygame.transform.scale(frame, (tamanho * scale, tamanho * scale))
        frames.append(frame)
    return frames


def ler_letras(): #Procura M, B, O, S e P no mapa e troca por vazio
    global pivo_x, pivo_y, inicio_x, inicio_y, lista_macas, total_macas, lista_surpresa
    global tem_bola, tem_serra, serra_x, serra_topo
    lista_macas = []
    lista_surpresa = []
    tem_bola = False
    tem_serra = False
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == "M":
                lista_macas.append((j * tile_size + 16, i * tile_size + 16))
                mapa[i][j] = "."
            elif mapa[i][j] == "B":
                pivo_x = j * tile_size
                pivo_y = i * tile_size
                tem_bola = True
                mapa[i][j] = "."
            elif mapa[i][j] == "O":
                serra_x = j * tile_size + tile_size // 2
                serra_topo = i * tile_size + tile_size // 2
                tem_serra = True
                mapa[i][j] = "."
            elif mapa[i][j] == "S":
                lista_surpresa.append([j, i, -1]) #coluna, linha, espera (-1 = escondido, -2 = já apareceu)
                mapa[i][j] = "."
            elif mapa[i][j] == "P":
                inicio_x = j * tile_size
                inicio_y = (i + 1) * tile_size - 64
                mapa[i][j] = "."
    total_macas = len(lista_macas)


def carregar_fase(): #Carrega o mapa da fase atual e começa ela do zero
    global macas, terminou, tempo, angulo, bola_x, bola_y, vidas, serra_y
    load_mapa(fases[fase_atual])
    ler_letras()
    macas = 0
    vidas = max_vidas
    terminou = False
    tempo = 0
    angulo = 0
    bola_x = pivo_x
    bola_y = pivo_y + comprimento
    serra_y = serra_topo
    renascer()


def carregar_boneco(): #Carrega as animações do boneco escolhido
    global anim_parado, anim_andando, anim_pulo, anim_queda, anim_pulo_duplo, anim_morte
    pasta = "assets/Main Characters/" + bonecos[boneco] + "/"
    anim_parado = load_frames(pasta + "Idle (32x32).png", 11)
    anim_andando = load_frames(pasta + "Run (32x32).png", 12)
    anim_pulo = load_frames(pasta + "Jump (32x32).png", 1)
    anim_queda = load_frames(pasta + "Fall (32x32).png", 1)
    anim_pulo_duplo = load_frames(pasta + "Double Jump (32x32).png", 6)
    anim_morte = load_frames(pasta + "Hit (32x32).png", 7)


def criar_coracoes(): #Desenha o coração (cheio e vazio) pixel por pixel
    global coracao_cheio, coracao_vazio
    #Coração em pixel art: cada letra é um pixel (o = contorno, r = vermelho, b = brilho)
    desenho = [
        ".oo..oo.",
        "orboorro",
        "orrrrrro",
        "orrrrrro",
        ".orrrro.",
        "..orro..",
        "...oo...",
    ]
    coracao_cheio = pygame.Surface((8, 7), pygame.SRCALPHA)
    coracao_vazio = pygame.Surface((8, 7), pygame.SRCALPHA)
    for y in range(7):
        for x in range(8):
            letra = desenho[y][x]
            if letra == "o":
                coracao_cheio.set_at((x, y), (60, 20, 30))
                coracao_vazio.set_at((x, y), (60, 60, 70))
            elif letra == "r":
                coracao_cheio.set_at((x, y), (220, 40, 50))
                coracao_vazio.set_at((x, y), (130, 130, 140))
            elif letra == "b":
                coracao_cheio.set_at((x, y), (255, 150, 150))
                coracao_vazio.set_at((x, y), (170, 170, 180))
    coracao_cheio = pygame.transform.scale(coracao_cheio, (8 * 5, 7 * 5))
    coracao_vazio = pygame.transform.scale(coracao_vazio, (8 * 5, 7 * 5))


def load():
    global clock, direcao
    global anim_aparecer
    global bola_img, corrente_img, espinho_img, anim_serra, trilho_img
    global anim_maca, fonte_img, botao_img, botao, reiniciar_img
    global menu_frames, menu_rects, play_img, play_rect
    clock = pygame.time.Clock()
    load_tiles("assets/Terrain/Terrain (16x16).png")

    carregar_boneco()
    anim_aparecer = load_frames("assets/Main Characters/Appearing (96x96).png", 7, 96)

    bola_img = pygame.image.load("assets/Traps/Spiked Ball/Spiked Ball.png").convert_alpha()
    bola_img = pygame.transform.scale(bola_img, (28 * scale, 28 * scale))
    corrente_img = pygame.image.load("assets/Traps/Spiked Ball/Chain.png").convert_alpha()
    corrente_img = pygame.transform.scale(corrente_img, (8 * scale, 8 * scale))

    anim_serra = load_frames("assets/Traps/Saw/On (38x38).png", 8, 38)
    trilho_img = pygame.image.load("assets/Traps/Saw/Chain.png").convert_alpha()
    trilho_img = pygame.transform.scale(trilho_img, (8 * scale, 8 * scale))

    espinho_img = pygame.image.load("assets/Traps/Spikes/Idle.png").convert_alpha()
    espinho_img = pygame.transform.scale(espinho_img, (16 * scale, 16 * scale))

    anim_maca = load_frames("assets/Items/Fruits/Apple.png", 17)
    fonte_img = pygame.image.load("assets/Menu/Text/Text (Black) (8x10).png").convert_alpha()

    criar_coracoes()

    botao_img = pygame.image.load("assets/Menu/Buttons/Next.png").convert_alpha()
    botao_img = pygame.transform.scale(botao_img, (21 * 3, 22 * 3))
    botao = botao_img.get_rect(topleft=(width // 2 - 31, height // 2 + 10))

    #Menu: título, os 4 bonecos (ampliados 2x de novo) e o botão Play
    menu_frames = []
    menu_rects = []
    for k in range(len(bonecos)):
        frames = load_frames("assets/Main Characters/" + bonecos[k] + "/Idle (32x32).png", 11)
        for n in range(len(frames)):
            frames[n] = pygame.transform.scale(frames[n], (128, 128))
        menu_frames.append(frames)
        menu_rects.append(pygame.Rect(192 + k * 192, 200, 128, 128))

    play_img = pygame.image.load("assets/Menu/Buttons/Play.png").convert_alpha()
    reiniciar_img = pygame.transform.scale(play_img, (21 * 3, 22 * 3)) #Mesmo tamanho e lugar do botão Next
    play_img = pygame.transform.scale(play_img, (21 * 4, 22 * 4))
    play_rect = play_img.get_rect(topleft=(width // 2 - 42, 400))

    direcao = 1          #1 = direita, -1 = esquerda


def tile_solido(i, j): #Diz se o tile da linha i e coluna j bloqueia o personagem
    if i < 0 or i >= len(mapa) or j < 0 or j >= len(mapa[i]):
        return True
    return mapa[i][j] == "#" or mapa[i][j] in tiles_grama


def colide(x, y): #Diz se o personagem na posição (x, y) está batendo em algum tile
    esquerda = int((x + hit_x) // tile_size)
    direita = int((x + hit_x + hit_w - 1) // tile_size)
    cima = int((y + hit_y) // tile_size)
    baixo = int((y + hit_y + hit_h - 1) // tile_size)
    for i in range(cima, baixo + 1):
        for j in range(esquerda, direita + 1):
            if tile_solido(i, j):
                return True
    return False


def pegar_macas(): #Pega as maçãs que o personagem está tocando
    global macas
    personagem = pygame.Rect(px + hit_x, py + hit_y, hit_w, hit_h)
    for maca in list(lista_macas): #Percorre uma cópia, porque vamos remover itens da lista
        retangulo = pygame.Rect(maca[0] - 12, maca[1] - 14, 24, 28)
        if personagem.colliderect(retangulo):
            lista_macas.remove(maca)
            macas = macas + 1


def renascer(): #Volta o personagem para a posição inicial
    global px, py, vy, no_chao, pulos, estado, tempo_anim
    esconder_espinhos()
    px = inicio_x
    py = inicio_y
    vy = 0
    no_chao = False
    pulos = 0
    estado = "nascendo"
    tempo_anim = 0


def update_armadilhas(dt): #Balança a bola como um pêndulo e sobe e desce a serra
    global tempo, angulo, bola_x, bola_y, serra_y
    tempo = tempo + dt
    angulo = angulo_max * math.cos(tempo * vel_bola)
    bola_x = pivo_x + comprimento * math.sin(angulo)
    bola_y = pivo_y + comprimento * math.cos(angulo)
    serra_y = serra_topo + serra_percurso * (1 - math.cos(tempo * vel_serra)) / 2


def acertou_circulo(cx, cy, raio): #Vê se o círculo encostou na caixa de colisão do personagem
    esquerda = px + hit_x
    cima = py + hit_y
    perto_x = max(esquerda, min(cx, esquerda + hit_w)) #Ponto do personagem mais perto do círculo
    perto_y = max(cima, min(cy, cima + hit_h))
    dx = cx - perto_x
    dy = cy - perto_y
    return dx * dx + dy * dy < raio * raio


def esconder_espinhos(): #Os espinhos surpresa voltam a ficar escondidos
    for s in lista_surpresa:
        mapa[s[1]][s[0]] = "."
        s[2] = -1


def atualizar_surpresas(dt): #Espinho aparece depois de um tempo aleatório quando o personagem chega perto
    for s in lista_surpresa:
        centro_x = s[0] * tile_size + tile_size // 2
        pe_y = py + 64 
        perto_x = abs(px + 32 - centro_x) < 3 * tile_size
        perto_y = abs(pe_y - (s[1] + 1) * tile_size) < 2 * tile_size
        if s[2] == -1 and perto_x and perto_y:
            s[2] = random.randint(0, 300) 
        if s[2] >= 0:
            s[2] = s[2] - dt
            if s[2] < 0:
                mapa[s[1]][s[0]] = "^"
                s[2] = -2


def espinho_acertou(): #Vê se o personagem encostou nas pontas de algum espinho
    personagem = pygame.Rect(px + hit_x, py + hit_y, hit_w, hit_h)
    esquerda = int(personagem.left // tile_size)
    direita = int((personagem.right - 1) // tile_size)
    cima = int(personagem.top // tile_size)
    baixo = int((personagem.bottom - 1) // tile_size)
    for i in range(cima, baixo + 1):
        for j in range(esquerda, direita + 1):
            if i >= 0 and i < len(mapa) and j >= 0 and j < len(mapa[i]) and mapa[i][j] == "^":
                #As pontas ficam só na metade de baixo do tile
                ponta = pygame.Rect(j * tile_size + 4, i * tile_size + 20, tile_size - 8, tile_size - 20)
                if personagem.colliderect(ponta):
                    return True
    return False


def pular():
    global vy, pulos, tempo_anim
    if tela == "menu": #No menu não pula
        return
    if estado == "morrendo" or estado == "nascendo": #Morto ou aparecendo não pula
        return
    if no_chao:
        vy = forca_pulo
        pulos = 1
    elif pulos < 2: #Já está no ar: pulo duplo
        vy = forca_pulo2
        pulos = 2
        tempo_anim = 0


def update(dt):
    global px, py, vy, direcao, estado, tempo_anim, no_chao, pulos, terminou, vidas
    if dt > 50: #Se travar, não deixa o personagem atravessar o chão
        dt = 50

    if tela == "menu": #No menu nada se mexe
        return

    if terminou: #Pegou todas as maçãs: o jogo fica parado
        return

    #Morrendo: o personagem fica parado até a animação acabar, depois renasce
    if estado == "morrendo":
        tempo_anim = tempo_anim + dt
        update_armadilhas(dt)
        if tempo_anim > 7 * 80 + 300: #7 quadros de 80ms + uma pausa
            if vidas == 0:
                carregar_fase() #Perdeu todas as vidas: a fase começa do zero
            else:
                renascer()
        return

    #Nascendo: fica parado até a animação de aparecer acabar
    if estado == "nascendo":
        tempo_anim = tempo_anim + dt
        update_armadilhas(dt)
        if tempo_anim > 7 * 80: #7 quadros de 80ms
            estado = "parado"
            tempo_anim = 0
        return

    teclas = pygame.key.get_pressed()
    andar = 0
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        andar = andar - 1
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        andar = andar + 1
    if andar != 0:
        direcao = andar

    #Movimento na horizontal: se bater na parede, volta um pouquinho até sair dela
    px = px + (vel * dt * andar)
    while andar != 0 and colide(px, py):
        px = px - andar * 0.1

    #Movimento na vertical (gravidade)
    vy = vy + gravidade * dt
    if vy > 0.6:
        vy = 0.6
    py = py + vy * dt
    no_chao = False
    if colide(px, py):
        while colide(px, py):
            if vy > 0:
                py = py - 0.1 #Estava caindo: sobe até ficar em cima do chão
            else:
                py = py + 0.1 #Estava subindo: desce até sair do teto
        if vy > 0:
            no_chao = True
            pulos = 0
        vy = 0

    #Escolhe a animação
    if no_chao and andar != 0:
        novo_estado = "andando"
    elif no_chao:
        novo_estado = "parado"
    elif vy < 0 and pulos == 2:
        novo_estado = "pulo duplo"
    elif vy < 0:
        novo_estado = "pulo"
    else:
        novo_estado = "queda"
    if novo_estado != estado:
        estado = novo_estado
        tempo_anim = 0
    tempo_anim = tempo_anim + dt

    #Armadilhas
    update_armadilhas(dt)
    atualizar_surpresas(dt)
    if (tem_bola and acertou_circulo(bola_x, bola_y, raio_bola)) or (tem_serra and acertou_circulo(serra_x, serra_y, raio_serra)) or espinho_acertou():
        estado = "morrendo"
        tempo_anim = 0
        vidas = vidas - 1
    else:
        pegar_macas()
        if len(lista_macas) == 0:
            terminou = True


def tile_moldura(i, j): #Escolhe qual pedaço da moldura de pedra usar
    ultima_linha = len(mapa) - 1
    ultima_coluna = len(mapa[i]) - 1
    if i == 0:
        if j == 0:
            return (0, 0)
        if j == ultima_coluna:
            return (2, 0)
        return (1, 0)
    if i == ultima_linha:
        if j == 0:
            return (0, 2)
        if j == ultima_coluna:
            return (2, 2)
        return (1, 2)
    if j == 0:
        return (0, 1)
    return (2, 1)


def draw_tile(screen, pos, tile): #Desenha o tile (coluna, linha) do tileset na posição pos
    quad = (tile[0] * tile_size, tile[1] * tile_size, tile_size, tile_size)
    screen.blit(tileset_image, pos, quad)


def escrever(screen, texto, x, y, escala): #Escreve o texto com a fonte pixelada da imagem
    texto = texto.upper()
    for k in range(len(texto)):
        pos = letras.find(texto[k]) 
        if pos >= 0:
            quadro = fonte_img.subsurface(((pos % 10) * 8, (pos // 10) * 10, 8, 10))
            quadro = pygame.transform.scale(quadro, (8 * escala, 10 * escala))
            screen.blit(quadro, (x + k * 8 * escala, y))


def desenhar_menu(screen):
    escrever(screen, "Jogo", width // 2 - 64, 80, 4) #4 letras de 32 pixels
    numero = (pygame.time.get_ticks() // 60) % len(menu_frames[0]) #Animação parada dos bonecos
    for k in range(len(menu_rects)):
        r = menu_rects[k]
        pygame.draw.rect(screen, (255, 255, 255), r.inflate(16, 16))
        if k == boneco:
            pygame.draw.rect(screen, (59, 130, 212), r.inflate(16, 16), 6) #Borda do escolhido
        else:
            pygame.draw.rect(screen, (170, 170, 170), r.inflate(16, 16), 2)
        screen.blit(menu_frames[k][numero], r)
    screen.blit(play_img, play_rect)


def desenhar_vidas(screen): #Corações no alto da esquerda (vazio = vida perdida)
    for k in range(max_vidas):
        if k < vidas:
            screen.blit(coracao_cheio, (44 + k * 48, 44))
        else:
            screen.blit(coracao_vazio, (44 + k * 48, 44))


def draw_screen(screen):
    for y in range(0, height, 64 * scale): #Fundo repetido
        for x in range(0, width, 64 * scale):
            screen.blit(background_image, (x, y))

    if tela == "menu":
        desenhar_menu(screen)
        return

    for i in range(len(mapa)): #Percorre a matriz e desenha imagens quadradas
        for j in range(len(mapa[i])):
            pos = ((j * tile_size), (i * tile_size))
            if mapa[i][j] == "#":
                draw_tile(screen, pos, tile_moldura(i, j))
            elif mapa[i][j] in tiles_grama:
                draw_tile(screen, pos, tiles_grama[mapa[i][j]])
            elif mapa[i][j] == "^":
                screen.blit(espinho_img, pos)

    #Maçãs (o desenho tem 64x64, mas a fruta fica no meio dele)
    numero_maca = int(tempo / 50) % len(anim_maca)
    for maca in lista_macas:
        screen.blit(anim_maca[numero_maca], (maca[0] - 32, maca[1] - 28))

    #Corrente (vários pedacinhos entre o bloco e a bola)
    if tem_bola:
        for k in range(0, comprimento // 16):
            cx = pivo_x + math.sin(angulo) * k * 16
            cy = pivo_y + math.cos(angulo) * k * 16
            screen.blit(corrente_img, (cx - 8, cy - 8))

    #Trilho da serra (corrente reta de cima até onde ela chega embaixo)
    if tem_serra:
        for y in range(serra_topo, serra_topo + serra_percurso + 1, 16):
            screen.blit(trilho_img, (serra_x - 8, y - 8))

    #Personagem
    if estado == "morrendo":
        frames = anim_morte
    elif estado == "nascendo":
        frames = anim_aparecer
    elif estado == "parado":
        frames = anim_parado
    elif estado == "andando":
        frames = anim_andando
    elif estado == "pulo":
        frames = anim_pulo
    elif estado == "pulo duplo":
        frames = anim_pulo_duplo
    else:
        frames = anim_queda

    if estado == "morrendo" or estado == "nascendo": #Toca uma vez só e fica no último quadro
        numero = min(int(tempo_anim / 80), len(frames) - 1)
    else:
        numero = int(tempo_anim / 60) % len(frames) #Troca de quadro a cada 60ms
    imagem = frames[numero]
    if direcao == -1:
        imagem = pygame.transform.flip(imagem, True, False)
    if estado == "nascendo": #O quadro é 96x96 (192 ampliado), então centraliza no personagem
        screen.blit(imagem, (px + 32 - 96, py + 32 - 96))
    else:
        screen.blit(imagem, (px, py))

    #Bola e serra (desenhadas por cima)
    if tem_bola:
        screen.blit(bola_img, (bola_x - 28, bola_y - 28))
    if tem_serra:
        numero_serra = int(tempo / 40) % len(anim_serra) #Gira a cada 40ms
        screen.blit(anim_serra[numero_serra], (serra_x - 38, serra_y - 38))

    #Fase concluída: caixa no meio da tela com a mensagem
    if terminou:
        pygame.draw.rect(screen, (255, 255, 255), (width // 2 - 160, height // 2 - 70, 320, 160))
        pygame.draw.rect(screen, (40, 40, 40), (width // 2 - 160, height // 2 - 70, 320, 160), 4)
        if fase_atual == len(fases) - 1:
            texto = "Voce venceu!"
            screen.blit(reiniciar_img, botao)
        else:
            texto = "Fase concluida!"
            screen.blit(botao_img, botao)
        escrever(screen, texto, width // 2 - len(texto) * 8 * 2 // 2, height // 2 - 45, 2)

    desenhar_vidas(screen)

    #Contador de maçãs no alto da direita
    texto = str(macas) + " de " + str(total_macas)
    largura = len(texto) * 8 * 2
    icone = pygame.transform.scale(anim_maca[0], (48, 48))
    escrever(screen, texto, width - largura - 48, 52, 2)
    screen.blit(icone, (width - largura - 100, 38))


def main_loop(screen):
    global clock, fase_atual, boneco, tela
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                break
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE or e.key == pygame.K_UP or e.key == pygame.K_w:
                    pular()
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if tela == "menu":
                    for k in range(len(menu_rects)):
                        if menu_rects[k].collidepoint(e.pos):
                            boneco = k
                            carregar_boneco()
                    if play_rect.collidepoint(e.pos):
                        tela = "jogando"
                        carregar_fase()
                elif terminou and botao.collidepoint(e.pos):
                    if fase_atual < len(fases) - 1:
                        fase_atual = fase_atual + 1
                    else:
                        fase_atual = 0 #Ganhou o jogo: recomeça da fase 1
                    carregar_fase()

        # Define FPS máximo
        clock.tick(60)
        # Calcula tempo transcorrido desde a última atualização
        dt = clock.get_time()
        # Desenha objetos na tela
        draw_screen(screen)
        # Atualiza posição dos objetos da tela
        update(dt)
        # Pygame atualiza o seu estado
        pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo")
load()
main_loop(screen)
pygame.quit()
