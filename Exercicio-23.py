#23. Entrar com dois valores via teclado, onde o segundo deverá ser 
# maior que o primeiro. Caso contrário solicitar novamente apenas o segundo valor.
v1 = float(input("Digite um numero : "))
v2 = float(input("Digite um  numero maior que o anterior : "))

while(v1>=v2):
    print("O primeiro numero é maior que o segundo")
    v2 = float(input("Digite um numero maior que o primeiro: "))

print("O segundo numero é maior que o primeiro, Obrigado")





  