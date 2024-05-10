from datetime import datetime


class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.contas = []
        self.endereco = endereco

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.cliente = cliente
        self.historico = Historico()
        self.agencia = '0001'

    def ver_infoconta(self):
        print(f'''
Titular:         \t{self.cliente.nome}
Número da conta: \t{self.numero}
Agência:         \t{self.agencia}
''')

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.registrar("Depósito", valor)
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito!")

    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente!')
        elif valor <= 0:
            print("Insira um valor válido para saque!")
        else:
            self.saldo -= valor
            self.historico.registrar("Saque", valor)
            print("Saque realizado com sucesso!")

    def ver_extrato(self):
        self.historico.mostrar_registro(self.saldo)


class Historico:
    def __init__(self):
        self.registros = []

    def registrar(self, tipo_transacao, valor):
        self.registros.append({
            'Tipo': tipo_transacao,
            'Valor': valor,
            'Data': datetime.now()
        })

    def mostrar_registro(self, saldo):
        for transacao in self.registros:
            print(f"{transacao['Tipo']} de {transacao['Valor']} em {transacao['Data']}")
        print(f"Saldo atual: {saldo}")


lista_de_clientes = []


def criar_cliente():
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite a data de seu nascimento (dd/mm/yyyy): ")
    cpf = input("Digite seu CPF: ")
    endereco = input("Digite seu endereço: ")
    cliente = Cliente(nome, data_nascimento, cpf, endereco)
    lista_de_clientes.append(cliente)
    return cliente


def encontrar_conta(cpf, numero_conta):
    for cliente in lista_de_clientes:
        if cliente.cpf == cpf:
            for conta in cliente.contas:
                if conta.numero == numero_conta:
                    return conta
    return None


def interagir_com_conta(conta):
    while True:
        try:
            escolha = input(menu_conta())
        except ValueError:
            print("Erro!")
        if escolha == '1':
            valor = float(input("Valor do depósito: "))
            conta.depositar(valor)
        elif escolha == '2':
            valor = float(input("Valor do saque: "))
            conta.sacar(valor)
        elif escolha == '3':
            conta.ver_extrato()
        elif escolha == '4':
            conta.ver_infoconta()
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


def menu_inicial():
    return '''
1 - Cadastrar-se
2 - Entrar na conta
3 - Sair
Escolha: '''


def menu_conta():
    return '''
1 - Depositar
2 - Sacar
3 - Ver extrato
4 - Informações da conta
5 - Sair
Escolha: '''


def main():
    while True:
        try:
            opcao = input(menu_inicial())
        except ValueError:
            print("Erro!")
            continue

        if opcao == '1':
            cliente = criar_cliente()
            numero_conta = len(lista_de_clientes)  
            conta = Conta(numero_conta, cliente)
            cliente.adicionar_conta(conta)
            print("Cliente registrado e conta criada com sucesso!")
            conta.ver_infoconta()
        elif opcao == '2':
            cpf = input("Digite o CPF: ")
            numero_conta = int(input("Digite o número da conta: "))
            conta = encontrar_conta(cpf, numero_conta)
            if conta:
                print("Conta encontrada. Acessando...")
                interagir_com_conta(conta)
            else:
                print("Conta não encontrada.")
        elif opcao == '3':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
