import sympy as sp

funcao = input('Digite a função:\n')
x = sp.symbols('x')
funcao = sp.sympify(funcao) 

pontoInicial = float(input('Digite o ponto inicial:\n'))
erroDesejado = float(input('Digite o erro desejado(inferior a):\n'))
e = False # Se o erro está abaixo do erro desejado

pontoAtual = pontoInicial

derivada = sp.diff(funcao, x)

while(e == False):
    valor_derivada = derivada.subs(x, pontoAtual).evalf()
    valor_funcao = funcao.subs(x, pontoAtual).evalf()

    novoPonto = pontoAtual - ((valor_funcao)/(valor_derivada))
    
    # Calculo do erro
    erroAtual = abs((novoPonto - pontoAtual)/novoPonto)
    if(erroAtual < erroDesejado):
        e = True

    pontoAtual = novoPonto

print(f'ponto atual: {pontoAtual} e erro de {erroAtual}')
    

