#region imports
import pygame as pg
from OpenGL.GL import *
#endregion

#region constants
SCREEN_SIZE = (600,600)
SCREEN_COLOR = (0.5,0.0,0.25,1.0)
WINDOW_CREATION_FLAGS = pg.OPENGL | pg.DOUBLEBUF
FRAMERATE = 60
#endregion

#region program setup
pg.init()
screen = pg.display.set_mode(SCREEN_SIZE, WINDOW_CREATION_FLAGS)
clock = pg.time.Clock()
glClearColor(*SCREEN_COLOR)
# endregion

# region main loop
running = True
color = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            color = not color
    
    if color:
        glClear(GL_COLOR_BUFFER_BIT)
    else: 
        glClearColor(1.0,0,0,1.0)
        glClear(GL_COLOR_BUFFER_BIT)

    pg.display.flip()
    clock.tick(FRAMERATE) # to limit the speed and use CPU efficiently
# endregion

# region program cleanup
pg.quit()
# endregion