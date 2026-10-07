while True:
    nome = input('Qual seu nome? ')
    idade = input('Quantos anos você tem? ')
    salario = input('Qual seu salário? ')
    estado_civil = input('Qual seu estado civil? [D]ivorciado, [S]olteiro, [C]asado ou [V]iúvo?').lower()
   
    idade_float = 0
    salario_float = 0
    idade_salario_ok = None
    
    try:
        idade_float=float(idade)
        salario_float=float(salario)
        idade_salario_ok= True
    except:
        idade_salario_ok = None
        
    if idade_salario_ok is None:
        print('Informações que pedem números devem ser escritas em números!')
        
    if len(nome) <= 3:
        print('Seu nome deve ter pelo mneos 3 caracteres!')
        continue
     
    idade_invalida = idade_float < 0 or idade_float > 150
     
    if idade_invalida:
        print('Como uma idade dessa é possível? Ta maluco?')
        continue
    
    if salario_float <= 0:
        print('Pobres não passarão! Salário zerado num pode!')
        continue
    
    estado_civil_valido = ('d', 's', 'v', 'c')
    
    if estado_civil not in estado_civil_valido:
        print('Escolha entre as opções ofertadas de estado civil!')
        continue
    
    print('Obrigado por sua colaboração!')
    break