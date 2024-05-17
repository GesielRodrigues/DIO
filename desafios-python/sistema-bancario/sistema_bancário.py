menu = """
    Menu de operações:

    [d] depositar
    [s] sacar
    [e] extrato
    [q] sair

"""

LIMITE_SAQUES = 3 # Limite de quantidade de saques.
LIMITE_SAQUE = 500 # Limite de valor do saque.
saldo = 0 # Toda conta iniciará com o saldo zerado.
numero_saques = 0 # Quantidade de saques realizados
extrato = "" # Extrato das operações


# função para depositar dinheiro
def depositar(valor):
    global saldo, extrato
    
    if valor < 0:
        print("Não é possível depositar um valor negativo!")
    else:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")


# função para sacar dinheiro
def sacar(valor):
    global saldo, numero_saques, extrato

    if valor < 0:
        print("Não é possível sacar um valor negativo!")
    elif numero_saques >= LIMITE_SAQUES:
        print("Você já realizou o limite máximo de saques!")
    elif valor > LIMITE_SAQUE:
        print("Valor superior ao seu limite de saque")
    elif valor > saldo:
        print("Saldo insuficiente!")
    else:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque: - R$ {valor:.2f}\n"
        print("Saque realizado com sucesso!")


# função para imprimir o extrato
def exibir_extrato():
    global extrato

    print()
    print("#" * 10, " EXTRATO " + "#" * 10)
    print("Não houve nenhuma movimentação" if not extrato else extrato)
    print("Seu saldo atual é de R$", saldo)
    print("#" * 30)

# loop principal do sistema bancário
while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado: R$"))
        depositar(valor)
        
        
    elif opcao == "s":
        valor = float(input("Digite o valor a ser sacado: R$"))
        sacar(valor)
        
        
    elif opcao == "e":
        exibir_extrato()


    elif opcao == "q":
        print("Obrigado por usar nosso sistema bancário!")
        break


    else:
        print("Opção inválida. Por favor, selecione uma opção do menu.")
