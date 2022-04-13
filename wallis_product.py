from manim import *


def wallis_prod(n):
	init_wallis = 1
	for i in range(1,n):
		init_wallis *= ((2*i)/(2*i - 1 ))*((2*i)/(2*i + 1))
		yield init_wallis

def advance_wallis(w, jump):
	for _ in range(jump): next(w)


class Wallis(Scene):

	def construct(self):
		titulo = Tex('Producto de Wallis', color=BLUE)
		titulo.shift(3*UP)
		formula = MathTex(r'W\left( N \right) = 2 \prod_{i=1}^N \left( \frac{2n}{2n+1} \right) \left( \frac{2n}{2n-1} \right)')
		limite = MathTex(r'N \rightarrow \infty \, , W\left( N \right) \rightarrow \pi')
		limite.shift(2*DOWN)
		self.add(titulo)
		self.play(FadeIn(formula), FadeIn(limite), run_time=2)
		self.wait(1)

		lista = [f'({2*i}/{2*i-1})({2*i}/{2*i+1}) ' for i in range(1,6)]
		wallis_p = wallis_prod(10000)

		for i, f in enumerate(lista):
			if i>0: lista[0] = lista[0] + f

			new_formula = MathTex(f'W({i+1})=2 {lista[0]}')
			new_limite = MathTex(f'W({i+1})={round(2*next(wallis_p), 3)}').shift(2*DOWN)
			
			self.play(Transform(formula, new_formula), Transform(limite, new_limite))
			self.wait(0.5)

		self.play(Transform(formula, limite))
		self.play(FadeOut(limite))
		self.wait(0.5)
		
		step = 100
		advance_wallis(wallis_p, 4)
		for i in range(9, 1000, step):
			new_limite = MathTex(f'W({i+1})={round(2*next(wallis_p), 4)}')
			advance_wallis(wallis_p, step-1)
			self.play(Transform(formula, new_limite))
			self.wait(0.0001)







