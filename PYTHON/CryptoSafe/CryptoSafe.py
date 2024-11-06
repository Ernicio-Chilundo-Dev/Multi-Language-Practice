import os
from cryptography.fernet import Fernet

import getpass

# Função para gerar uma chave de criptografia e salvá-la em um arquivo
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

# Função para carregar a chave de criptografia
def carregar_chave():
    return open("chave.key", "rb").read()

# Função para criptografar um arquivo
def criptografar_arquivo(nome_arquivo, chave):
    fernet = Fernet(chave)
    with open(nome_arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = fernet.encrypt(dados)
    with open(nome_arquivo, "wb") as file:
        file.write(dados_encriptados)

# Função para descriptografar um arquivo
def descriptografar_arquivo(nome_arquivo, chave):
    fernet = Fernet(chave)
    with open(nome_arquivo, "rb") as file:
        dados_encriptados = file.read()
    dados = fernet.decrypt(dados_encriptados)
    with open(nome_arquivo, "wb") as file:
        file.write(dados)

# Função para configurar a pasta segura
def criar_pasta_segura():
    pasta = "Pasta_Segura"
    os.makedirs(pasta, exist_ok=True)
    gerar_chave()
    print("Pasta segura criada com sucesso!")

# Função para adicionar um arquivo à pasta segura e criptografá-lo
def adicionar_arquivo(nome_arquivo):
    chave = carregar_chave()
    criptografar_arquivo(nome_arquivo, chave)
    os.replace(nome_arquivo, os.path.join("Pasta_Segura", nome_arquivo))
    print(f"Arquivo {nome_arquivo} criptografado e movido para a pasta segura.")

# Função para acessar um arquivo na pasta segura e descriptografá-lo
def acessar_arquivo(nome_arquivo):
    chave = carregar_chave()
    caminho_arquivo = os.path.join("Pasta_Segura", nome_arquivo)
    if os.path.exists(caminho_arquivo):
        senha = getpass.getpass("Digite a senha para acessar o arquivo: ")
        if senha == "12345678":  # Substitua por uma senha segura
            descriptografar_arquivo(caminho_arquivo, chave)
            print(f"Arquivo {nome_arquivo} descriptografado e pronto para uso.")
        else:
            print("Senha incorreta. Acesso negado.")
    else:
        print("Arquivo não encontrado na pasta segura.")

# Menu para o usuário
def menu():
    print("=== Pasta Segura ===")
    print("1. Criar Pasta Segura")
    print("2. Adicionar Arquivo à Pasta Segura")
    print("3. Acessar Arquivo na Pasta Segura")
    print("4. Sair")
    while True:
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            criar_pasta_segura()
        elif escolha == "2":
            nome_arquivo = input("Digite o nome do arquivo para adicionar: ")
            adicionar_arquivo(nome_arquivo)
        elif escolha == "3":
            nome_arquivo = input("Digite o nome do arquivo para acessar: ")
            acessar_arquivo(nome_arquivo)
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()

