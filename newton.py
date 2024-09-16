import sympy as sp

# Função
funcao = input('Digite a função:\n') # Recebe a função do usuário
x = sp.symbols('x') # Define a variável da função
funcao = sp.sympify(funcao) # Converte função para o formato da biblioteca sympy

# Ponto Inicial e Erro
pontoInicial = float(input('Digite o ponto inicial:\n'))
erroDesejado = float(input('Digite o erro desejado(inferior a):\n'))
e = False # Se o erro está abaixo do erro desejado, então é True. Se o erro for maior, é False.

pontoAtual = pontoInicial

derivada = sp.diff(funcao, x) # sp.diff -> Deriva a função na variável x
num_iter = 0

# Iterações
while(e == False):
    num_iter += 1
    
    valor_derivada = derivada.subs(x, pontoAtual).evalf() # Calcula o valor da derivada no ponto atual 
    valor_funcao = funcao.subs(x, pontoAtual).evalf() # Calcula o valor da função no ponto atual

    novoPonto = pontoAtual - ((valor_funcao)/(valor_derivada)) # Fórmula do Método de Newton
    
    # Cálculo do erro
    erroAtual = abs((novoPonto - pontoAtual)/novoPonto)
    if(erroAtual < erroDesejado): # Se o erro for menor que o erro desejado, então 'e' recebe 'True' e as iterações param
        e = True

    pontoAtual = novoPonto

print(f'{num_iter} iterações. Ponto final: {pontoAtual} e erro de {erroAtual}')
    

