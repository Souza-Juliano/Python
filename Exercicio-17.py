#17. Verificar se três valores quaisquer (A, B, C) que serão digitados formam 
# ou não um triângulo retângulo. Lembre-se que o quadrado da hipotenusa é igual 
# a soma dos quadrados dos catetos.
v1 = float(input("Digite o valor de um dos catetos:  "))
v2 = float(input("Digite o valor do outro cateto:  "))
v3 = float(input("Digite o valor da hipotenusa:  "))

m = (v1*v1) + (v2*v2)
if m == v3*v3:
    print("Valores digitados  correnpondem a um triângulo: ")
else:
    print("Valores digitados não correnpondem a um triângulo: ")
   

