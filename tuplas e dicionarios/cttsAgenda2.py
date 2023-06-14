D = {}
while True:
    print("Bem-vindo ao programa Agenda de Contato")
    print("Digite 1 para cadastrar um contato")
    print("Digite 2 para consultar um contato")
    print("Digite 3 para excluir um contato")        
    print("Digite 0 para sair do programa")

    op = int(input())

    if op == 1:
        nome = input("Digite o nome do contato: ") 
        
        if nome in D:
            print("Contato com nome ja cadastrado")
        
        idade = input("Digite a sua idade: ")
        peso = input("Digite o seu peso: ")
        cidade = input("Digite a sua cidade: ")
        telefone = input("Digite o seu telefone: ")
        apelido = input("Digite o seu apelido: ")
        
        verifCtt = {
          'idade': idade,
          'peso': peso,
          'cidade': cidade,
          'telefone': telefone,
          'apelido': apelido,
        }    
        D[nome] = verifCtt
        print("Contato Cadastrado!")
    elif op == 2:
        nome = input('Digite o contato a ser verificado: ')
        
        if nome in D:
            verifCtt = D[nome]
            print("O contato {} tem {} anos de idade, pesa {} Kg, mora em {}, o telefone dele é {} e seu apelido é {}.".format(nome, verifCtt['idade'],verifCtt['peso'],verifCtt['cidade'],verifCtt['telefone'], verifCtt['apelido']))
        else: 
            print("Contato inexistente")
    elif op == 3:
        deleteNome = input('Digite o contato a ser deletado: ')
        if deleteNome in D:
            del D[nome]
            print("Exclusão realizada com sucesso")
        else:
            print("Contato inexistente")


    elif op == 0:
        break
            