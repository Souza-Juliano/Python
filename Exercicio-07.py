#7. Entrar via teclado com o valor de cinco produtos. 
# Após as entradas, digitar um valor referente ao
#  pagamento da somatória destes valores. Calcular
#  e exibir o troco que deverá ser devolvido.

v1 = int(input("Digite o valor do primeiro produto"))
v2 = int(input("Digite o valor do segundo produto "))
v3 = int(input("Digite o valor do terceiro produto "))
v4 = int(input("Digite o valor do quarto produto "))
v5 = int(input("Digite o valor do quinto produto "))

m = v1 + v2 + v3 + v4 + v5 

v6 = int(input("Digite o valor refente ao pagamento "))

n =   v6-m

print(f" O seu troco é de:  {n:.2f} ")

