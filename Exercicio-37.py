#37. Armazenar um máximo de 20 valores em um vetor. A quantidade de valores a serem 
# armazenados será escolhida pelo usuário. Enviar mensagem de erro, caso a quantidade 
# de valores escolhida esteja fora da faixa possível e solicitar a quantidade novamente.
#  Após a digitação dos valores, criar uma rotina de consulta, onde o usuário digita um
#  número e o programa exibe em qual posição do vetor este número está localizado. Se o 
# número não for encontrado, enviar mensagem “Valor não encontrado!”. Perguntar ao usuário
#  se deseja ou não fazer uma nova consulta, consistir a resposta e encerrar o programa em 
# caso negativo.
numeros1 =  []
num = 0
esc = 0
Let = 'S' 
p = 1

num = int(input("Digite a quantidade de numeros que serão armazenados(A quantidade tem que ser maior que 0 e menor que 20) "))
if (num >= 20 or num <=0 ):
    num = int(input("Quantidade invalida. Digite a quantidade de numeros que serão armazenados (A quantidade tem que ser maior que 0 e menor que 20) "))

for i in range(0, num, 1):
    x = int(input('Digite um numero: '))
    numeros1.append(x)


while (Let == 'S'):
     esc = int(input("Digite um dos numeros para saber a posição dele: "))
     for i in range(1, num, 1 ):
        if (esc == numeros1[i]):
            p = i 
            print(f"A posição do numero é: {p}")
            let=  'N'
            break
            
        else:
             print("Numero não encontrado.")
             continue
             print(i)


     Let = (input(" Deseja procurar por outro numero: (S para sim e N para não): "))

        
    








