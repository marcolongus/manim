from manim import *

# manim -qm -p file.py class_scene_name
# Every animation will be a class. 
# Inherits from Scene.
# Anatomy:
# Scene: animation canvas
# Mobjects: Manim objecst.
# Global constanants: colors, directions, etc/
# docs.manim.community 

class FirstExample(Scene):
	
	def construct(self):
		blue_circle = Circle(color=BLUE, fill_opacity=0.5)
		green_square = Square(color=RED, fill_opacity=0.8)
		green_square.next_to(blue_circle, RIGHT)
		self.add(blue_circle, green_square)