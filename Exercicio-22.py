# 22. Criar uma rotina de entrada que aceite somente um valor positivo.
v1 = float(input("Digite um numero positivo: "))

while (v1 <= 0):
    print("Numero não permitido")
    v1 = float(input("Digite um numero positivo: "))

print("Numero permitido. Obrigado!!")

