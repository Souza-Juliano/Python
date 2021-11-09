#29. Exibir a soma dos números inteiros positivos do intervalo de um a cem.

r = 0 
num = 1

while(num<=100):
    r = num + r 
    num = 1 + num 
    
print(f"A soma dos numeros é: {r} " ) 