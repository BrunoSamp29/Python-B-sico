
cliente1 = 'Antonio Nunes'
cliente2 = 'Fabricio Cordeiro Gomes'
cliente = input('Qual cliente você quer consultar hoje?:  ')

if int(cliente) == 1:
    print(f'Seu cliente é {cliente1}')
    vara = '27ª vara federal'
    processo1= '0008137.412025'
    cpf= '30036267368'
    senha_inss = 'Arroz101#'
    print(f'Senha ISS: {senha_inss} \nCPF: {cpf}')

    resposta = input('O benefício dele ja está ativado? (Sim ou não): ')

    if resposta == 'sim':
        print('Avisar para o cliente')
    elif resposta == 'não':
        print(f'Processo: {processo1}')
        print('Ligar para a vara cobrando a implantação do benefício, alegando estar desde maio esperando a lideração, os honorários ja foram liberados e ainda nada')

elif int(cliente) == 2:
    print(f'Seu cliente é {cliente2}')
    vara = '27ª vara federal'
    processo2: 0001353.14202611
    cpf= 91094763349
    senha_inss = 'Arroz101#'
    print(f'{senha_inss} \n {cpf}')
    resposta = input('O benefício dele ja está ativado? (Sim ou não)' )

    if resposta == 'sim':
        print('Avisar para o cliente')
    elif resposta == 'não':
        print(f'Processo: {processo2}')
        print('Ligar para a vara cobrando a implantação do benefício, alegando estar desde maio esperando a lideração, os honorários ja foram liberados e ainda nada')
        