preco = '10'
print(type(preco))

preco = float(preco) 
print(type(preco))

print('=-' * 30)

preco = 10.89
print(preco)

preco = int(preco) #Vai arredondar para baixo, só vai excluir o decimal.
print(preco)

print('=-' * 30)

preco = 20
print(preco)
print(preco / 2) # tranforma int em float
print(preco // 2) # mantém como int, este é o format de divisão EXATA, 

print('=-' * 30)
# para concatenarmos String, é necessário converter números em String

preco = 10.50
idade = 28
print(str(preco))
print(str(idade))

# podemos também, usar F-Strings, para formatar nosso texto, informando que usaremos variáveis, Como?

texto = f'Sua idade é {idade} e o Preço foi {preco}.'
print(texto)

