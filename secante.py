import sympy as sp

# Função
funcao = input('Digite a função:\n') # Recebe a função do usuário
x = sp.symbols('x') # Define a variável da função
funcao = sp.sympify(funcao) # Converte função para o formato da biblioteca sympy

# Pontos Iniciais e Erro
pontoInicial = float(input('Digite o primeiro ponto inicial:\n'))
pontoInicial2 = float(input('Digite o segundo ponto inicial:\n'))
erroDesejado = float(input('Digite o erro desejado(inferior a): '))
e = False  # Se o erro está abaixo do erro desejado, então é True. Se o erro for maior, é False.

pontoAnterior = pontoInicial
pontoAtual = pontoInicial2

derivada = sp.diff(funcao, x) # sp.diff -> Deriva a função na variável x

# Iterações
while(e == False):
    valor_derivada = derivada.subs(x, pontoAtual)  # Calcula o valor da derivada no ponto atual 
    valor_funcao = funcao.subs(x, pontoAtual) # Calcula o valor da função no ponto atual 

    # Fórmula do Método da Secante
    novoPonto = ((pontoAnterior*funcao.subs(x, pontoAtual)) - (pontoAtual*funcao.subs(x, pontoAnterior)))/(funcao.subs(x, pontoAtual) - funcao.subs(x, pontoAnterior))

    # Calculo do erro
    erroAtual = abs((novoPonto - pontoAtual)/novoPonto)
    if(erroAtual < erroDesejado):  # Se o erro for menor que o erro desejado, então 'e' recebe 'True' e as iterações param
        e = True

    pontoAnterior = pontoAtual
    pontoAtual = novoPonto

print(f'ponto atual: {round(pontoAtual, 4)} e erro de {round(erroAtual, 4)}')
    

