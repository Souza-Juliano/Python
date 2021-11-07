# 19. A partir dos valores da aceleração (a em m/s2), da velocidade inicial
# (v0 em m/s) e do tempo de percurso(t em s). Calcular e exibir a velocidade 
# final de automóvel em km/h. Exibir mensagem de acordo com a tabela:
# Fórmula para o cálculo da velocidade em m/s: V = v0 + a. t

v0 = float(input("Digite o valor da velocidade em metros por segundo:  "))
a = float(input("Dgite o valor da aceleração em metros por segundo ao quadrado:  "))
t = float (input("Digite o valor do tempo em segundos:  "))

V = v0 + (a*t)

if   V <= 40:
    print("Veiculo muito lento")
elif V<=60:
    print("Veiculo permitida") 
elif V<=80:
    print("Veiculo rápido")
else:
    print("Veiculo muito rápido")