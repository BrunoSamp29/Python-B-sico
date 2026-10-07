tabuada = int(1)
soma = int(1)

while soma < 11:
    print(f'{tabuada} + {soma}= {tabuada+soma}')
    soma += 1

    if soma == 11:
        print ('')
        tabuada += 1
        soma = 1

        if tabuada == 11:
            break
print('Essa é a tabuada de somar!')

