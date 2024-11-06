import os
import json

def LimpaTela():
    os.system('cls' if os.name=='nt' else'clear')

from cad_fruta import Fruta 
frutinhas = Fruta()

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
    LimpaTela()
    print("+----------------------+")
    print("|      Menu            |")
    print("|                      |")
    print("|  1 - Cadastro        |")
    print("|  2 - Mostrar estoque |")
    print("| 10 - Sair            |")
    print("|                      |")
    print("+----------------------+")
    menu = input(" qual opção: ")
    if menu == "1":
        LimpaTela()
        frutinhas.cadastrar_fruta()
    elif menu == "2":
        LimpaTela()
        frutinhas.ver_estoque()    
    elif menu == "10":
        acessopermitido = False
    else:
        print("opção invalida")




