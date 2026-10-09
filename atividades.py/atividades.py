# 1 - Crie um programa que receba um nome e um curso do usuário e exiba a seguinte frase: "Olá, meu nome é _______ e faço o curso ____________". Use o printf
# 2 - Crie um programa que receba dois números do usuário. Faça as seguintes operações matemáticas: soma, subtração, multiplicação, divisão, exponenciação, resto da divisão e divisão inteira.
# 3 - Faça um programa que tenha uma variável fixa com um número. Depois, uma variável para receber um 'chute' do usuário. Na sequência, faça um condição para saber se o usuário acertou ou errou o número.
# 4 - Aprimore o exercício anterior utilando mais condições. Uma para avisar o usuári que ele digitou um número maior que o número fixo e outra para informar que ele digitou um número menor.

# nome = input('Digite o seu nome: ')
# curso = input('Digite o seu curso:')
# print(f'Olá, meu nome é {nome} e faço o curso {curso}')


# n1 = int(input('Digite um numero '))
# n2 = int(input('Digite outro numero '))
# adicao = n1 + n2
# subtrcao = n1 - n2
# mult = n1 * n2
# div = n1 / n2
# expo = n1 ** n2
# restoDiv = n1 % n2
# divInteira = n1 // n2

# print(adicao)
# print(subtrcao)
# print(mult)
# print(div)
# print(expo)
# print(restoDiv)
# print(divInteira)


# n1 = 5
# chute = int(input('escreva um numero '))

# if n1 == chute:
#     print('voce acertou ')
# else:
#     print('voce errou ')   
# 
numerosecreto = 46
tentativas = 5
while tentativas > 0:
    chute = int(input('Digite um numero: '))
    print(f'você digitou {chute}')
    if  chute < numerosecreto:
        print('Você errou,o numero secreto é maior')
    elif chute > numerosecreto:
        print('Você errou,o numero secreto é menor')
    else:
        print('Acertou') 
        break
    tentativas -= 1
else:
    print(f'Suas tentativas acabaram. O numero secreto era {numerosecreto}')       