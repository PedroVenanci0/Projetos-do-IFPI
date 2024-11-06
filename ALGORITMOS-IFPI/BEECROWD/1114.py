def main():
    senha_digitada = int(input(''))
    senha_armazenada = 2002
    while senha_digitada != senha_armazenada:
        if senha_digitada != senha_armazenada:
            print ('Senha Invalida')
        senha_digitada = int(input(''))
    print ('Acesso Permitido')
main()