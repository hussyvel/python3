print("******************")
print("Bem vindo no jogo ")
print("******************")

numero_do_chute = 42
tentativa = 3
rodada = 1
while(rodada <= tentativa):
    print("Tentativa",rodada, "de", tentativa)
    chute_str = input("Digite um numero:")

    chute = int(chute_str)


    acertou = chute == numero_do_chute
    maior = chute > numero_do_chute
    menor = chute < numero_do_chute


    if (acertou):
        print("Acertou")
    elif (maior):
        print('Errou, o chute foi maior que o numero secreto')
    elif (menor):
        print("Errou, o chute foi menor que o numero secreto")    
    print("Fim de jogo Uai!!!")
    rodada = rodada + 1