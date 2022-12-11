from Simulator import Simulator
import pygame
import os
pygame.font.init()


""" Screen vars """
WIDTH = 900
HEIGHT = 450
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulador da Equação de Drake")
FPS = 60
FONT = pygame.font.SysFont("Arial", 15)
FONT_VALUE = pygame.font.SysFont("Arial", 12)
FONT_RESULT = pygame.font.SysFont("Arial", 18)

""" Components vars """
BACKGROUND = pygame.image.load(os.path.join('Assets', 'background.png'))
TITLE = pygame.image.load(os.path.join('Assets', 'titulo.png'))
BTN_O = pygame.image.load(os.path.join('Assets', 'btnOtimista.png'))
BTN_P = pygame.image.load(os.path.join('Assets', 'btnPessimista.png'))
BTN_R = pygame.image.load(os.path.join('Assets', 'btnAleatorio.png'))
DRAKE = pygame.image.load(os.path.join('Assets', 'drake.png'))
RESULT_BALOON = pygame.image.load(os.path.join('Assets', 'resultBaloon.png'))

""" State of the vertex """
STEPS_LIST = []
VERTEX_LIST = []
EDGES_LIST = []
RESULT = 0
RESULT_TYPE = 0
# Maybe these vars will change of position in code


def draw():
    """ Widgets """
    WIN.fill((255, 255, 255))
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(TITLE, (26, 49))
    WIN.blit(BTN_O, (49, 383))
    WIN.blit(BTN_P, (172, 383))
    WIN.blit(BTN_R, (295, 383))
    WIN.blit(DRAKE, (715, 265))
    """ Graph """
    draw_graph()
    """ Result """
    if RESULT:
        draw_result()
    pygame.display.update()


""" Drawing Methods """
def draw_vertex(x, y, r, name, value):
    """ Circle """
    if name in STEPS_LIST:
        pygame.draw.circle(WIN, (21, 199, 17, 70), (x+r, y+r), r)
    else:
        pygame.draw.circle(WIN, (0, 0, 0), (x + r, y + r), r)
    pygame.draw.circle(WIN, (255, 255, 255), (x+r, y+r), r, 2)
    """ Text """
    if value == 10000000000:
        value = "10e9"
    text_name = FONT.render(name, 1, (255, 255, 255))
    text_rect_name = text_name.get_rect(center=(x+r, y+r-12))
    WIN.blit(text_name, text_rect_name)
    text_value = FONT_VALUE.render(str(value), 1, (255, 255, 255))
    text_rect_value = text_value.get_rect(center=(x + r, y + r + 7))
    WIN.blit(text_value, text_rect_value)

def draw_edge(xa, ya, xb, yb, weight):
    radius = 28.79
    if weight == 1:
        pygame.draw.line(WIN, (0, 255, 0), (xa + radius, ya + radius), (xb + radius, yb + radius))
    elif weight == -1:
        pygame.draw.line(WIN, (255, 0, 0), (xa + radius, ya + radius), (xb + radius, yb + radius))
    else:
        pygame.draw.line(WIN, (255, 255, 255), (xa + radius, ya + radius), (xb + radius, yb + radius))

