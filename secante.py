import sympy as sp

funcao = input('Digite a função:\n')
x = sp.symbols('x')
funcao = sp.sympify(funcao) 

pontoInicial = float(input('Digite o primeiro ponto inicial:\n'))
pontoInicial2 = float(input('Digite o segundo ponto inicial:\n'))
erroDesejado = float(input('Digite o erro desejado(inferior a): '))
e = False # Se o erro está abaixo do erro desejado

pontoAnterior = pontoInicial
pontoAtual = pontoInicial2

derivada = sp.diff(funcao, x)

while(e == False):
    valor_derivada = derivada.subs(x, pontoAtual)
    valor_funcao = funcao.subs(x, pontoAtual)

    novoPonto = ((pontoAnterior*funcao.subs(x, pontoAtual)) - (pontoAtual*funcao.subs(x, pontoAnterior)))/(funcao.subs(x, pontoAtual) - funcao.subs(x, pontoAnterior))

    # Calculo do erro
    erroAtual = abs((novoPonto - pontoAtual)/novoPonto)
    if(erroAtual < erroDesejado):
        e = True

    pontoAnterior = pontoAtual
    pontoAtual = novoPonto

print(f'ponto atual: {round(pontoAtual, 4)} e erro de {round(erroAtual, 4)}')
    

