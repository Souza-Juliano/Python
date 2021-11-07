# 13. Calcular e exibir a área de um retângulo, a partir dos valores da base
#  e altura que serão digitados. Se a área for maior que 100, exibir a mensagem
#  “Terreno grande”, caso contrário, exibir a mensagem “Terreno pequeno”.

v1 = float (input("Digite o valor da base do retangulo:  "))
v2 = float (input("Digite o valor da altura do retangulo:  "))

m = v1 * v2
print(f" A área do retangulo é de: {m:.2f} ")

if m >= 100:
   print(f" Terreno grande ") 
else:
    print(f"Terreno pequeno") 

