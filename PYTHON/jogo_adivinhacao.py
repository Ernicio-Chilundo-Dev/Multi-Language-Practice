from random import randint
def jogo_adivinhacao():
    print("Seja bevido ao jogo de adivinhacao")
    joga_novamente = True
    while joga_novamente:
        numero_secreto =randint(1,10)
        tentativas =0 
        max_tentativas = 5
        print("\nTente adivinhar numero entre 1 - 10! Voce tem 5 tentativas.")

        while tentativas < max_tentativas:
            palpite = int(input("Diga - me o seu palpite: "))
            tentativas += 1

            if palpite == numero_secreto:
                print(f"Parabens! Voce acertou o numero {numero_secreto} em {tentativas} tentativas.")
                break
            elif palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            else:
                print("Muito alto! Tente novamente.")
            if tentativas == max_tentativas:
                print(f"Voce nao conseguiu acertar o numero {max_tentativas} tentativas. O numero era {numero_secreto}.")
        joga_novamente_input = input("Deseja continuar a jogar (S/N): ").lower()
        if joga_novamente_input != "s":
            joga_novamente = False
            print("Muito obrigado por jogar! Volte sempre.")

jogo_adivinhacao()           