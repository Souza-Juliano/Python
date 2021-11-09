#  34. Armazenar dez valores na memória do computador. Após a digitação dos valores,
#  criar uma rotina para ler os valores e achar e exibir o maior deles.

numeros = []
n = 1

for i in range(0, 11, 1):
    x = int(input('Digite um numero: '))
    numeros.append(x)
 
# Exibir de forma crescente
for i in range(0, 11, 1):
    if n <= numeros[i]:
        n = numeros [i]

print(f"o maior numero é:{n}" ) 