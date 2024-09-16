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

num_iter = 0

# Iterações
while(e == False):
    num_iter += 1
    print(num_iter)
    valor_funcao_anterior = funcao.subs(x, pontoAnterior).evalf() # Calcula o valor da função no ponto anterior 
    valor_funcao_atual = funcao.subs(x, pontoAtual).evalf() # Calcula o valor da função no ponto atual 
    print('Passou o valor')


    # Fórmula do Método da Secante
    novoPonto = ((pontoAnterior*valor_funcao_atual) - (pontoAtual*valor_funcao_anterior))/(valor_funcao_atual - valor_funcao_anterior)
    print('Passou a formula')

    # Calculo do erro
    erroAtual = abs((novoPonto - pontoAtual)/novoPonto)
    print('Passou o calculo do erro')
    if(erroAtual < erroDesejado):  # Se o erro for menor que o erro desejado, então 'e' recebe 'True' e as iterações param
        e = True
    print('Passou o if do erro')
    pontoAnterior = pontoAtual
    pontoAtual = novoPonto
    print('Passou tudo')

print(f'{num_iter} iterações. Ponto final: {pontoAtual} e erro de {erroAtual}')

    

