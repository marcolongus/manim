from manim import *

# Scene.add -> add Mobjects to casnvas.
# Scene.wait -> Pause
# Scene.play -> Plays animations
# Animations can: add mobjects (create, FadeIn,..)
# 				  change mobjects (Transform,..)
# 				  emphasize mobjects(Indicate, Circumscribe,..)
# 				remove mobjects(Uncreate, FadeOut)

class function_plot(Scene):
	def construct(self):
		ax = Axes(x_range=(-3, 3), y_range=(-3, 3))
		curve = ax.plot(lambda x: (x+2)*(x-1)*(x+1), color=RED)
		other_curve = ax.plot(lambda x: x**2, color=BLUE)
		area = ax.get_area(curve, x_range = (-2,0))
		#self.add(ax, curve, area)
		self.play(Create(ax), Create(curve), run_time=3)
		#self.play(Create(area))
		self.play(FadeIn(area, run_time=4), Create(other_curve, run_time=2))
		self.wait(2)

class SquareToCircle(Scene):
	def construct(self):
		square = Square(color=BLUE, fill_opacity=0.5)
		circle = Circle(color=RED, fill_opacity=0.5)
		self.play(DrawBorderThenFill(square))
		self.wait(1)
		self.play(Transform(square, circle))
		self.play(Indicate(circle))
		self.play(FadeOut(square))
