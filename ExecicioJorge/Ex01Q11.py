'''
6) Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;

'''
print ('Avaliação de triangulo')

lado1 = int(input('Digite o Primeira Lado do triangulo: '))
lado2 = int(input('Digite o Segundo Lado do triangulo: '))
lado3 = int(input('Digite o Terceiro Lado do triangulo: '))

print('Analiando')

if (lado1 == lado2 == lado3):
    print('Triângulo Equilátero')
elif (lado1 == lado2) or (lado2 == lado3) or (lado1 == lado3):
    print ('Triângulo Isósceles')
elif: (lado1 != lado2 != lado3)
        print('Triângulo Escaleno')
else:

