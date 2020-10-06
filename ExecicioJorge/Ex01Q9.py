'''
9) Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
'''
print('Calculos')

#1º passo: receber os numeros
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

#2º passo: solicitar operação
operacao = input('Digite a operação: ')

#3º passo: efetuar operação
if(operacao == '+'):
    resultado = a + b
elif(operacao == '-'):
    resultado = a - b
elif(operacao == '*'):
    resultado = a * b
elif(operacao == '/'):
    resultado = a / b
else:
    printe('Operação escolhida não existe!!!')

#4º passo: definir se o resultado é par ou impar, positivo ou negativo
strpositivo = 'Negativo'
if(resultado >= 0): strpositivo = 'Positivo'

strPar = 'Impar'
if((resultado%2)==0): strPar = 'Par'

#5º passo: escrevero resultado na tela
print('O resultado da operfação foi ' + str(resultado) + ', que é ' + strpositivo + ' e ' + strPar)