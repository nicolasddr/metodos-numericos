matrixA = [[5.0, 1.0, 1.0], [3.0, 4.0, 1.0], [3.0, 3.0, 6.0]]
matrixB = [5.0, 6.0, 0.0]
n = 3
x = [0.0, 0.0, 0.0]
e = False

erroDesejado = float(input('Digite o erro desejado(inferior a):\n'))


for i in range(0,n):
    for j in range(0,n):
        print(f'{matrixA[i][j]}x{j+1}', end=" ")
    print(f'= {matrixB[i]}')

while(e != True):
    x_anterior = x.copy()
    for k in range(0,n):
        soma_val = matrixB[k]
        for l in range(0,n):
            if (k!=l):
                soma_val -= matrixA[k][l] * x[l]
        x[k] = soma_val/matrixA[k][k]

    # Calculo do erro
    max_val = 0.0
    max_x = 0.0

    for e in range(0,n):
        val = abs(x[k] - x_anterior[k])
        if(val > max_val):
            max_val = val

        if(abs(x[k]) > max_x):
            max_x = abs(x[k])

    if(max_val != 0):
        erroAtual = max_val/max_x
    else:
        erroAtual = float('inf')

    if(erroAtual < erroDesejado):
        e = True

print(x)