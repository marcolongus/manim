from manim import *

class MyScene(Scene):
    def construct(self):
        t = Text('Hola mundo', font_size=23, color=BLUE)
        
        self.play(Create(t))