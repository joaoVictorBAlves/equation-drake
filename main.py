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
""" Components vars """
BACKGROUND = pygame.image.load(os.path.join('Assets', 'background.png'))
TITLE = pygame.image.load(os.path.join('Assets', 'titulo.png'))
BTN_O = pygame.image.load(os.path.join('Assets', 'btnOtimista.png'))
BTN_P = pygame.image.load(os.path.join('Assets', 'btnPessimista.png'))
BTN_R = pygame.image.load(os.path.join('Assets', 'btnAleatorio.png'))
DRAKE = pygame.image.load(os.path.join('Assets', 'drake.png'))
""" State of the vertex """
RESULT_LIST = []
STEPS_LIST = []
VERTEX_LIST = []
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

    pygame.display.update()


""" Drawing Methods """
def draw_vertex(x, y, r, name, value):
    if name in STEPS_LIST:
        pygame.draw.circle(WIN, (21, 199, 17, 70), (x+r, y+r), r)
    pygame.draw.circle(WIN, (255, 255, 255), (x+r, y+r), r, 2)
    text_name = FONT.render(name, 1, (255, 255, 255))
    text_rect_name = text_name.get_rect(center=(x+r, y+r-12))
    WIN.blit(text_name, text_rect_name)
    text_value = FONT_VALUE.render(str(value), 1, (255, 255, 255))
    text_rect_value = text_value.get_rect(center=(x + r, y + r + 7))
    WIN.blit(text_value, text_rect_value)


def draw_graph():
    """ edges """

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

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_o]:
            pass
        if key_pressed[pygame.K_p]:
            pass
        if key_pressed[pygame.K_a]:
            pass
        """ Drawing in the screen """
        draw()
    pygame.quit()


if __name__ == "__main__":
    simulator = Simulator()
    simulator.start_world()
    VERTEX_LIST = simulator.galaxyGraph.vertices
    main()
