def calcula_imc():
    print("Calculadoara de IMC")
    print("@" * 30)
    
    try:
     nome = input("Digite seu nome: ")
     peso = float(input("Digite o seu peso em kg: "))
     altura = float(input("Digite a sua altura em metros: "))
     imc = peso / (altura ** 2)
     print(f"Oi \33[36m{nome}\33[m o seu IMC e \33[36m{imc:.2f}\33[m")
     if imc < 18.5:
         print("Classificacao: Abaixo do peso.")
     elif 18.5 <= imc < 24.9:
         print("Classificacao: \33[32mPeso normal. Parabens!!!\33[m")
     elif 25 <= imc < 29.9:
         print("Classificacao: Sobrepeso.")
     elif 30 <= imc < 34.9:
         print("Classificacao: Obesidade grau I.")
     elif 35 <= imc < 39.9:
         print("Classificacao: Obesidade grau II.")
     else:
         print("\33[31mClassifcacao: OBesidade grau III. Cuidado!!!\33[m")
    except ValueError:
        print("Error: digite um valor valido para o seu peso e altura!!!")
        
        
calcula_imc()    