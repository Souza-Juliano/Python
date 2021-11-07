# 16. A partir de três valores que serão digitados, verificar se formam ou não um triângulo. Em caso positivo,
#  exibir sua classificação: “Isósceles, escaleno ou eqüilátero”. Um triângulo escaleno possui todos os lados 
# diferentes, o isósceles, dois lados iguais e o eqüilátero, todos os lados iguais. Para existir triângulo é 
# necessário que a soma de dois lados quaisquer seja maior que o outro, isto, para os três lados.

v1 = float(input("Digite o valor de um lado do triangulo:  "))
v2 = float(input("Digite o valor de outro lado do triangulo:  "))
v3 = float(input("Digite o valor de outro lado do triangulo:  "))

m = v1 + v2
if m < v3:
    print("não é um triâgulo: ")
elif v1 == v2 and v1 == v3:
    print("Triangulo equilatero")
elif v1 == v2 or v1 == v3 or v2 ==v3:
    print("triagulo isósceles")
else:
    print("escaleno")



