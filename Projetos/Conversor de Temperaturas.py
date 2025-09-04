from emoji import emojize
print(emojize('Olá, isto é um conversor de temperatura com escalas Kelvin, Celsius e Fahrenheit \nfeito em python :snake: ', language = 'alias'))
k = 'Kelvin'
c = 'Celsius'
f = 'Fahrenheit'
escala = str(input('Qual escala deseja converter? ')).strip().lower()
if escala == 'kelvin':
    print('A escala Kelvin só aceita valores de 0 (zero absoluto) para cima.')
    temperaturaK = float(input('Você escolheu {}. Por favor, digite a temperatura: '.format(k)))
    if temperaturaK < 0:
        print('Erro: Kelvin não pode ser menor que 0, esse é o zero absoluto.')
    else:
        convK = str(input('Deseja converter para Celsius ou Fahrenheit? ')).strip().lower()
        if convK == 'celsius':
            resultadoC = temperaturaK - 273.15
            print('O resultado da conversão deu {:.2f}°C'.format(resultadoC))
        else:
            if convK == 'fahrenheit':
                resultadoF = (temperaturaK - 273.15) * 9 / 5 + 32
                print('O resultado da conversão deu {:.2f}°F'.format(resultadoF))
            else:
                print('Por favor, Digite uma escala valida')
if escala == 'celsius':
    print('A escala Celsius só aceita valores de -273.15 (zero absoluto) pra cima.')
    temperaturaC = float(input('Você escolheu {}. Por favor, digite a temperatura: '.format(c)))
    if temperaturaC < -273.15:
        print('Erro: Celsius não pode ser menor que -273.15, esse é o zero absoluto.')
    else:
        convC = str(input('Deseja converter para Kelvin ou Fahrenheit? ')).strip().lower()
        if convC == 'fahrenheit':
            resultadoF = (temperaturaC * 9 / 5) + 32
            print('O resultado da sua conversão deu {:.2f}°F'.format(resultadoF))
        else:
            if convC == 'kelvin':
                resultadoK = temperaturaC + 273.15
                print('O resultado da conversão deu {:.2f}K'.format(resultadoK))
            else:
                print('Por favor, Digite uma escala valida')
if escala == 'fahrenheit':
    print('A escala Fahrenheit, aceita apenas valores de -459.67 pra cima, esse é o zero absoluto.')
    temperaturaF = float(input('Você escolheu {}. por favor, digite a temperatura: '.format(f)))
    if temperaturaF < -459.67:
        print('Erro: Fahrenheit não pode ser menor que -459.67, afinal este é o zero absoluto.')
    else:
        convF = str(input('Deseja converter para Celsius ou Kelvin? ')).strip().lower()
        if convF == 'celsius':
            resultadoC = (temperaturaF - 32) * 5/9
            print('O resultado da conversão deu {:.2f}°C'.format(resultadoC))
        else:
            if convF == 'kelvin':
                resultadoK = (temperaturaF - 32) * 5/9 + 273.15
                print('O resultado da conversão deu {:.2f}K'.format(resultadoK))
            else:
                print('Por favor, Digite uma escala valida')
else:
    print('Por favor, Digite uma escala valida')