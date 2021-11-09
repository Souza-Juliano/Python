#33. Armazenar dez números na memória do computador. Exibir os valores na ordem inversa à da digitação.
numeros = []

for i in range(0, 11, 1):
    x = int(input('Digite um numero: '))
    numeros.append(x)
 
print('Os numeros que você digitou foram: ')
 
# Exibir de forma crescente
for i in range(10, -1, -1):
    print(numeros[i])