from os import system
from uuid import uuid4
from random import randint
from datetime import datetime
from utils import Validacoes

class Veiculos:
    cores_disponiveis = {
        '1': "Azul",
        '2': "Amarelo",
        '3': "Vermelho",
        '4': "Verde",
        '5': "Preto",
        '6': "Branco",
        '7': "roxo",
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
        self.potencia: int = None
        self.data_venda: str = None

    def carregamento_inicial(self, tipo_veiculo, numero_chassi, data_fabricacao, nome, 
                             placa, valor, cpf_comprador, cor, data_atual, potencia):
        self.tipo_veiculo = tipo_veiculo
        self.numero_chassi = str(numero_chassi)
        self.data_fabricacao = str(data_fabricacao)
        self.nome = str(nome)
        self.placa = str(placa)
        self.valor = float(valor)
        self.cpf_comprador = cpf_comprador
        self.cor = str(cor)
        self.data_atual = str(data_atual) 
        self.potencia = int(potencia)
        
    def cadastrar_veiculo(self, db):
        try:
            self.nome = Validacoes().valida_string("Digite o nome (modelo) do veiculo: ")
            self.data_fabricacao = Validacoes().valida_data()
            self.placa = Validacoes().valida_placa(db)
            self.valor = Validacoes().valida_float("Digite o valor do veiculo: ")
            self.potencia = Validacoes().valida_inteiro("Digite a potencia do veiculo: ")
            self.exibe_cores_disponiveis()
            self.cores_disponiveis = Validacoes().valida_cores_disponiveis(self.cores_disponiveis)     
            self.numero_chassi = self.gerador_chassi()
        except ValueError:
            print("Valor inválido")
    
    def alterar_veiculo(self, db, campo_alteracao):
        if campo_alteracao == 'cor':
            self.exibe_cores_disponiveis()
            self.cor = Validacoes().valida_cores_disponiveis(self.cores_disponiveis)
        elif campo_alteracao == 'valor':
            self.valor = Validacoes().valida_float("Digite o valor do veiculo: ")
        
        db.atualizar_veiculo(self)
    
    def vender_veiculo(self, db):
        self.cpf_comprador = Validacoes().valida_cpf()
        self.data_venda = datetime.now().strftime("%d/%m/%Y")
        db.vender_veiculo(self)
    
    def salvar_veiculo(self, db):
        db.salvar_veiculo(self)
        
    def listar_veiculos(self, db):
        db.listar_veiculos_por_tipo(self.__class__.__name__,)

    def exibe_cores_disponiveis(self):
        for cor in self.cores_disponiveis:
            print(f"{cor} - {self.cores_disponiveis[cor]}")    
  
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
        modelo = str(uuid4().fields[0])[:4].upper() #gera um modelo de veiculo aleatório
        ano_fabricacao = ano_fabricacao_chassi() 
        local_producao = 'D' #fabrica devincar
        sequencial = str(uuid4().fields[-1])[:6]
        chassi = str(f"{regiao}{pais_origem}{fabricante}{modelo}{ano_fabricacao}{local_producao}{sequencial}")
        
        return chassi
        
    

       
