from math import *
import sympy as sp


def derivada(expr, variables):
    for der_respect in variables:
        var = sp.Symbol(f'{der_respect}')
        funcion = sp.Derivative(expr, var, evaluate=True)
        print(f'La derivada parcial df/d{der_respect} =  {funcion}')


if __name__ == '__main__':
    variables = ['x', 'y', 'z']
    expr = input("\nFuncion a evaluar:    f(x,y,z)=")
    derivada(expr, variables)# Additional code to handle exceptions
    try:
        derivada(expr, variables)
    except Exception as e:
        print(f"An error occurred: {str(e)}")