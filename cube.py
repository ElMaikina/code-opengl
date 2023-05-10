import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

vertices = np.array([
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1, -1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1, -1,  1],
    [-1,  1,  1]
], dtype=np.float32)

edges = np.array([
    [0, 1],
    [0, 3],
    [0, 4],
    [2, 1],
    [2, 3],
    [2, 7],
    [6, 3],
    [6, 4],
    [6, 7],
    [5, 1],
    [5, 4],
    [5, 7]
], dtype=np.uint32)

class Cube:
    def __init__(self):
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        self.ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, edges.nbytes, edges, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

    def draw(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo)
        glDrawElements(GL_LINES, len(edges)*2, GL_UNSIGNED_INT, None)

        glDisableVertexAttribArray(0)

def main():
    pygame.init()
    display = (960, 540)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LINE_SMOOTH)

    cube = Cube()

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    clock = pygame.time.Clock()
    while True:
        dt = clock.tick(9000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(10 * dt / 1000, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cube.draw()
        pygame.display.flip()

if __name__ == '__main__':
    main()
