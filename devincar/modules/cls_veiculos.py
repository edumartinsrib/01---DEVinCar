from os import system
from uuid import uuid4
from random import randint
from datetime import datetime
from .cls_validacoes import Validacoes
from .database import Database as db

class Veiculos:
    cores_disponiveis = {
        1: "Azul",
        2: "Amarelo",
        3: "Vermelho",
        4: "Verde",
        5: "Preto",
        6: "Branco",
        7: "roxo",
    }

    tipos_veiculos = {
        1: "Carro",
        2: "Moto",
        3: "Caminhonete",
    }

    def __init__(self):
        self.tipo_veiculo = None
        self.numero_chassi: str = None
        self.data_fabricacao: str = None
        self.nome: str = None
        self.placa: str = None
        self.valor: float = None
        self.cpf_comprador: str = 0
        self.cor: str = None
        self.data_atual: str = datetime.now().strftime("%d/%m/%Y")

    def carregamento_inicial(self, tipo_veiculo, numero_chassi, data_fabricacao, nome, placa, valor, cpf_comprador, cor, data_atual):
        self.tipo_veiculo = tipo_veiculo
        self.numero_chassi = numero_chassi
        self.data_fabricacao = data_fabricacao
        self.nome = nome
        self.placa = placa
        self.valor = valor
        self.cpf_comprador = cpf_comprador
        self.cor = cor
        self.data_atual = data_atual 
        
    def cadastrar_veiculo(self):
        self.nome = input("Digite o nome (modelo) do veiculo: ")
        self.data_fabricacao = input("Digite a data de fabricação do veiculo: ")
        self.placa = input("Digite a placa do veiculo: ")
        self.valor = float(input("Digite o valor do veiculo: "))
        while True:
            self.exibe_cores_disponiveis()
            cor_escolhida = int(input("Escolha a opção de cor disponível para o veiculo:  "))
            if cor_escolhida in self.cores_disponiveis:
                self.cor = self.cores_disponiveis[cor_escolhida]
                break
            else:
                print("Opção inválida")
        self.numero_chassi = self.gerador_chassi()
        
    def alterar_veiculo(self):
       pass

    ##vender veículo e informar CPF do comprador
    def vender_veiculo(self):
        pass

    def exibe_cores_disponiveis(self):
        for cor in self.cores_disponiveis:
            print(f"{cor} - {self.cores_disponiveis[cor]}")

    def listar_todos_veiculos(self):
        print(f"Listando todos os veiculos cadastrados".center(50, "-"))
        db.listar_todos_veiculos_menu()

    def salvar_veiculo(self):
        db.salvar_veiculo(self)
        
    def gerador_chassi(self):
        def ano_fabricacao_chassi(ano_inicial = 1980):
            ##captura caracteres de ano de fabricacao a partir do ano do veículo - a partir de 1980 até 2030
            caracteres_ano_fabricacao = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l',
                              'm', 'n', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                              '1', '2', '3', '4', '5', '6', '7', '8', '9']
            ano_fabricao_veiculo = int(self.data_fabricacao[6:10])
            
            index = ano_fabricao_veiculo - ano_inicial
            
            if index > len(caracteres_ano_fabricacao):
                index = index - len(caracteres_ano_fabricacao)
                
            return caracteres_ano_fabricacao[index]
        
        regiao = randint(8, 9) #América do Sul
        pais_origem = 'B' #Brasil
        fabricante = 'D' #devinCar
        modelo = str(uuid4().fields[0])[:4].upper #gera um modelo de veiculo aleatório
        ano_fabricacao = ano_fabricacao_chassi() 
        local_producao = 'D' #fabrica devincar
        sequencial = str(uuid4().fields[-1])[:6]
        chassi = f"{regiao}{pais_origem}{fabricante}{modelo}{ano_fabricacao}{local_producao}{sequencial}"
        
        return chassi
    
    

       