def draw_graph():
    """ edges """
    draw_edge(49, 196, 126, 196, EDGES_LIST[0].weight)     # R >> Fp
    draw_edge(126, 196, 200.14, 139, EDGES_LIST[1].weight)     # Fp >> NeO
    draw_edge(126, 196, 200.14, 254.15, EDGES_LIST[2].weight)     # Fp >> NeP
    draw_edge(200.14, 139, 275.71, 139, EDGES_LIST[3].weight)      # NeO >>  FlO
    draw_edge(200.14, 139, 275.71, 254.15, EDGES_LIST[4].weight)      # NeO >>  FlP
    draw_edge(200.14, 254.15, 275.71, 139, EDGES_LIST[5].weight)  # NeP >>  FlO
    draw_edge(200.14, 254.15, 275.71, 254.15, EDGES_LIST[6].weight)  # NeP >>  FlP
    draw_edge(275.71, 139, 351.28, 139, EDGES_LIST[7].weight)  # FlO >>  FiO
    draw_edge(275.71, 139, 351.28, 254.15, EDGES_LIST[8].weight)  # FlO >>  FiP
    draw_edge(275.71, 254.15, 351.28, 139, EDGES_LIST[9].weight)  # FlP >>  FiO
    draw_edge(275.71, 254.15, 351.28, 254.15, EDGES_LIST[10].weight)  # FlP >>  FiP
    draw_edge(351.28, 139, 426.85, 196.58, EDGES_LIST[11].weight)  # FiO >>  Fc
    draw_edge(351.28, 254.15, 426.85, 196.58, EDGES_LIST[12].weight)  # FlP >>  Fc
    draw_edge(426.85, 196.58, 502.42, 139, EDGES_LIST[13].weight)  # Fc >>  LO
    draw_edge(426.85, 196.58, 502.42, 254.15, EDGES_LIST[14].weight)  # Fc >>  LP
    """ vertices """
    draw_vertex(49, 196, 28.79, VERTEX_LIST[0].data[0], VERTEX_LIST[0].data[1])
    draw_vertex(126, 196, 28.79, VERTEX_LIST[1].data[0], VERTEX_LIST[1].data[1])
    draw_vertex(200.14, 139, 28.79, VERTEX_LIST[2].data[0], VERTEX_LIST[2].data[1])
    draw_vertex(200.14, 254.15, 28.79, VERTEX_LIST[3].data[0], VERTEX_LIST[3].data[1])
    draw_vertex(275.71, 139, 28.79, VERTEX_LIST[4].data[0], VERTEX_LIST[4].data[1])
    draw_vertex(275.71, 254.15, 28.79, VERTEX_LIST[5].data[0], VERTEX_LIST[5].data[1])
    draw_vertex(351.28, 139, 28.79, VERTEX_LIST[6].data[0], VERTEX_LIST[6].data[1])
    draw_vertex(351.28, 254.15, 28.79, VERTEX_LIST[7].data[0], VERTEX_LIST[7].data[1])
    draw_vertex(426.85, 196.58, 28.79, VERTEX_LIST[8].data[0], VERTEX_LIST[8].data[1])
    draw_vertex(502.42, 139, 28.79, VERTEX_LIST[9].data[0], VERTEX_LIST[9].data[1])
    draw_vertex(502.42, 254.15, 28.79, VERTEX_LIST[10].data[0], VERTEX_LIST[10].data[1])

def draw_result():
    if RESULT_TYPE == 1:
        color = (0, 255, 0)
    elif RESULT_TYPE == -1:
        color = (255, 0, 0)
    else:
        color = (255, 255, 255)

    WIN.blit(RESULT_BALOON, (640.5, 201.5))
    text_value = FONT_RESULT.render(str(RESULT), 1, color)
    text_rect_value = text_value.get_rect(center=(741, 225))
    WIN.blit(text_value, text_rect_value)
def equation(option=None):
    global RESULT
    global STEPS_LIST
    global RESULT_TYPE
    if option is None:
        result = simulator.drake_equation()
        RESULT = result[1]
        STEPS_LIST = result[0]
        RESULT_TYPE = 0
    else:
        if option == "MAX":
            result = simulator.drake_equation(option)
            RESULT = result[1]
            STEPS_LIST = result[0]
            RESULT_TYPE = 1
        else:
            result = simulator.drake_equation(option)
            RESULT = result[1]
            STEPS_LIST = result[0]
            RESULT_TYPE = -1
    print(RESULT)


def main():
    clock = pygame.time.Clock()
    global FPS
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_o]:
            equation("MAX")
        if key_pressed[pygame.K_p]:
            equation("MIN")
        if key_pressed[pygame.K_a]:
            equation()
        """ Drawing in the screen """
        draw()
    pygame.quit()


if __name__ == "__main__":
    """ Start simulator """
    simulator = Simulator()
    simulator.start_world()
    
    VERTEX_LIST = simulator.galaxyGraph.vertices
    EDGES_LIST = simulator.galaxyGraph.edges
    """ Start game """
    main()
