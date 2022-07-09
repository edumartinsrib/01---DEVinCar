from .cls_veiculos import Veiculos
from utils import Validacoes

class Carro(Veiculos):
    opt_combustivel = {
        1: "Gasolina",
        2: "Flex",
    }
    tipo_veiculo = 'Carro'
    
    campos_relatorio = {
        'tipo_veiculo': 'Tipo veiculo',
        'numero_chassi': 'Número do chassi',
        'data_fabricacao': 'Data de fabricação',
        'nome': 'Nome',
        'placa': 'Placa',
        'valor': 'Valor',
        'cpf_comprador': 'CPF do comprador',
        'cor': 'Cor',
        'potencia': 'Potência',
        'qtd_portas': 'Quantidade de portas',
        'combustivel': 'Combustivel',
        'data_venda': 'Data de venda',
        'status': 'Status',
    }
    
    def __init__(self):
        super().__init__()
        self.tipo_veiculo = self.__class__.__name__
        self.combustivel: str = None
        self.qtd_portas: int = None

    def cadastrar_veiculo(self, db):
        try:
            super().cadastrar_veiculo(db)
            self.escolher_combustivel()
            self.qtd_portas = Validacoes.valida_inteiro("Digite a quantidade de portas do veiculo: ")
            super().salvar_veiculo(db)
            
        except ValueError:
            print("Valor inválido")
            
    def escolher_combustivel(self):
        for combustivel in self.opt_combustivel:
            print(f"{combustivel} - {self.opt_combustivel[combustivel]}")
            
        while True:
            opcao = int(input("Escolha a opção de combustivel para o veículo: "))
            if opcao in self.opt_combustivel.keys():
                self.combustivel = self.opt_combustivel[opcao]
                break
            
    def carregamento_inicial(self, numero_chassi, data_fabricacao, nome, placa, valor, cpf_comprador, cor, potencia, qtd_portas, combustivel, status):
          tipo_veiculo = self.__class__.__name__
          super().carregamento_inicial(tipo_veiculo=tipo_veiculo,numero_chassi=numero_chassi,data_fabricacao=data_fabricacao, 
                                       nome=nome,placa=placa,valor=valor,cpf_comprador=cpf_comprador,cor=cor,potencia=potencia,status=status)
          self.qtd_portas = int(qtd_portas)
          self.combustivel = str(combustivel)