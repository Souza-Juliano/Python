#36. Armazenar vinte valores na memória. Após a digitação,
#   entrar com uma constante multiplicativa que deverá multiplicar
#   cada um dos valores do vetor e armazenar o resultado em outro 
#   vetor, porém em posições equivalentes. Exibir os vetores na tela.
numeros1 = []
numeros2 = []
r = 2
for i in range(0, 20, 1):
    x = int(input('Digite um numero: '))
    numeros1.append(x)
 
print('Os numeros que você digitou  multiplicado por 2 é : ')
 
for i in range(0, 20, 1):
    n = r * numeros1[i]
    numeros2.append(n)
    print(f"{numeros2[i]}")

