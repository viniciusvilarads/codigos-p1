usuario = input("Usuário: ")
senha = input("Senha: ")
while usuario == senha:
    print("Não é permitido usuario e senha igual! Digite novamente")
    usuario = input("Usuário: ")
    senha = input("Senha: ")

print("Usuário e senha cadastrado com sucesso!")
