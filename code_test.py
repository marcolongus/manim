from manim import *

class CodeFromString(Scene):
    def construct(self):
        with open('auxilary.py', 'r') as f:
            code = f.read()
        rendered_code = Code(code=code, tab_width=4, background="window",
                            language="Python", font="Monospace")
        self.add(rendered_code)