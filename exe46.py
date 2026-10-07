"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra_secreta = 'Porta'
tentativa = 0
palavra_tentada = ('*****')
tentar = input('Escreva uma letra: ')

for letra in range( 0 , 5, ):
    tentativa += 1

    if tentar not in palavra_secreta:
        print(palavra_tentada)

    
