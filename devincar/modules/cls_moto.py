from .cls_veiculos import Veiculos
from .cls_validacoes import Validacoes

class Moto(Veiculos):
     
        tipo_veiculo = 'Moto/Triciclo'
        
        def __init__(self):
             super().__init__()
             self.tipo_veiculo = self.__class__.__name__
             self.qtd_rodas: int = None
            
        def cadastrar_veiculo(self, db):
               super().cadastrar_veiculo(db)
               self.qtd_rodas = Validacoes.valida_inteiro("Digite a quantidade de rodas do veiculo: ")
               super().salvar_veiculo(db)

        
        def carregamento_inicial(self, numero_chassi, data_fabricacao, nome, placa, valor, cpf_comprador, cor, data_atual, potencia, qtd_rodas):
          tipo_veiculo = self.__class__.__name__
          super().carregamento_inicial(tipo_veiculo, numero_chassi, data_fabricacao, nome, placa, valor, cpf_comprador, cor, data_atual, potencia)
          self.qtd_rodas = int(qtd_rodas)