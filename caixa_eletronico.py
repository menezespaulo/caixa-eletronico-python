conta_usuario = {
    "numero": "1234",
    "senha": "5678",
    "saldo_inicial": 1000.00    

}

print("Bem vindo ao sistema de autenticação do caixa eletrônico!")
while True:
    conta = input("Digite o número da conta: ")
    senha = input("Digite a senha: ")
    if conta == conta_usuario["numero"] and senha == conta_usuario["senha"]:
        print("Login bem-sucedido!")
        break
    else:
        print("Número da conta ou senha incorretos. Tente novamente.")

while True:
    print("\n---Menu de Operações---")
    print("Selecione a operação desejada no menu:")
    print("1. Ver saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Sair")
    opcao = input("Digite o número da operação desejada: ")
    match opcao:
        case "1":
            print(f"Saldo em conta: R${conta_usuario["saldo_inicial"]:.2f}")
        case "2":
            valor_deposito = float(input("Insira o valor a ser depositado: "))
            if valor_deposito > 0:
                conta_usuario["saldo_inicial"] += valor_deposito 
                print(f"Seu saldo atualizado é R${conta_usuario["saldo_inicial"]:.2f}")
        case "3":
            valor_saque = float(input("Insira o valor que deseja sacar: "))
            if valor_saque > 0 and valor_saque <= conta_usuario["saldo_inicial"]:
                conta_usuario["saldo_inicial"] -= valor_saque
                print(f"Saque de R${valor_saque:.2f} realizado com sucesso!")
                print(f"Seu saldo atualizado é de R${conta_usuario["saldo_inicial"]:.2f}")
            elif valor_saque > conta_usuario["saldo_inicial"]:
             print("Operação cancelada: Saldo insuficiente.")
            else:
                print("Valor de saque inválido.")
        
        case "4":
            print("Obrigado por utilizar o caixa eletrônico XYZ.")
            break
        case _:
            print("Opção inválida. Tente novamente")   




