import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, 0, 0),
    (1, 0, 1),
    (0, 0, 1),
    (0, 0, 0),
    (0.5, 1, 0.5)
)

caras = (
    (0, 1, 2, 3),
    (0, 1, 4),
    (1, 2, 4),
    (2, 3, 4),
    (3, 0, 4)
)

def Piramide():
    glBegin(GL_QUADS)
    for cara in caras:
        glColor3fv((1,0,0))
        for vertice in cara:
            glVertex3fv(vertices[vertice])
    glEnd()

    glBegin(GL_TRIANGLES)
    for cara in caras[1:]:
        glColor3fv((0,1,0))
        for vertice in cara:
            glVertex3fv(vertices[vertice])
    glEnd()

def main():
    pygame.init()
    display = (960, 540)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0,-5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glRotatef(1, 0, 1, 0)
        Piramide()
        pygame.display.flip()
        pygame.time.wait(1)

main()