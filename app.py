import sys

# Exibir a versão do Python
print(sys.version)

def saudacao():
    print("Olá! Bem-vindo à Mecânica GT. Como posso ajudá-lo hoje?")
    print("1. Agendar um serviço")
    print("2. Informações sobre os serviços")
    print("3. Falar com um atendente")
    print("4. Sair")

def agendar_servico():
    nome = input("Por favor, insira seu nome: ")
    contato = input("Por favor, insira seu telefone para contato: ")
    data = input("Qual a data desejada para o serviço? (DD/MM/AAAA): ")
    print(f"Obrigado, {nome}! Seu agendamento para {data} foi registrado. Entraremos em contato pelo número {contato} para confirmar.")

def info_servicos():
    print("Oferecemos os seguintes serviços:")
    print("1. Troca de óleo")
    print("2. Revisão completa")
    print("3. Balanceamento e alinhamento")
    print("4. Diagnóstico eletrônico")
    print("5. Voltar ao menu principal")

def main():
    while True:
        saudacao()
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == "1":
            agendar_servico()
        elif opcao == "2":
            info_servicos()
        elif opcao == "3":
            print("Por favor, entre em contato com nossa central pelo telefone (11) 1234-5678.")
        elif opcao == "4":
            print("Obrigado por visitar a Mecânica GT. Tenha um ótimo dia!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
