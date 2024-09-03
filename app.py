import sys
import time

# Exibir a versão do Python
print(sys.version)

def saudacao():
    print("\n" * 2)  # Adiciona duas linhas em branco antes da saudação
    print("Olá! Bem-vindo à Mecânica GT. Como posso ajudá-lo hoje?")
    print("1. Agendar um serviço")
    print("2. Informações sobre os serviços")
    print("3. Falar com um atendente")
    print("4. Sair")
    print("\n" * 2)  # Adiciona duas linhas em branco após o menu

def agendar_servico():
    nome = input("Por favor, insira seu nome: ")
    contato = input("Por favor, insira seu telefone para contato: ")
    data = input("Qual a data desejada para o serviço? (DD/MM/AAAA): ")
    print(f"Obrigado, {nome}! Seu agendamento para {data} foi registrado. Entraremos em contato pelo número {contato} para confirmar.")
    time.sleep(5)  # Delay de 5 segundos antes de voltar ao menu principal

def info_servicos():
    print("\n" * 2)  # Adiciona duas linhas em branco antes da lista de serviços
    print("Oferecemos os seguintes serviços:")
    print("1. Troca de óleo")
    print("2. Revisão completa")
    print("3. Balanceamento e alinhamento")
    print("4. Diagnóstico eletrônico")
    print("5. Voltar ao menu principal")
    print("\n" * 2)  # Adiciona duas linhas em branco após a lista
    time.sleep(5)  # Delay de 5 segundos antes de voltar ao menu principal

def main():
    while True:
        saudacao()
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == "1":
            agendar_servico()
        elif opcao == "2":
            info_servicos()
        elif opcao == "3":
            print("\nPor favor, entre em contato com nossa central pelo telefone (11) 1234-5678.\n")
            time.sleep(5)  # Delay de 5 segundos antes de voltar ao menu principal
        elif opcao == "4":
            print("\nObrigado por visitar a Mecânica GT. Tenha um ótimo dia!\n")
            break
        else:
            print("\nOpção inválida. Por favor, tente novamente.\n")
            time.sleep(2)  # Delay de 2 segundos antes de pedir novamente

if __name__ == "__main__":
    main()
