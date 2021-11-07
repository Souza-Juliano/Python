#20. Uma escola com cursos em regime semestral, realiza duas avaliações 
# durante o semestre e calcula a média do aluno, da seguinte maneira:
#MEDIA = (P1 + 2P2) / 3
#Fazer um programa para entrar via teclado com os valores das notas (P1 e P2)
#  e calcular a média. Exibir a situação final do aluno (“Aprovado ou Reprovado”),
#  sabendo que a média de aprovação é igual a cinco.


p1 = float(input("Digite o valor da nota P1: "))
p2 = float(input("Digite o valor da nota P2: "))

M = (p1 +(2*p2))/3

if M >= 5:
    print("Aprovado")
else:
    print("Reprovado")

