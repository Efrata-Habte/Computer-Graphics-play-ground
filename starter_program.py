import random
import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
window_size = (500, 600)
pygame.display.set_mode(window_size, OPENGL)


gluPerspective(45, (window_size[0]/window_size[1]), 0.1, 150.0)
glTranslatef(0.0, 0.0, -10)

# draw dots


# draw sierpinski

# draw cosine graph

# draw polylines

    # GL__LINE_LOOP mode

# draw polygons, filled region


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_DEPTH_BUFFER_BIT)
    
    pygame.display.flip()
    pygame.time.wait(10)