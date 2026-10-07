#Supondo que a população de um país A seja da ordem de 80_000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200_000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

# País A = 80mil habitantes com crescimentode 3%
# País B = 200mil habitantes com crescimento de 1.5% 

pais_a = 80000
pais_b = 200000
ano= 0

while pais_a < pais_b:
    crescimento_a = 0.3 * pais_a
    crescimento_b = 0.15 * pais_b
    pais_a += crescimento_a
    pais_b += crescimento_b
    ano += 1

print(f'Levou {ano} anos para que o país A passasse o país B')