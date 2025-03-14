import var

def logar(email, senha):
    #email = input("Digite seu email: ")
    if email in var.emails:
        for i in range(5):
            #senha = input("Digite sua senha: ")
            if var.emails[email] == senha:
                print("Loguin efetuado com sucesso")
                break
            else:
                print("Senha incorreta")
            if i == 4:
                print("Acabou suas tentativas tente novamente mais tarde")
    else:
        print("Email não encontrado")


def cadastrar(email, senha):
    index = True
    while index:
        #email = input("Digite seu email para cadastrar: ")
        if email in var.emails:
            return print("Esse email já foi cadastrado")
        elif any(type_email in email for type_email in var.types_email):
            index = False
        else:
            print("email invalido")
            pass
    #senha = input("Digite seu senha: ")
    var.emails[email] = senha
    print("Email adicionado com sucesso")



if __name__ == '__main__':
    logar('jonatas@gmail.com', 1234)
    cadastrar('pedro@yahoo.com', 4321)