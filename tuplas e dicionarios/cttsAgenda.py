while True:
  D = {}
  D['nome'] = input()
  D['idade'] = int(input())
  D['peso'] = float(input())
  D['cidade'] = input()
  D['telefone'] = int(input())
  D['apelido'] = input()




  print("O contato {} tem {} anos de idade, pesa {} Kg, mora em {}, o telefone dele é {} e seu apelido é {}.".format(D['nome'], D['idade'],D['peso'],D['cidade'],D['telefone'], D['apelido']))