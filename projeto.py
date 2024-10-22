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







class Fruta:
    def __init__(self):
        self.estoque = {}

    def cadastrar_fruta(self):
        nome_da_fruta = input("Qual o nome da fruta: ")
        qual_unidade_de_venda = input("Qual unidade de venda (kg, un): ")
        quantidade_da_fruta = input("Qual a quantidade: ")
        qual_o_preco = input("Qual o valor de venda: ")

    def adicionar_fruta(self, nome, unidade, quantidade, preco):
        if nome in self.estoque:
            self.estoque[nome]['quantidade'] += quantidade
        else:
            self.estoque[nome] = {'nome': nome, 'unidade': unidade, 'quantidade': quantidade, 'preco': preco}
        print(f"Adicionadas {quantidade} unidades de {nome} ao estoque.")

    def ver_estoque(self):
        print("\nEstoque de Frutas:")
        for fruta, info in self.estoque.items():
            print(f"{fruta}: {info['quantidade']} unidades a R${info['preco']:.2f} cada")

    def vender_fruta(self, nome, quantidade):
        if nome in self.estoque and self.estoque[nome]['quantidade'] >= quantidade:
            total = quantidade * self.estoque[nome]['preco']
            self.estoque[nome]['quantidade'] -= quantidade
            print(f"Vendeu {quantidade} unidades de {nome}. Total: R${total:.2f}")
        else:
            print(f"Não há estoque suficiente de {nome}.")
