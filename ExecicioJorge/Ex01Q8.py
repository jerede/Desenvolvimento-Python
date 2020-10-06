'''
8) Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá
pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os
demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
print ('Equação')

# 1º Passo: receber a, b, c
a = int(input('Digite o valor de A: ') )
b = int(input('Digite o valor de B: ') )
c = int(input('Digite o valor de C: ') )

# 2º Passo: Testar se a é igual a zero
if(a == 0):
    print('Esta Equação não é do segundo grau')
    quit()

# 3º Passo: Calular o valor de delta == > delta=(b**2)-(4*a*c)
delta =(b ** 2) - (4 * a * c)

# 4º Passo: Testa se Delta menos que zero
#    se Delta menor que zero, avisar a equação nãopossui raizes reais
if (delta < 0):
    print('Delta menor que zero, Equação não possui raizes reais!!!')
    quit()

# 5º Passo: Calular raizes
#    se Deslta = 0 calcular raiz
#    se Delta > 0 calcule as duas raizes
if (delta == 0):
    raiz=(-b) / (2 * a)
    print('Delta =0, logo apenas uma raiz real igual a ' + raiz)
else:
# Calculo raiz quadrada de delta
    raizQuadradaDelta = delta ** (1/2)

#cacular as raizes da equação
    raiz1 = ((-b) + raizQuadradaDelta) / (2 * a)
    raiz2 = ((-b) - raizQuadradaDelta) / (2 * a)
    print('Delta > 0 a euqação possui duas raizes, com valores ' + str(raiz1) + ' e ' + str(raiz2))