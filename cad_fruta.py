import json
import os
from pathlib import Path

class Fruta:
    def __init__(self):
        self.nome_arquivo = "dadosfruta.json"
        arquivo = Path(self.nome_arquivo)
        if arquivo.exists():
            with open(self.nome_arquivo, "r") as arquivo:
                self.estoque = json.load(arquivo)
        else: 
            self.estoque = {}

    def cadastrar_fruta(self):
        print("+----")
        print("| cadastro de fruta ")
        print("|")
        nome_da_fruta = input("|Qual o nome da fruta: ")
        qual_unidade_de_venda = input("|Qual unidade de venda (kg, un): ")
        quantidade_da_fruta = float(input("|Qual a quantidade: "))
        qual_o_preco =  float(input("|Qual o valor de venda: "))
        self.adicionar_fruta(nome_da_fruta, qual_unidade_de_venda, quantidade_da_fruta, qual_o_preco)
        
    def adicionar_fruta(self, nome, unidade, quantidade, preco):
        if nome in self.estoque:
            self.estoque[nome]['quantidade'] += quantidade
        else:
            self.estoque[nome] = {'nome': nome, 'unidade': unidade, 'quantidade': quantidade, 'preco': preco}
        print(f"Adicionadas {quantidade} unidades de {nome} ao estoque.")
        self.gravaJson()

    def ver_estoque(self):
        print("\nEstoque de Frutas:")
        for fruta, info in self.estoque.items():
            print(f"{fruta}: {info['quantidade']} unidades a R${info['preco']:.2f} cada")
        t= input("precione a tecla entrer para sair:")

    def vender_fruta(self, nome, quantidade):
        if nome in self.estoque and self.estoque[nome]['quantidade'] >= quantidade:
            total = quantidade * self.estoque[nome]['preco']
            self.estoque[nome]['quantidade'] -= quantidade
            print(f"Vendeu {quantidade} unidades de {nome}. Total: R${total:.2f}")
        else:
            print(f"Não há estoque suficiente de {nome}.")

    def gravaJson(self):
        with open(self.nome_arquivo, "w") as arquivo:
            json.dump(self.estoque, arquivo, indent=4)        

    
