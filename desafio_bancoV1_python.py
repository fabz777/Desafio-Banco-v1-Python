menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.0
limite_sacar = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        try:
            valor_deposito = float(input("Digite o valor a ser depositado: "))
        except ValueError:
            print("Digite um número!")
            continue
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Foi depositado R$ {valor_deposito:.2f} na sua conta!")
        else:
            print("Por favor, digite um número positivo e maior que zero.")
        continue

    elif opcao == "s":
        try:
            valor_sacar = float(input("Digite o valor a ser sacado: "))
        except ValueError:
            print("Digite um número!")
            continue
        if valor_sacar > saldo:
            print("Você não tem saldo o suficiente para essa operação!")
        elif valor_sacar > limite_sacar:
            print("Você excedeu o limite de saque!")
        elif numero_saques == LIMITE_SAQUES:
            print("Você excedeu o limite diário de saques!")
        elif valor_sacar > 0:
            saldo -= valor_sacar
            numero_saques += 1
            extrato += f"Saque: R$ {valor_sacar:.2f}\n"
            print(f"Foi sacado R${valor_sacar:.2f} da sua conta!")
        else:
            print("Não foi possível sacar o valor inserido. Por favor, \
                  digite um número válido.")
        continue

    elif opcao == "e":
        print(extrato)
        print("Não foram realizadas movimentações." if not extrato
              else extrato)
        print(f'Saldo total: R${saldo:.2f}')
        continue

    elif opcao == "q":
        break

    else:
        print("Você não digitou nenhuma das opções!")

print("Encerrando a sessão!")
