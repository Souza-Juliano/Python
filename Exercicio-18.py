# 18. Entrar com o peso, o sexo e a altura de uma determinada pessoa. 
# Após a digitação, exibir se esta pessoa está ou não com seu peso ideal.
#  Fórmula: peso/altura².


v1 = float(input("Digite a altura: "))
v2 = float(input("Digite o valor do peso:  "))
# o input por padrão já é uma string
v3 = (input("Digite o Sexo, F se feminino e M de masculino "))

R = (v2/(v1*v1))

if v3 == 'm':
    if R < 20:
        print("Abaixo do peso!")
    elif R < 25:
        print("Peso ideal!")
    else:
        print("Acima do peso!")  

elif v3 == 'f':
    if R < 19:
        print("Abaixo do peso!")
    elif R < 24:
        print("Peso ideal!")
    else:
        print("Acima do peso!") 


    
    

    

     
