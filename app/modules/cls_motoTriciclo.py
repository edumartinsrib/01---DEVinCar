from cls_veiculos import Veiculos

class Moto(Veiculos):
     
        tipo_veiculo = 'Moto/Triciclo'
        
        def __init__(self):
             super().__init__()
             self.tipo_veiculo = self.__class__.__name__
             self.potencia: int = None
             self.qtd_rodas: int = None
            
        def cadastrar_veiculo(self):
               super().cadastrar_veiculo()
               self.potencia = int(input('Digite a potencia: '))
               self.qtd_rodas = int(input('Digite a quantidade de rodas: '))
               super().salvar_veiculo()
               print('Veiculo cadastrado com sucesso!')
        
        def carregamento_inicial(self, numero_chassi, data_fabricacao, nome, placa, valor, cpf_comprador, cor, data_atual, potencia, qtd_rodas):
          tipo_veiculo = self.__class__.__name__
          super().carregamento_inicial(tipo_veiculo, numero_chassi, data_fabricacao, nome, placa, valor, cpf_comprador, cor, data_atual)
          self.potencia = potencia
          self.qtd_rodas = qtd_rodas
       
               
        