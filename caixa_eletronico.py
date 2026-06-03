conta_correta = "1234"
senha_correta = "5678"
saldo_inicial = 1000.00 

print("Bem vindo ao sistema de autenticação do caixa eletrônico!")
while True:
    conta = input("Digite o número da conta: ")
    senha = input("Digite a senha: ")
    if conta == conta_correta and senha == senha_correta:
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
            print(f"Saldo em conta: R${saldo_inicial:.2f}")
        case "2":
            print("Funcionalidade de depósito em construção")
        case "3":
            print("Funcionalidade de saque em construção")
        case "4":
            print("Obrigado por utilizar o caixa eletrônico XYZ.")
            break
        case _:
            print("Opção inválida. Tente novamente")   




