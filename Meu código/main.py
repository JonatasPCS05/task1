def logar(email, senha):
    if email in emails:
        if emails[email] == senha:
            print("Loguin efetuado com sucesso")
        else:
            print("Senha incorreta")
    else:
        print("Email não encontrado")

emails = {"jonatas@gmail.com": 1234}

logar('jonatas@gmail.com', 1234)