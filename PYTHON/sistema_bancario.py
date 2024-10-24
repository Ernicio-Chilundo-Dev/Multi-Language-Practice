# Obejeto para armazenar as contas criadas
contas ={}

# Funcao para criar novas contas
def criar_conta(numero_conta,nome_cliente):
    if numero_conta in contas:
        print("Erro: esta conta ja existe!")
        return False
    contas[numero_conta] = {"nome":nome_cliente, "saldo": 0}
    print(f"Conta criada com sucesso para {nome_cliente}")
    return True

# Funcao para verficar saldo
def verficar_saldo(numero_conta):
    if numero_conta in contas:
        saldo = contas[numero_conta]["saldo"]
        print(f"O saldo da conta {numero_conta}: tem R$ {saldo:.2f}")
        return saldo
    else:
        print("Erro: Conta nao encontrada!")
        return None
    

# Funcao para depositar

def depositar(numero_conta,valor):
    if numero_conta in contas:
        contas[numero_conta]['saldo'] += valor
        print(f"Deposito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Erro: Conta nao encontrada!")

# Funcao para sacar

def sacar(numero_conta,valor):
    if numero_conta in contas:
        if contas[numero_conta]['saldo'] >= valor:
            contas[numero_conta]['saldo'] -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("\33[31mErro: Saldo insuficiente!\33[m")
    else:
        print("Erro: Conta nao encontrada!")

# Funcao para encerrar a conta

def encerrar(numero_conta):
    if numero_conta in contas:
        if contas[numero_conta]['saldo'] == 0:
            del contas[numero_conta]
            print(f"Conta {numero_conta} encerrada.")
        else:
            print("Erro: A conta ainda tem saldo! Retire o saldo antes de encerrar.")
    else:
        print("Erro: Conta nao encontrada!")

# Funcap menu, funcao principal do sistema bancario

def menu():
    while True:
        print("\n\33[36m{:=^40}".format("SISTEMA BANCARIO"))
        print("1. Criar nova conta")
        print("2. Verficar saldo")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Encerrar conta")
        print("6. Sair")
        print("\n\33[36m{:=^40}".format("SISTEMA BANCARIO"))

        opcao = input("Digite a sua opcao: ")

        if opcao == "1":
            numero_conta = input("Digite o numero da sua conta: ")
            nome_cliente = input("Digite o nome do cliente: ")
            criar_conta(numero_conta,nome_cliente)
        elif opcao == "2":
            numero_conta = input("Digite o numero da conta: ")
            verficar_saldo(numero_conta)
        elif opcao == "3":
            numero_conta = input("Digite o numero da conta: ")
            valor = float(input("Digite o valor a depositar: "))
            depositar(numero_conta,valor)
        elif opcao == "4":
            numero_conta = input("Digite o numero da conta: ")
            valor = float(input("Digite o valor a sacar: "))
            sacar(numero_conta,valor)
        elif opcao == "5":
            numero_conta = input("Digite o numero da conta: ")
            encerrar(numero_conta)
        elif opcao == "6":
            print("Saindo do sistema bancario")
            break
        else:
            print("Erro: Opcao inavalida!")

menu()            