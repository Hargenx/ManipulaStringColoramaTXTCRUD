import os
import colorama
from colorama import Fore, Style

# inicializa o módulo colorama
colorama.init(autoreset=True)

def pinta_amarelo(text):
    print('\033[33m{}\033[m'.format(text))

def pinta_vermelho(text):
    print('\033[31m{}\033[m'.format(text))

# verifica se o arquivo existe, caso contrário, cria um novo
if not os.path.exists('pessoas.txt'):
    open('pessoas.txt', 'w').close()

# função para limpar tela
def limpa_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
  
# função para adicionar uma nova pessoa
def adicionar_pessoa():
    print(Fore.BLUE + 'Adicionar nova pessoa' + Style.RESET_ALL)
    nome = input('Digite o nome da pessoa: ')
    idade = input('Digite a idade da pessoa: ')
    with open('pessoas.txt', 'a') as arquivo:
        arquivo.write(f'{nome},{idade}\n')
    print(Fore.GREEN + 'Pessoa adicionada com sucesso!' + Style.RESET_ALL)

# função para listar todas as pessoas
def listar_pessoas():
    print(Fore.BLUE + 'Listar todas as pessoas' + Style.RESET_ALL)
    with open('pessoas.txt', 'r') as arquivo:
        for linha in arquivo:
            nome, idade = linha.strip().split(',')
            print(f'Nome: {nome}, Idade: {idade}')
    print(Fore.GREEN + 'Fim da lista' + Style.RESET_ALL)

# função para atualizar informações de uma pessoa
def atualizar_pessoa():
    print(Fore.BLUE + 'Atualizar informações de uma pessoa' + Style.RESET_ALL)
    nome_antigo = input('Digite o nome da pessoa que deseja atualizar as informações: ')
    with open('pessoas.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
    for i, linha in enumerate(linhas):
        nome, idade = linha.strip().split(',')
        if nome == nome_antigo:
            novo_nome = input('Digite o novo nome da pessoa: ')
            nova_idade = input('Digite a nova idade da pessoa: ')
            linhas[i] = f'{novo_nome},{nova_idade}\n'
            with open('pessoas.txt', 'w') as arquivo:
                arquivo.writelines(linhas)
            print(Fore.GREEN + 'Informações atualizadas com sucesso!' + Style.RESET_ALL)
            return
    print(Fore.RED + 'Pessoa não encontrada!' + Style.RESET_ALL)

# função para excluir uma pessoa
def excluir_pessoa():
    print(Fore.BLUE + 'Excluir uma pessoa' + Style.RESET_ALL)
    nome = input('Digite o nome da pessoa que deseja excluir: ')
    with open('pessoas.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
    for i, linha in enumerate(linhas):
        if nome in linha:
            del linhas[i]
            with open('pessoas.txt', 'w') as arquivo:
                arquivo.writelines(linhas)
            print(Fore.GREEN + 'Pessoa excluída com sucesso!' + Style.RESET_ALL)
            return
    print(Fore.RED + 'Pessoa não encontrada!' + Style.RESET_ALL)

# loop principal do menu
def main():
  while True:
    limpa_tela()
    opcoes = [
      ('Sair', exit),
      ('Adicionar pessoa', adicionar_pessoa),
      ('Listar pessoas', listar_pessoas),
      ('Atualizar informações de uma pessoa', atualizar_pessoa),
      ('Excluir pessoa', excluir_pessoa),
      ]
    print(Fore.YELLOW + '========= MENU =========' + Style.RESET_ALL)
    for i, opcao in enumerate(opcoes):
      print(f'{i} - {opcao[0]}')
  
    
    '''print(Fore.YELLOW + '========= MENU =========' + Style.RESET_ALL)
    print('1 - Adicionar pessoa')
    print('2 - Listar pessoas')
    print('3 - Atualizar informações de uma pessoa')
    print('4 - Excluir pessoa')
    print('0 - Sair')'''
    
    opcao = input('Digite a opção desejada: ')
    match opcao:
      case '0':
        break
      case '1':
        adicionar_pessoa()
      case '2':
        listar_pessoas()
      case '3':
        atualizar_pessoa()
      case '4':
        excluir_pessoa()
      case _:
        print(Fore.RED + 'Opção inválida!' + Style.RESET_ALL)
        
    '''if opcao == '1':
        adicionar_pessoa()
    elif opcao == '2':
        listar_pessoas()
    elif opcao == '3':
        atualizar_pessoa()
    elif opcao == '4':
        excluir_pessoa()
    elif opcao == '0':
        break
    else:
        print(Fore.RED + 'Opção inválida!' + Style.RESET_ALL)'''
  
    if opcao.isdigit() and int(opcao) in range(len(opcoes)):
      opcoes[int(opcao)][1]()
    else:
      print(Fore.RED + 'Opção inválida!' + Style.RESET_ALL)
  
    input('Pressione ENTER para MENU...')

if __name__=='__main__':
  main()