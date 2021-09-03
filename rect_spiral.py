from svg_backend import SVGBackend
from turtle import Turtle
from grammar import Grammar

backend = SVGBackend()
turtle = Turtle(backend)

grammar = Grammar()

grammar.add_non_terminal('S', [
    lambda turtle: turtle.forward(1),
    lambda turtle: turtle.turn_right(89.5),
    lambda turtle: turtle.scale(0.99),
    'S'
])

grammar.expand('S', turtle, 500)
backend.write('rect_spiral.svg')
