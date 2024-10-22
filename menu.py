acessopemitido = False
usuario = "adm"
senha = "adm"

qusuario = input("Digite seu usuario: ")
qsenha = input("Digite sua senha: ")

if (senha == qsenha and usuario == qusuario):
    acessopermitido = True
else: 
    print("Acesso negado")

while acessopermitido:
    print("1 - cadastro")
    print("10 - sair")
    menu = input("qual opção: ")
    if menu == "1":
     if menu == "10":
        acessopermitido = False
    else:
        print("opção invalida")
