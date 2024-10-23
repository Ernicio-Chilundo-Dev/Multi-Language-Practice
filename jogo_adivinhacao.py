from random import randint
def jodo_adivinhacao():
    print("Seja bevido ao jo de adivinhacao")
    jogar_novamente = True
    while jogar_novamente:
        numero_secreto = randint(1,100)
        tentativas= 0
        max_tentativas = 5
        print("\nTente adivinhar entre 1 - 100 o numero escolhido. Voce tem 5 tentativas.")
        while tentativas < max_tentativas:
            palpite = int(input("Digite o seu palpite: "))
            tentativas += 1
            if palpite == numero_secreto:
                print(f"Parabens! Voce acertou o numero {numero_secreto} em {tentativas} tentativas!")
                break
            elif palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            else:
                print("Muito alto! Tente novamente.")
            if tentativas == max_tentativas:
                print(f"Voce nao conseguiu acertar em {max_tentativas} tentativas. O numero era {numero_secreto}.")
        jogar_novamente_input = input("Deseja jogar continuar a jogar (S/N): ").lower()
        if jogar_novamente_input != "s":
            jogar_novamente = False
            print("Muito obrigado por jogar! Volte sempre.")
jodo_adivinhacao()            