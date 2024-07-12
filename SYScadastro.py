import os
import time

lista_cpf = ['58975285', '23855896', '77559132', '49562831']
lista_usuarios = ["fernande", "moreira", "sousa", "amaral"]

while True: 
    print(30*'=', 'Bem- vindo ao Python cadastros', 30*'=')
    print('1. Cadastrar Usuário')
    print('2. Consultar Usuário')
    print('3. Acessar o sistema')
    print('4. Remover um usuário')
    print('5. Sair')

    opcao = input('Digite a opção desejada: (1-2-3-4-5)')

    #opcao para cadastrar usuario
    if opcao == '1':
        os.system('cls')
        novo_nome = input("Digite o nome que será cadastrado: ")
        novo_cpf = input('Digite um novo cpf: ')

        if novo_cpf in lista_cpf:
            print('O cpf digitado já existe.')
        else:
            lista_cpf.append(novo_cpf)
            print('CPF cadastrado com sucesso!')
            
    #opcao consultar uduario
    elif opcao == '2':
        os.system('cls')
        for i in lista_usuarios:
            print(f'Usuário: {i}')
    
    #opcao para acessar o sistema
    elif opcao == '3':
        os.system('cls')
        cpf_login = input('Digite o CPF: ')
        if cpf_login in lista_cpf:
             print('Acesso realizado com sucesso.')   
        else:
            print('Usuário não possui cadastro.')

    #opcao para remover o usuario
    elif opcao == '4':
        os.system('cls')
        cpf_remove = input('Digite o CPF a ser excluído:')
        if cpf_remove in lista_cpf:
            indice = lista_cpf.index(cpf_remove)
            nome = lista_usuarios.pop(indice)
            lista_cpf.pop(indice)

            print(f'Usuário: {nome} de CPF {cpf_remove} foi removido com sucesso!')

    #opcao para sair
    elif opcao == '5':
        os.system('cls')
        print('O sistema será encerrado.')
        time.sleep(3)
        break
    else:
        print('Opção inválida!')


