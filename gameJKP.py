from random import randint

# 0 - Pedra
# 1 - Papel
# 2 - Tesoura

# Declarando variaveis

jogadores = ["Teilor", "Computador"]
pedra = 0
papel = 1
tesoura = 2
quantidadeEmpates = 0
partidas = {}
chave = 1
vitorias = []
derrotas = []

# Funcoes

# Funcao principal que calcula o resultado da jogada
def testarJogada(nomeJogador1, jogada1, nomeJogador2, jogada2):
  global quantidadeEmpates
  global partidas
  global chave
  global pedra
  global papel
  global tesoura

  if (jogada1 == pedra) & (jogada2 == pedra):
    print("Empate!")
    quantidadeEmpates += 1
    partidas[nomeJogador1+" -> Pedra VS "+nomeJogador2+" -> Pedra"]=chave
    chave += 1
  elif (jogada1 == papel) & (jogada2 == papel):
    print("Empate!")
    quantidadeEmpates += 1
    partidas[nomeJogador1+" -> Papel VS "+nomeJogador2+" -> Papel"]=chave
    chave += 1
  elif (jogada1 == tesoura) & (jogada2 == tesoura):
    print("Empate!")
    quantidadeEmpates += 1
    partidas[nomeJogador1+" -> Tesoura VS "+nomeJogador2+" -> Tesoura"]=chave
    chave += 1
  elif (jogada1 == pedra) & (jogada2 == papel):
    print("Papel embrulhou a Pedra!")
    print(nomeJogador2,"venceu esta partida!")
    partidas[nomeJogador1+" -> Pedra VS "+nomeJogador2+" -> Papel"]=chave
    chave += 1
    vitorias.append(nomeJogador2)
    derrotas.append(nomeJogador1)
  elif (jogada1 == papel) & (jogada2 == pedra):
    print("Papel embrulhou a Pedra!")
    print(nomeJogador1,"venceu esta partida!")
    partidas[nomeJogador1+" -> Papel VS "+nomeJogador2+" -> Pedra"]=chave
    chave += 1
    vitorias.append(nomeJogador1)
    derrotas.append(nomeJogador2)
  elif (jogada1 == pedra) & (jogada2 == tesoura):
    print("Pedra esmagou a Tesoura!")
    print(nomeJogador1,"venceu esta partida!")
    partidas[nomeJogador1+" -> Pedra VS "+nomeJogador2+" -> Tesoura"]=chave
    chave += 1
    vitorias.append(nomeJogador1)
    derrotas.append(nomeJogador2)
  elif (jogada1 == tesoura) & (jogada2 == pedra):
    print("Pedra esmagou a Tesoura!")
    print(nomeJogador2,"venceu esta partida!")
    partidas[nomeJogador1+" -> Tesoura VS "+nomeJogador2+" -> Pedra"]=chave
    chave += 1
    vitorias.append(nomeJogador2)
    derrotas.append(nomeJogador1)
  elif (jogada1 == papel) & (jogada2 == tesoura):
    print("Tesoura cortou o Papel!")
    print(nomeJogador2,"venceu esta partida!")
    partidas[nomeJogador1+" -> Papel VS "+nomeJogador2+" -> Tesoura"]=chave
    chave += 1
    vitorias.append(nomeJogador2)
    derrotas.append(nomeJogador1)
  elif (jogada1 == tesoura) & (jogada2 == papel):
    print("Tesoura cortou o Papel!")
    print(nomeJogador1,"venceu esta partida!")
    partidas[nomeJogador1+" -> Tesoura VS "+nomeJogador2+" -> Papel"]=chave
    chave += 1
    vitorias.append(nomeJogador1)
    derrotas.append(nomeJogador2)

# Programa pricipal

