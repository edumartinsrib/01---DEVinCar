from .cls_veiculos import Veiculos
from utils import Validacoes

class Caminhonete(Veiculos):

    opt_combustivel = {
        1: "Gasolina",
        2: "Diesel",
    }
    
    cores_disponiveis = {
        '1': "Roxo",
    }
    
    tipo_veiculo = 'Caminhonete'

    campos_relatorio = {
        'tipo_veiculo': 'Tipo veiculo',
        'numero_chassi': 'Número do chassi',
        'data_fabricacao': 'Data de fabricação',
        'nome': 'Nome',
        'placa': 'Placa',
        'cor': 'Cor',
        'potencia': 'Potência*',
        'qtd_portas': 'Quantidade de portas*',
        'capacidade_carregamento': 'Capacidade de carregamento*',
        'combustivel': 'Combustivel*',
        'valor': 'Valor',
        'cpf_comprador': 'CPF do comprador',
        'data_venda': 'Data de venda',
        'status': 'Status',
    }
    
    campos_relatorio_veiculo_disponivel = {
        'tipo_veiculo': 'Tipo veiculo',
        'numero_chassi': 'Número do chassi',
        'data_fabricacao': 'Data de fabricação',
        'nome': 'Nome',
        'placa': 'Placa',
        'cor': 'Cor',
        'potencia': 'Potência*',
        'qtd_portas': 'Quantidade de portas*',
        'capacidade_carregamento': 'Capacidade de carregamento*',
        'combustivel': 'Combustivel*',
        'valor': 'Valor',
        'status': 'Status',
    }
    
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
    
    def carregamento_inicial(self, numero_chassi, data_fabricacao, nome, placa, valor, cpf_comprador, cor, potencia, qtd_portas, combustivel, capacidade_carregamento, status):
        tipo_veiculo = self.__class__.__name__
        super().carregamento_inicial(tipo_veiculo=tipo_veiculo, numero_chassi=numero_chassi, data_fabricacao=data_fabricacao, 
                                     nome=nome, placa=placa,valor=valor,cpf_comprador=cpf_comprador,cor=cor,potencia=potencia,status=status)
        self.qtd_portas = int(qtd_portas)
        self.combustivel = str(combustivel)
        self.capacidade_carregamento = str(capacidade_carregamento)
        