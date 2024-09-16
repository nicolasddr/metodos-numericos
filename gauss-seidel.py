

n = int(input('Digite o número de linhas e colunas da matiriz:\n'))
matrizA = []
matrizB = []
x = []
num_iter = 0

# Lê a Matriz A e a Matriz B
for i in range(0,n):
    linha = []
    print(f"Digite os elementos da linha {i+1}, separados por espaço:")
    elementos = input().split() # Lê e converte os elementos em uma lista de strings

    # Adiciona elementos na linha e converte para float
    for elem in elementos:
       linha.append(float(elem)) 

    # Adiciona elementos na matriz
    matrizA.append(linha)

    # Lê o 'b' e adiciona a Matriz B
    b = float(input('Digite o elemento b da linha:'))
    matrizB.append(b)

# Lê a aproximação inicial
print(f"Digite as aproximações separadas por espaço:")
aproximacoes = input().split() # Lê e converte as aproximações em uma lista de strings

# Adiciona as aproximações na linha e converte para float
for apr in aproximacoes:
    x.append(float(apr))

# Imprime a Matriz
print(f'Matriz A e Matriz B')
for i in range(0,n):
    for j in range(0,n):
        print(f'{matrizA[i][j]}x{j+1}', end=" ")
    print(f'= {matrizB[i]}')

erroDesejado = float(input('Digite o erro desejado(inferior a):\n'))
e = False   # Se o erro está abaixo do erro desejado, então é True. Se o erro for maior, é False.

# Iterações
while(e != True):
    num_iter += 1
    x_anterior = x.copy() # Copia e salva a aproximação anterior para calcular o erro
    for k in range(0,n):
        somatorio = matrizB[k] # somatorio recebe o 'b' da linha k
        for l in range(0,n): # Itera os elementos da linha k para fazer a subtração
            if (k!=l): # Não inclui a diagonal principal na soma
                somatorio -= matrizA[k][l] * x[l] # somatorio = somatorio - a * x(k)
        # Nova aproximação
        x[k] = somatorio/matrizA[k][k] # Depois que a linha termina, ocorre a divisão pelo elemento da diagonal

    # Calculo do erro
    dif_maxima = 0.0 # O valor máximo da diferença do 'xNovo - xAntigo' em módulo
    x_maximo = 0.0 # O valor máximo da matriz do x Novo

    for k in range(0,n):
        # Encontra o valo máximo da diferença do x novo e antigo
        val = abs(x[k] - x_anterior[k])
        if(val > dif_maxima):
            dif_maxima = val

        # Encontra o maior valor do novo x
        if(abs(x[k]) > x_maximo):
            x_maximo = abs(x[k])

    # Se a diferença é diferente de 0, calcula o erro
    if(dif_maxima != 0):
        erroAtual = dif_maxima/x_maximo
    else:
        erroAtual = float('inf')

    # Se o erro for menor que o erro desejado, então 'e' recebe 'True' e as iterações param
    if(erroAtual < erroDesejado): 
        e = True

# Imprime a aproximação final, o número de iterações e o erro
print(f'{num_iter} iterações. Erro final: {erroAtual}')
print(x)