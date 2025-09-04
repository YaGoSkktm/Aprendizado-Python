from emoji import emojize
print(emojize('Olá, Essa é uma calculadora IMC feita em python :snake:', language='alias'))
peso = float(input('Pode me dizer seu peso? '))
altura = float(input('E qual é a sua altura? '))
imc = peso / altura**2
print('Seu IMC é {:.1f}'.format(imc))
if imc <18.5:
    print('Você está abaixo do peso.')
else:
    if imc <= 24.9:
        print('Você está em um peso ideal.')
    else:
        if imc <= 29.9:
            print('Você está com sobrepeso.')
        else:
            print('Você está com obesidade.')
