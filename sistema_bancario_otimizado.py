def menu():
    menu = """\n
    ******** MENU ********
    [d] Fazer deposito
    [s] Fazer Saque
    [e] Extrato
    [nu] Criar usuario
    [cn] Criar conta
    [ec] Exibir contas
    Digite sua opção """
    return input((menu))


def depositar_dinheiro (saldo, valor, extrato, /):
     if valor > 0:
        saldo += valor
        extrato += f"Deposito de R${valor}\n"
        print(f"Deposito de R${valor} realizado")
     else:
        print("Valor invalido")
     return saldo, extrato


def efetuar_saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    saldo_insuficiente = valor > saldo
    limite_insuficiente = valor > limite
    saques_insuficiente = numero_saques >= limite_saques

    if saldo_insuficiente:
        print("\n Sem saldo suficiente.")

    elif limite_insuficiente:
        print("\n O limite de saque é R$500")

    elif saques_insuficiente:
        print("\n Voce atingiu o limite diario de saques")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def puxar_extrato(saldo, /, *, extrato):
        print("**** EXTRATO ****")
        if extrato == "":
            print("\nNão foram realizadas movimentações")
        else:
            print(extrato)
            print(f"Saldo: R${saldo} ")

def criar_usuario(usuarios):
    cpf = input("Digite o seu CPF (apenas numeros): ")
    usuario = filtro_de_usuarios(cpf, usuarios)

    if usuario:
        print("CPF já cadastrado")
        return
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("*** Usuário criado com sucesso! ***")

def filtro_de_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta_usuario(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtro_de_usuarios(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
def exibir_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print((linha))

def principal():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []


    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar_dinheiro(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = efetuar_saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            puxar_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "cn":
            numero_conta = len(contas) + 1
            conta = criar_conta_usuario(AGENCIA, numero_conta, usuarios )

            if conta:
                contas.append(conta)
        
        elif opcao == "ec":
            exibir_contas(contas)
        
        elif opcao == "q":
            break
        
        else:
            print("Opção Invalida")


principal()