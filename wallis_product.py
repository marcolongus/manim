from manim import *

aprox = [(2*i)**2/((2*i-1)*(2*i+1)) for i in range(1,1000)]
wallis_product = []
init_wallis = 1
for i in range(len(aprox)):
	init_wallis *= aprox[i]
	wallis_product.append(2*init_wallis)

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
		
		for i, f in enumerate(lista):
			if i>0: lista[0] = lista[0] + f

			new_formula = MathTex(f'W({i+1})=2 {lista[0]}')
			new_limite = MathTex(f'W({i+1})={round(wallis_product[i], 3)}').shift(2*DOWN)
			
			self.play(Transform(formula, new_formula), Transform(limite, new_limite))
			self.wait(0.5)

		self.play(Transform(formula, limite))
		self.play(FadeOut(limite))
		self.wait(0.5)
		
		for i in range(9, len(wallis_product) - 1, 100):
			new_limite = MathTex(f'W({i+1})={round(wallis_product[i], 4)}')
			self.play(Transform(formula, new_limite))
			self.wait(0.0001)






