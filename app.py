import os

def mostra_titulo():

    print('Aurora confecções\n')

def mostra_escolhas():
    print('1. Cadastro de confecções de vestidos de noiva')
    print('2. Listar horários de produção de vestidos agendados')
    print('3. Ativar cadastro de cliente com vestidos em produção')
    print('4. Sair da aplicação')

def escolhe_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    print('Você escolheu a opção: ' , opcao_escolhida)

    def finalizar_programa():
        os.system('cls')
        print('Finalizando programa')

    if opcao_escolhida == 1:
        print('Cadastrar vestidos para confecção')
    elif opcao_escolhida == 2:
        print('Listar horários e consultas de orçamento agendados')
    elif opcao_escolhida == 3:
        print('Ativar/Desativar cadastro de clientes')
    else:
        finalizar_programa()

def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == '__main__':
    main()