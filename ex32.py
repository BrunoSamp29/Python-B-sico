'''
num = input('Digite um número: ')

if "." in num:
    print('Digite um número inteiro!')
else:
    num_int=int(num)
    if (num_int % 2 == 0):
        print('É um número par')
    else:
        print('É um número ímpar')
'''
'''
hr = int(input('Quais as horas?'))
bomdia = hr >= 0 and hr <= 11
boatarde = hr > 11 and hr <= 17
boanoite = hr > 17 and hr < 0

if bomdia:
    print('Bom dia!')
elif boatarde:
    print('Boa tarde!')
elif boanoite:
    print('Boa noite')
else: 
    print('Digite um horário válido')
'''

nome = input('Qual seu nome?')
curto = len(nome) <= 4
normal = len(nome) > 4 and len(nome) < 7
longo = len(nome) > 6

if curto:
    print('Seu nome é curto')
elif normal:
    print('Seu nome é normal')
else: 
    print('Seu nome é longo')
