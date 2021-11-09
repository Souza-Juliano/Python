#31. Exibir os vinte primeiros valores da série de Bergamaschi. A série: 1, 1, 1, 3, 5, 9, 17, ...
a = 1
b = 1 
c = 1
num = 1
while (num<=20):
    d = a + b + c 
    print (f"{a}")
    a = b
    b = c 
    c = d 
    num = num + 1 