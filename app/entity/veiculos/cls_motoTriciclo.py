from .cls_veiculos import Veiculos

class Moto(Veiculos):
     
     
        def __init__(self):
             super().__init__()
             self.potencia: int = None
             self.qtd_rodas: int = None

        def cadastrar_veiculo(self, tipo_veiculo):
               super().cadastrar_veiculo(tipo_veiculo)
               self.potencia = int(input('Digite a potencia: '))
               self.qtd_rodas = int(input('Digite a quantidade de rodas: '))
               print('Veiculo cadastrado com sucesso!')
        
        def __str__(self):
             return f'{super().__str__()}\nPotencia: {self.potencia}\nQtd rodas: {self.qtd_rodas}'