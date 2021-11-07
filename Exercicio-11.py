# 11.  Entrar com dois valores quaisquer. Exibir o maior deles, se existir, caso contrário, enviar mensagem avisando que os números são idênticos.
v1 = float(input("Digite um valor: "))
v2 = float(input("Digite outro valor: "))

if v2 > v1: 
    print("O primeiro valor é o menor")
elif v1 == v2: 
    print("Os numeros são idênticos")
else:
    print("O segundo valor é o menor")     