from emoji import emojize
print(emojize('Olá, esse é um conversor de tempo feito em python! :snake:', language = 'alias'))
tempo = str(input('faça uma escolha para decidir qual periodo você irá converter, dias, horas, minutos ou segundos: '))

if tempo == 'dias' or 'hora':
    dias = int(input('Qual número em dias deseja converter? '))
    horasD = dias * 24
    minutosD = dias * 1440
    segundosD = dias * 86400
    escolhaD = str(input('Deseja converter para horas, minutos ou segundos? ')).strip().lower()
    if escolhaD == 'horas' or 'hora':
        print('{} dia(s) convertido para horas, dá um total de {} horas'.format(dias, horasD))
    if escolhaD == 'minutos' or 'minuto':
         print('{} dia(s) convertidos para minutos, da um total de {} minutos'.format(dias, minutosD))
    if escolhaD == 'segundos' or 'segundo':
        print('{} dia(s) convertidos para segundos, da um total de {} segundos'.format(dias, segundosD))
    if escolhaD != 'horas' or 'hora' and escolhaD != 'minutos' or 'minuto' and escolhaD != 'segundos' or 'segundo':
        print('Erro: por favor faça uma escolha valida.')

if tempo == 'horas' or 'hora':
    horas = int(input('Qual número em horas deseja converter? '))
    diasH = horas / 24
    minutosH = horas * 60
    segundosH = horas * 3600
    escolhaH = str(input('Deseja converter para dias, minutos ou segundos? ')).strip().lower()
    if escolhaH == 'dias' or 'dia':
        print('{} hora(s) convertidos em dias, dá um total de {:.0f} dias'.format(horas, diasH))
    if escolhaH == 'minutos' or 'minuto':
        print('{} hora(s) convertido em minutos, dá um total de {:.0f} minutos'.format(horas, minutosH))
    if escolhaH == 'segundos' or 'segundo':
        print('{} hora(s) convertidos em segundos, dá um total de {:.0f} segundos'.format(horas, segundosH))
    if escolhaH != 'dias ' or 'dia' and escolhaH != 'minutos'or 'minuto' and escolhaH != 'segundos' or 'segundo':
        print('Erro: por favor faça uma escolha valida.')

if tempo == 'minutos' or 'minuto':
    minutos = int(input('Qual número em minutos deseja converter? '))
    diasM = minutos / 1440
    horasM = minutos / 60
    segundosM = minutos * 60
    escolhaM = str(input('Deseja converter para dias, horas ou segundos? ')).strip().lower()
    if escolhaM == 'dias' or 'dia':
        print('{} minutos convertidos em dias, dá um total de {:.0f) dias'.format(minutos, diasM))
    if escolhaM == 'horas' or 'hora':
        print('{} minutos convertidos em horas, dá um total de de {} horas'.format(minutos, horasM))
    if escolhaM == 'segundos' or 'segundo':
        print('{} minuto(s convertidos em segundos, dá um total de {} segundos'.format(minutos, segundosM))
    if escolhaM != 'dias' or 'dia' and escolhaM != 'horas' or 'hora' and escolhaM != 'segundos' or 'segundo':
        print('Erro: por favor faça uma escolha valida.')

if tempo == 'segundos' or 'segundo':
    segundos = int(input('Qual número em segundos deseja converter? '))
    minutosS = segundos / 60
    horasS = segundos / 3600
    diasS = segundos / 86400
    escolhaS = str(input('Deseja converter para dias, horas ou minutos? ')).strip().lower()
    if escolhaS == 'dias' or 'dia':
        print('{} segundos convertidos em dias, dá um total de {} dias'.format(segundos, diasS))
    if escolhaS == 'horas' or 'hora':
        print('{} segundos convertidos em horas, dá um total de {} horas'.format(segundos, horasS))
    if escolhaS == 'minutos' or 'minuto':
        print('{} segundos convertidos em minutos, dá um total de {} minutos'.format(segundos, minutosS))
    if escolhaS != 'dias' or 'dia' and escolhaS != 'horas' or 'hora' and escolhaS != 'minutos' or 'minuto':
        print('Erro: por favor faça uma escolha valida.')