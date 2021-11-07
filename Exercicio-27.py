#27. Entrar via teclado com um valor (X) qualquer. Travar a digitação, no sentido de aceitar somente valores positivos.
#  Solicitar o intervalo que o programa que deverá calcular a tabuada do valor digitado, sendo que o segundo valor (B),
#  deverá ser maior que o primeiro (A), caso contrário, digitar novamente somente o segundo. Após a validação dos dados,
#  exibir a tabuada do valor digitado, no intervalo decrescente, ou seja, a tabuada de X no intervalo de B para A.

print('Tabuada com WHILE')
 
num = int(input("Digite um numero para obter a tabuada: "))
 
while(num <= 0):
    print("Não pode numero negativo!")
    num = int(input("Digite um outro numero para obter a tabuada: "))
 
i = int(input("Digite o intervalo da tabuada:(inicio) "))
f =int(input("Digite o intervalo da tabuada:(Termíno) "))
 
while(f < i):
    print("O primeiro numero é maior que o segundo")
    f = int(input("Digite um numero maior que o primeiro: "))

f = f + 1
while (i < f):
    r = num * i
    print(f'{num} X {i} = {r}')
    i = i + 1