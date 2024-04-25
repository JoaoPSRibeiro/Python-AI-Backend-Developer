# print('-=' * 30)
# print(f'Bem Vindo ao Banco JPS'.center(60,' '))
# print('-=' * 30)
# print()
# print("""Serviços:
#       [ 1 ] Extrato 
#       [ 2 ] Depósito
#       [ 3 ] Saque
#       [ 4 ] Sair""")
# print('-=' * 30)
# print()
# menu = int(input('Escolha uma opção: '))
# saldo = 1500
# extrato = list()
# LIMITE_DE_SAQUE = 0
# saque = 0


# while True:
#     if menu == 1:
#         print(f'Saldo atual: R$ {saldo:.2f}')
#         break
#     elif menu == 2:
#         valor = int(input('Valor a ser Depositado: '))
#         saldo += valor
#         extrato.append(saldo)
#         print(extrato)
#         break
#     elif menu == 3:
#         saque = int(input('Qual valor deseja sacar? R$ '))
#         if saque > 500:
#             print('Valor excede limite por transação.')
#         elif saque <= 500:
#             print(f'Sacando o valor de R$ {saque:.2f}.')
#             LIMITE_DE_SAQUE += 1
#             extrato.append(saque)
#             if LIMITE_DE_SAQUE == 3:
#                 print("Limite de saque diário atingido.")
#         pass
#     elif menu == 4:
#         break
#     else:
#         print("Valor inválido, comece novamente.")

print('-=' * 30)
print(f'Bem Vindo ao Banco JPS'.center(60,' '))
print('-=' * 30)
menu = """Serviços:
      [ 1 ] Depositar
      [ 2 ] Sacar
      [ 3 ] Extrato
      [ 4 ] Sair 
      => """
print()
saldo = 0 
numero_saques = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input('Informe o valor do depósito: R$ '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Operação falhou! O valor informado é inválido.')
    elif opcao == 2:
        valor = float(input('Informe o valor do saque: R$ '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print('Operação não realizada, saldo insuficiente.')
        elif excedeu_limite:
            print('Operação não realizada, valor de saque execede valor limite.')
        elif excedeu_saques:
            print('Operação não realizada, número de saques excedidos.')
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print('Operação não realizada, valor informado inválido.')
    elif opcao == 3:
        print('-=' * 30)
        print('Extrato'.center(60, ' '))
        print('Não foram realizadas transações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('-=' * 30)
    elif opcao == 4:
        break
    else:
        print('Operação Inválida, por favor selecione novamente a opção desejada!')
