menu = '''
        MENU PRINCIPAL  
1 - Sacar
2 - Depositar
3 - Ver extrato
4 - Sair

Opção desejada: '''

saldo = 1500
quant_saques = 0
extrato = ''

while True:
    opc = int(input(menu))
    if opc == 1:
        if quant_saques < 3:
            valor_saque = float(input("Valor do saque: "))
            if saldo > valor_saque:
                if valor_saque <= 500 and valor_saque > 0:
                    saldo -= valor_saque
                    print("Saque realizado com sucesso!")
                    quant_saques +=1
                    extrato += f"Saque: R${valor_saque}\n"
                else:
                    print("Valor máximo do saque é de 500 reais.") 
            else:
                print("Sem saldo suficiente!")
        else:
            print("Limite de saques diários atingido! Tente novamente outro dia!")
    elif opc == 2:
        deposito = float(input("Valor do depósito: "))
        if deposito > 0:
            print("Depósito realizado com sucesso!")
            saldo += deposito
            extrato +=  f"Depósito: R${deposito}\n"
    elif opc == 3:
        print("-"*40)
        print("EXTRATO".center(40))
        print("Não houveram movimentações." if not extrato else extrato)
        print(f"\nSaldo: {saldo}")
        print("-"*40)
    elif opc == 4:
        print("Saindo...")
        break
    else:
        print("Escolha um opção válida!")      
