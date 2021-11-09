#35. Armazenar vinte valores em um vetor. Após a digitação, entrar com uma constante
#  multiplicativa que deverá multiplicar cada um dos valores do vetor e armazenar o 
# resultado no próprio vetor, na respectiva posição.
numeros = []
r = 2
for i in range(0, 21, 1):
    x = int(input('Digite um numero: '))
    numeros.append(x)
 
print('Os numeros que você digitou  multiplicado por 2 é : ')
 
for i in range(0, 21, 1):
    numeros[i] = r * numeros[i]
    print(f"{numeros[i]}")






    
