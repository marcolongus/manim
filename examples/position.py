from manim import *

class Positioning(Scene):
	def construct(self):
		plane = NumberPlane()
		self.add(plane)


		red_dot = Dot(color=RED)
		blue_dot =Dot(color=BLUE)
		
		# Next
		blue_dot.next_to(red_dot, RIGHT + UP) #Right=[1,0,0]
		self.add(red_dot, blue_dot)

		# Shift
		s = Square(color=ORANGE)
		s.shift(2*UP + 4*RIGHT)
		self.add(s)

		# move_to
		c = Circle(color=PURPLE)
		c.move_to([-3, -2, 0])
		self.add(c)

		# align_to
		c2 = Circle(radius=0.5, color=RED, fill_opacity=0.5)
		c3 = c2.copy().set_color(YELLOW)
		c4 = c2.copy().set_color(ORANGE)
		c2.align_to(s, UP)
		c3.align_to(s, RIGHT)
		c4.align_to(s, UP + RIGHT)

		self.add(c2, c3, c4)

class CriticalPoints(Scene):
	def construct(self):
		c = Circle(color=GREEN, fill_opacity=0.5)
		self.add(c)

		for d in [(0,0,0), UP, UR, RIGHT, DR, DOWN, DL, LEFT, UL]:
			self.add(Cross(scale_factor=0.2).move_to(c.get_critical_point(d)))