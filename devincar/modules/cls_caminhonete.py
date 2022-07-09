from .cls_veiculos import Veiculos
from ..utils.cls_validacoes import Validacoes

class Caminhonete(Veiculos):

    opt_combustivel = {
        1: "Gasolina",
        2: "Diesel",
    }
    
    cores_disponiveis = {
        '1': "roxo",
    }
    
    tipo_veiculo = 'Caminhonete'

    def __init__(self):
        super().__init__()
        self.tipo_veiculo = self.__class__.__name__
        self.qtd_portas: int = None
        self.combustivel: str = None
        self.capacidade_carregamento: float = None

    def cadastrar_veiculo(self, db):
        super().cadastrar_veiculo(db)
        self.qtd_portas = Validacoes.valida_inteiro("Digite a quantidade de portas do veiculo: ")
        self.escolher_combustivel()
        self.capacidade_carregamento = Validacoes().valida_float("Digite a capacidade de carregamento do veiculo: ")
        super().salvar_veiculo(db)
        
    def escolher_combustivel(self):
        for combustivel in self.opt_combustivel:
            print(f"{combustivel} - {self.opt_combustivel[combustivel]}")
        while True:
            opcao = int(input("Escolha a opção de combustivel para o veículo: "))
            if opcao in self.opt_combustivel.keys():
                self.combustivel = self.opt_combustivel[opcao]
                break
    
    def carregamento_inicial(self, numero_chassi, data_fabricacao, nome, placa, valor, cpf_comprador, cor, data_atual, potencia, qtd_portas, combustivel, capacidade_carregamento):
        tipo_veiculo = self.__class__.__name__
        super().carregamento_inicial(tipo_veiculo, numero_chassi, data_fabricacao, nome, placa, valor, cpf_comprador, cor, data_atual, potencia)
        self.qtd_portas = int(qtd_portas)
        self.combustivel = str(combustivel)
        self.capacidade_carregamento = str(capacidade_carregamento)
        