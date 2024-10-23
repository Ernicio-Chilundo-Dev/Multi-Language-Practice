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
            palpite = input("Digite o seu palpite: ")
            tentativas += 1
            if palpite == numero_secreto:
                print(f"Parabens! Voce acertou o numero {numero_secreto} em {tentativas} tentativas!")
                break