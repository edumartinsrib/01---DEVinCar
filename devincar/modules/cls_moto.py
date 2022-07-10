from .cls_veiculos import Veiculos
from utils import Validacoes

class MotoTriciclo(Veiculos):
     
        tipo_veiculo = 'MotoTriciclo'
        
        campos_relatorio = {
        'tipo_veiculo': 'Tipo veiculo',
        'numero_chassi': 'Número do chassi',
        'data_fabricacao': 'Data de fabricação',
        'nome': 'Nome',
        'placa': 'Placa',
        'valor': 'Valor',
        'cpf_comprador': 'CPF do comprador',
        'cor': 'Cor',
        'potencia': 'Potência*',
        'qtd_rodas': 'Qtd. rodas*',
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
        'qtd_rodas': 'Qtd. rodas*',
        'valor': 'Valor',
        'status': 'Status',
    }
        
        def __init__(self):
             super().__init__()
             self.tipo_veiculo = self.__class__.__name__
             self.qtd_rodas: int = None
            
        def cadastrar_veiculo(self, db):
               super().cadastrar_veiculo(db)
               self.qtd_rodas = Validacoes.valida_inteiro("Digite a quantidade de rodas do veiculo: ")
               super().salvar_veiculo(db)

        def carregamento_inicial(self, numero_chassi, data_fabricacao, nome, placa, valor, cpf_comprador, cor, potencia, qtd_rodas, status):
          tipo_veiculo = self.__class__.__name__
          super().carregamento_inicial(tipo_veiculo=tipo_veiculo,numero_chassi=numero_chassi,data_fabricacao=data_fabricacao,
                                       nome=nome, placa=placa, valor=valor, cpf_comprador=cpf_comprador, cor=cor, potencia=potencia, status=status)
          self.qtd_rodas = int(qtd_rodas)