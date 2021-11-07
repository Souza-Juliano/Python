#5. Entrar via teclado com o valor de uma 
# temperatura em graus Celsius, calcular e
#  exibir sua temperatura equivalente em Fahrenheit.

v1 = int(input("Digite da temperatura em graus celsius °C"))

m = (32 + (v1*1.8))
print(f" A temperatura em Fahrenheit é: {m:.2f} °F")