while True:
  print ("\n" * 50) 
  print("/********** Jo-Ken-Po **********\ ")
  print("|                               |")
  print("| 1: Jogar sozinho              |")
  print("| 2: 2 Jogadores                |")
  print("| 3: Estatisticas de jogo       |")
  print("|                               |")
  print("| 0: Encerrar                   |")
  print("|                               |")
  print("\*******************************/\n")
  menu = input("Escolha a operação: ")

  if menu == "1":
    print("\n" * 50)
    novoJogador = input("Escolha seu nickname: ")
    jogadores.append(novoJogador)

    while True:
      input("\nPressione Enter para jogar!")
      print("  ---------------------------  ")
      print("| Código      -       Jogada  |")
      print("|                             |")
      print("|  0                   Pedra  |")
      print("|  1                   Papel  |")
      print("|  2                 Tesoura  |")
      print("|                             |")
      print("|  9          Voltar ao menu  |")
      print("  ---------------------------  \n")
      opcao = input("Entre com o código da jogada: ")

      if opcao == "0":
        testarJogada(novoJogador, 0, "Computador", randint(0,2))
      elif opcao == "1":
        testarJogada(novoJogador, 1, "Computador", randint(0,2))
      elif opcao == "2":
        testarJogada(novoJogador, 2, "Computador", randint(0,2))
      elif opcao == "9":
        break
      else:
        input("\nCódigo desconhecido. Pressione Enter para tentar novamente.")

  if menu == "2":
    print("\n" * 50)
    novoJogador = input("Jogador 1, escolha seu nickname: ")
    jogadores.append(novoJogador)

    novoJogador2 = input("Jogador 2, escolha seu nickname: ")
    jogadores.append(novoJogador2)

    while True:
      input("\nPressione Enter para jogar!")
      print("  ---------------------------  ")
      print("| Código      -       Jogada  |")
      print("|                             |")
      print("|  0                   Pedra  |")
      print("|  1                   Papel  |")
      print("|  2                 Tesoura  |")
      print("|                             |")
      print("|  9          Voltar ao menu  |")
      print("  ---------------------------  \n")
      print("EXTREMAMENTE PROIBIDO OLHAR NA TELA QUANDO O OUTRO JOGADOR ESTIVER ESCOLHENDO")
      opcao = input("Jogador 1, entre com o código da jogada: ")
      print("\n" * 50)
      opcao2 = input("Jogador 2, entre com o código da jogada: ")

      if (opcao == "0" or opcao == "1" or opcao == "2") and (opcao2 == "0" or opcao2 == "1" or opcao2 == "2"):
        testarJogada(novoJogador, int(opcao), novoJogador2, int(opcao2))
      elif opcao == "9" or opcao2 == "9":
        break
      else:
        input("\nCódigo desconhecido. Pressione Enter para tentar novamente.")

  elif menu == "3":
    print("\n" * 50)

    while True:
      print("        _______________________")
      print("        \ 1 = Partidas,Empates/")
      print("         \  2 = Percentual   /")
      print("          \   3 = Historico /")
      print("           \    9 = sair   /")
      print("            \ ----------- /")
      print("             \    J O    /")
      print("              \   KEN   /")
      print("               \  P O  /")
      print("                \  !  /")
      print("                 \ ! /")
      print("                  \_/\n")
      opcao = input("Entre com o código da operação desejada: ")

      if opcao == "1":
        print("Numero de empates =",quantidadeEmpates)
        print("Quantidade de partidas realizadas =",len(partidas))
        input("Pressione Enter para voltar ao menu.")

      elif opcao == "2":
        for nome in jogadores:
          print(nome,"ganhou",vitorias.count(nome),"partidas e perdeu",derrotas.count(nome))
        input("Pressione Enter para voltar ao menu.")

      elif opcao == "3":
        for historico, partida in partidas.items():
          print("Partida N°",partida,"=",historico)
        input("Pressione Enter para voltar ao menu.")

      elif opcao == "9":
        break

      else:
        input("\nCódigo desconhecido. Pressione Enter para tentar novamente.")

  elif menu == "0":
    input("Obrigado por jogar.")
    break

  else:
    input("\nCódigo desconhecido. Pressione Enter para tentar novamente.")