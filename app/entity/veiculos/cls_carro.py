from .cls_veiculos import Veiculos
 
class Carro(Veiculos):
        def __init__(self):
             super().__init__()
             self.combustivel: str = None
             self.qtd_portas: int = None
             self.potencia: int = None
        
        def cadastrar_veiculo(self, tipo_veiculo):
               super().cadastrar_veiculo(tipo_veiculo)
               self.combustivel = input('Digite o tipo de combustivel: ')
               self.potencia = input('Digite a potencia: ')
               self.qtd_portas = input('Digite a quantidade de portas: ')
               print('Veiculo cadastrado com sucesso!')