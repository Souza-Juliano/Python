#32. Calcular e exibir a soma dos “N” primeiros valores da sequência abaixo. 
# O valor “N” será digitado, deverá ser positivo, mas menor que cem. Caso o 
# valor não satisfaça a restrição, enviar mensagem de erro e solicitar o valor
#  novamente.A seqüência: 2, 5, 10, 17, 26, ....

a = 1 
b = 1 
c = 0 
num1 = 1
num = int(input("Digitar quantos elementos serão somados (o numero deverá ser maior que zero e menor que cem). "))
while (num<=0 or num>=100):
    num = int(input("Numero invalido, digite novamente (o numero deverá ser maior que zero e menor que cem). "))

while (num1<=num):
    a = a + b 
    b = b + 2 
    c = c + a 
    num1 = num1 + 1 

print(f"A soma dos numeros é: {c} " ) 


