# 24. Entrar via teclado com o sexo de determinado usuário, 
# aceitar somente “F” ou “M” como respostas válidas.

v1 = (input("Digite seu sexo, F (feminino) ou M (masculino) : "))

while (v1 != 'm' and v1 != 'f') :
    print("Resposta invalida")
    v1 = (input("Digite seu sexo, F (feminino) ou M (masculino) : "))

print("Resposta valida, Obrigado!!")    

