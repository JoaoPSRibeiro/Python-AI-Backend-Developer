idade = input('Informe a sua idade: ')

nome = "João Paulo"
sobrenome = "Santos"

print(nome, sobrenome)
print(nome, sobrenome, end=' ...\n') #exibirá os 3 pontinhos no final e pulará uma linha
print(nome, sobrenome, sep="_") #entrará um _ entre nome e sobrenome
print(f'Seu nome é {nome}, seu Sobrenome é {sobrenome} e sua idade é {idade}', end='!!!')