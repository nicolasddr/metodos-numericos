from pymep.realParser import parse
from pymep.realParser import eval
import math

func = input('Digite a função:\n')
a = float(input('Digite o ponto de início do intervalo: '))
b = float(input('Digite o ponto final do intervalo: '))
e = float(input('Digite o erro desejado: '))
n_iter = (math.log(abs(b-a)) - math.log(e))/math.log(2)
n_iter = int(n_iter)+1
print(f'Serão necessárias no mínimo {n_iter} iterações')

for i in range(1, n_iter+1):
    print(f'------------ ITERAÇÃO {i} ------------ \n')
    m = abs((a+b)/2)

    a_y = eval(func, a)
    m_y = eval(func, m)
    b_y = eval(func, b)

    print(f'f({a}) = {a_y}')
    print(f'f({m}) = {m_y}')
    print(f'f({b}) = {b_y}')

    if m_y*a_y < 0:
        print(f'f({m}) * f({a}) < 0')
        b = m;
        print(f'Novo intervalo: [{a}; {b}]')

    elif m_y*b_y < 0:
        print(f'f({m}) * f({b}) < 0')
        a = m;
        print(f'Novo intervalo: [{a}; {b}]')

 
        

x = abs((a+b)/2)
print('\n------------ RESULTADO ------------')
print(f'x = {x}\nf({x}) = {eval(func, x)}')

    
