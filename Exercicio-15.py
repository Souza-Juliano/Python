# 15. Entrar com o peso e a altura de uma determinada pessoa. 
# Após a digitação, exibir se esta pessoa está ou não com seu 
# peso ideal. Fórmula: peso/altura².

v1 = float(input("Digite a altura: "))
v2 = float(input("Digite o valor do peso:  "))

R = (v2/(v1*v1))

if R < 20:
    print("Abaixo do peso!")
elif R < 25:
    print("Peso ideal!")
else: 
     print("Acima do peso!")  


    

      

 

