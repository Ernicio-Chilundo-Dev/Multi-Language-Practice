from random import randint
from time import sleep

computador = randint(0,2)
itens=['Pedra',"Papel",'Tesoura']
print("""Suas opcoes:
[0] PEDRA
[1] PAPEL
[2] TESOURA
      """)
jogador = int(input("Qual e a sua opcao: "))
if jogador <= 2:
    print('{:=^40}'.format("JOGADOR"))
    print("\n\33[32mO jogador jogou\33[m\33[34m {}\33[m".format(itens[jogador]))
    print("\n{:#^40}".format("COMPUTADOR"))
    print(f"\n\33[34mO Computador jogou\33[m\33[32m {itens[computador]}\33[m\n")
    print("{:=^40}".format("JOKENPO"))
    sleep(1)
    print("\33[32mJO\33[m")
    sleep(0.5)
    print("\33[33mKEN\33[m")
    sleep(0.5)
    print("\33[31mPO\33[m")
    sleep(1)
else:
    print("\33[31mJogada invalida tente novamante!\33[m]")


print('\n{:=^40}\n'.format("FIM"))

if computador == 0:
    if jogador == 0:
        print("\33[33mEmpate!\33[m")
    elif jogador == 1:
        print("\33[34mJogador venceu!\33[m")
    elif jogador == 2:
        print("\33[32mComputador venceu!\33[m")
elif computador == 1:
    if jogador == 0:
        print("\33[32mComputador venceu!\33[m")
    elif jogador == 1:
        print("\33[33mEmpate!\33[m")
    elif jogador == 2:
        print("\33[34mJogador venceu!\33[m")
elif computador == 2:
    if jogador == 0:
        print("\33[34mJogador venceu!\33[m")
    elif jogador == 1:
        print("\33[32mComputador venceu!\33[m")
    elif jogador == 2:
        print("\33[33mEmpte!\33[m")