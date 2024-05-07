def criarusuario(lista):
    usuarios = {}

    while True:
        usuarios['CPF'] = str(input("CPF: ")).replace("-","").replace(".","").strip()
        if len(usuarios['CPF']) < 11 or usuarios['CPF'] == '':
            print("Preencha o seu CPF corretamente.")
            continue
        else:
            for cadastro in lista:
                if usuarios['CPF'] == cadastro['CPF']:
                    print("CPF já existente no sistema.")
                    return None
        break

    usuarios['nomeCompleto'] = str(input("Nome completo: "))
    usuarios['dataNascimento'] = str(input(("Data de nascimento (dd/mm/aaaa): ")))
    usuarios['endereco'] = str(input("Endereço: "))

    print("Usuário cadastrado com sucesso!")

    return usuarios

def criarconta(lista):
    contas = {}

    while True:
        contas['CPF'] = str(input("CPF: ")).replace("-","").replace(".","").strip()
        if len(contas['CPF']) != 11 or contas['CPF'] == '':
            print("Preencha o seu CPF corretamente.")
            continue
        break

    for cadastro in lista_de_usuarios:
        if cadastro['CPF'] == contas['CPF']:
            print("Conta criada com sucesso!")
            contas['nomeCompleto'] = cadastro['nomeCompleto']
            break
    else:
        print("CPF não encontrado!")
        return None
    
    contas['agencia'] = '0001'
    contas['numerodaconta'] = len(lista_de_usuarios) + 1

    
    return contas

lista_de_usuarios = list()
lista_de_contas = list()



def fazer_login(lista, nome, cpf):
    for cadastro in lista:
        if cadastro['nomeCompleto'].lower() == nome.lower() and cadastro['CPF'] == cpf:
            print("Entrando na conta...")
            return True
    print("Conta não encontrada!")
    return False


def processar_saque(*,valor_saque, saldo, limite=500,extrato,quant_saques):
    if valor_saque <= 0:
        print("O saque deve ser maior que 0.")
        return saldo, extrato, quant_saques
    
    if saldo >= valor_saque:
        if valor_saque <= limite:
            novo_saldo = saldo - valor_saque
            print("Saque realizado com sucesso!")
            extrato += f"Saque: R${valor_saque:.2f}\n"
            quant_saques += 1
            return novo_saldo, extrato, quant_saques
        else:
            print(f"Valor máximo do saque é de R${limite:.2f}.") 
    else:
        print("Sem saldo suficiente!")
    
    return saldo, extrato, quant_saques


def imprimir_extrato(extrato,/,*, saldo):
    print("-"*40)
    print("EXTRATO".center(40))
    print("Sem transações." if not extrato else extrato)
    print(f"\nSaldo: {saldo:.2f}")
    print("-"*40)


def processar_deposito(valor_depo, saldo, extrato,/):
    if valor_depo > 0:
            print("Depósito realizado com sucesso!")
            novo_saldo = saldo + valor_depo
            extrato +=  f"Depósito: R${deposito:.2f}\n"
            return novo_saldo, extrato
    else:
        print("O valor do depósito deve ser maior que 0!")  
        return saldo, extrato



menu_inicial = '''
-------------------------------------
             Menu de Login

1 - Entrar na conta
2 - Cadastrar usuário
3 - Criar conta (necessário usuário)
4 - Sair

-------------------------------------

Digite a opção desejada: '''


menu_banco = '''
-------------------------------------
             MENU PRINCIPAL  
1 - Sacar
2 - Depositar
3 - Ver extrato
4 - Sair da conta

-------------------------------------

Digite a opção desejada: '''



while True:
    try:
        opc = int(input(menu_inicial))
    except ValueError:
        print("Escolha um opção válida!")
    
    if opc == 1:
        nome = str(input("Nome completo: "))
        senha = str(input("Senha (CPF): "))
        entrar = fazer_login(lista_de_usuarios, nome, senha)
        
        if entrar == True:
            saldo = 0
            quant_saques = 0
            extrato = ''
                
            while True:
                try:
                    opcbanco = int(input(menu_banco))
                except ValueError:
                    print("Escolha uma opção válida!")
                    continue
                if opcbanco == 1:
                    if quant_saques < 3:
                        try:
                            valor_saque = float(input("Valor do saque: "))
                            saldo, extrato, quant_saques = processar_saque(valor_saque=valor_saque, saldo=saldo, extrato=extrato, quant_saques=quant_saques, limite=500)
                        except:
                            print("Erro!")
                            continue
                    else:
                        print("Limite de saques diários atingido! Tente novamente outro dia!")
                elif opcbanco == 2:
                    try:
                        deposito = float(input("Valor do depósito: "))
                        saldo, extrato = processar_deposito(deposito, saldo, extrato)
                    except:
                        print('Erro!')
                elif opcbanco == 3:
                    imprimir_extrato(extrato, saldo=saldo)
                elif opcbanco == 4:
                    print("Saindo...")
                    break
                else:
                    print("Escolha um opção válida!") 

    elif opc == 2:
        lista_de_usuarios.append(criarusuario(lista_de_usuarios))
    elif opc == 3:
        lista_de_contas.append(criarconta(lista_de_contas))
    elif opc == 4:
        print('Saindo...')
        break
    else:
        print("Escolha uma opção válida!")
