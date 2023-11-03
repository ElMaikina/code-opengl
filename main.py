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


# Initialize Pygame
pygame.init()
width, height = 640, 360
display = (width, height)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Set up the perspective for the 3D scene
gluPerspective(120, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Initial camera position and rotation
x, y, z = 0, 0, 0
camera_rotation = [0, 0, 0]

# Set the maximum frame rate to 120 FPS
clock = pygame.time.Clock()

# Create a Cube
cubes = []
cubes.append(Cube())

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Handle keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        z += 0.001
    if keys[pygame.K_DOWN]:
        z -= 0.001
    if keys[pygame.K_LEFT]:
        camera_rotation[1] += 1
    if keys[pygame.K_RIGHT]:
        camera_rotation[1] -= 1

    # Clear the screen and set background color
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.2, 0.2, 0.2, 1.0)

    # Set the new camera position and rotation
    glTranslatef(x, y, z)
    glRotatef(camera_rotation[1], 0, 1, 0)

    # Example: Draw a cube
    #glBegin(GL_QUADS)
    #glVertex3f(1, -1, -1)
    #glVertex3f(1, 1, -1)
    #glVertex3f(-1, 1, -1)
    #glVertex3f(-1, -1, -1)
    #glEnd()

    for cube in cubes:
        cube.draw()

    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 120 FPS
    clock.tick(120)
