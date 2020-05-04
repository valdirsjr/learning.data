def computador_escolhe_jogada(n,m,total):
    y = 0
    i = 1
    while i <= m:
        if (total - i) % (m + 1) == 0:
            y = i
        i = i + 1
            
    if y == 0:
        y = m
        
    if y == 1:
        print("O computador tirou uma peça.")
    else:
        print(f"O computador tirou {y} peças.")
    return y


def usuario_escolhe_jogada(n,m):
    y = m+1
    while y > m:
        y = int(input("Quantas peças você vai tirar? "))
        if y > m:
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            if y == 1:
                print("Você tirou uma peça.")
            else:
                print(f"Você tirou {y} peças.")
    return y

def partida():
    jogo = int(input("""
    Bem-vindo ao jogo do NIM! Escolha:

    1 - para jogar uma partida isolada
    2 - para jogar um campeonato
    """))
    if jogo == 1:
        campeonato = 1
    else:
        campeonato = 3
        print("Voce escolheu um campeonato!")
    rodada = 1    
    score_pessoa = 0
    score_computador = 0
    
    while rodada <= campeonato:
        if campeonato > 1:
            print(f"**** Rodada {rodada} ****")
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        total = n

        if n % (m + 1) == 0:
            print("Você começa!")
            player = 1
        else:
            print("Computador começa!")
            player = 0

        while total > 0:
            if player == 1:
                total = total - usuario_escolhe_jogada(n,m)
                player = 0
            else:
                total = total - computador_escolhe_jogada(n,m,total)
                player = 1

            if total > 1:
                print(f"Agora restam {total} peças no tabuleiro")
            elif total == 1:
                print(f"Agora resta apenas {total} peça no tabuleiro")
            else:
                if player == 1:
                    print("Fim do jogo! O computador ganhou!")
                    score_computador = score_computador + 1
                else:
                    print("Fim do jogo! Você ganhou!")
                    score_pessoa = score_pessoa + 1
        rodada = rodada + 1
    if campeonato > 1:
        print("**** Final do campeonato! ****")
        print(f"Placar: Você {score_pessoa} X {score_computador} Computador")
    


partida()