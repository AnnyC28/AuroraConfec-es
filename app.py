import os

noivas = [{'nome':'Ana', 'categoria':'vestido Mediterrâneo', 'em produção': True},
          {'nome':'Nickolle', 'categoria': 'vestido Sereia', 'em produção': True},
          {'nome':'Tauany', 'categoria': 'vestido Tradicional', 'em produção': False}]

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print("")

def retorna_menu_principal():
    input('\n Digite uma tecla para voltar ao menu principal')
    main()


def mostra_titulo():

    print('''
          

     𝔸𝕦𝕣𝕠𝕣𝕒 ℂ𝕠𝕟𝕗𝕖𝕔𝕔̧𝕠̃𝕖𝕤\n
          ''')

def mostra_escolhas():
    print('1. Cadastro de confecções de vestidos de noiva')
    print('2. Listar horários de produção de vestidos agendados')
    print('3. Ativar cadastro de cliente com vestidos em produção')
    print('4. Sair da aplicação')

def escolhe_opcao():
 try:
    opcao_escolhida = int(input('Escolha uma opção: '))
    print('Você escolheu a opção: ' , opcao_escolhida)


    if opcao_escolhida == 1:
        print('Cadastrar noivas para confecção dos vestidos')
    elif opcao_escolhida == 2:
        print('Listar horários e consultas de orçamento agendados')
    elif opcao_escolhida == 3:
        print('Ativar/Desativar cadastro de noivas')
    elif opcao_escolhida == 4:
        finalizar_programa()
    else:
        opcao_invalida()
 except:
  opcao_invalida()

def cadastrar_confeccao():
     exibir_subtitulo('Cadastrar noiva')

     nome_cliente = input('Digite o nome da noiva: ')
     noivas.append(nome_cliente)
     print(f' {nome_cliente} foi adicionado(a) as noivas da confecção')
     retorna_menu_principal()

def mostrar_noivas():
    exibir_subtitulo('Cadastrar noiva')

    for noiva in noivas:
        nome_noiva = noiva['nome']
        categoria = noiva['categoria']
        ativo = noiva['ativo']

        print(f' - {noiva} {categoria} {ativo}')
        retorna_menu_principal
     
def finalizar_programa():
        os.system('cls')
        print('Finalizando programa')

def opcao_invalida():
        print('Esse caractere não é permitido')
        input('Digite qualquer tecla')
        main()
def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == '__main__':
    main()