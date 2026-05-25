#region imports
import pygame as pg
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
#endregion

#region constants
SCREEN_SIZE = (600,600)
SCREEN_COLOR = (0.5,0.0,0.25,1.0)
WINDOW_CREATION_FLAGS = pg.OPENGL | pg.DOUBLEBUF
FRAMERATE = 60
#endregion

#region helper functions
def make_shader(vertex_filename: str, fragment_filename: str) -> int:
    vertex_module = make_shader_module(vertex_filename, GL_VERTEX_SHADER)
    fragment_module = make_shader_module(fragment_filename, GL_FRAGMENT_SHADER)
    return compileProgram(vertex_module, fragment_module)

def make_shader_module (filename: str, module_type: int) -> int:
    
    with open(filename,'r') as file:
        source_code = file.readlines()
        return compileShader(source_code, module_type)
# endregion 

#region classes
class Renderer:
    SCREEN_COLOR = (0.5,0.0,0.25,1.0)

    def __init__ (self):
        glClearColor(*Renderer.SCREEN_COLOR)

        self.VAO = glGenVertexArrays(1)
        glBindVertexArray(self.VAO)

        self.shader = make_shader('vertex.txt','fragment.txt')
    
    def draw(self) -> None:
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(self.shader)
        glDrawArrays(GL_TRIANGLES, 0, 3)

    def destroy(self) -> None:
        glDeleteProgram(self.shader)
# endregion

#region program setup
pg.init()
pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION,3)
pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
screen = pg.display.set_mode(SCREEN_SIZE, WINDOW_CREATION_FLAGS)
clock = pg.time.Clock()
renderer = Renderer()
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
    
    # if color:
    #     glClear(GL_COLOR_BUFFER_BIT)
    # else: 
    #     glClearColor(1.0,0,0,1.0)
    #     glClear(GL_COLOR_BUFFER_BIT)

    renderer.draw()
    pg.display.flip()
    clock.tick(FRAMERATE) # to limit the speed and use CPU efficiently
# endregion

# region program cleanup
renderer.destroy()
pg.quit()
# endregion