nome = input('Qual seu nome? ')
idade = input('DIga sua idade ')

if nome and idade:
    print(f'O seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print ('Tem espaço no seu nome!')
    else:
        print('Não tem espaço no seu nome!')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A últma letra do seu nome é {nome[-1]}')
    print(f'A primeira letra do seu nome é {nome[0]}')
else:
    print('Você precisa digitar algo!')

