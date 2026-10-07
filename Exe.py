while True:
    nota = input('De uma nota: ')
    valor_valido = None
    nota_float = 0
    
    try:
        nota_float= float(nota)
        numero_valido= True
    except:
        numero_valido = None
        
    if numero_valido is None:
        print('Esse valor não é válido')
        continue
        
    nota_numericamente_aceitavel = nota_float >= 0 and nota_float <=10

    if not nota_numericamente_aceitavel:
        print('Digite um valor entre 0 e 10')
        continue
        
    print (f'Você nos deu nota {nota_float}, muito obrigado por sua opinião! ')

    sair = input('Você quer sair? sim [s]').lower().startswith('s')

    if sair is True:
        break