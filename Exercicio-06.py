#6. Entrar via teclado com o valor da cotação do dólar
#  e uma certa quantidade de dólares. Calcular e exibir 
# o valor correspondente em Reais (R$).


v1 = float(input("Digite o valor da cotação do dolar: "))
v2 = float(input("Digite de uma quantia em dolar: "))

m = v1 * v2

print(f" Valor da quantia em Reais: {m:.2f} ")
