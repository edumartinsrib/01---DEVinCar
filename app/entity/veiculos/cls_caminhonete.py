from .cls_veiculos import Veiculos

class Caminhonete(Veiculos): 
        
        opt_combustivel = ['gasolina', 'diesel']
        
        def __init__(self):
             super().__init__()
             self.potencia: int = None
             self.qtd_rodas: int = None
             self.combustivel: str = None
             self.capacidade_carregamento: int = None
        
        def cadastrar_veiculo(self, tipo_veiculo):
             super().cadastrar_veiculo(tipo_veiculo)
             self.potencia = int(input("Digite a potencia do veiculo: "))
             self.qtd_rodas = int(input("Digite a quantidade de rodas do veiculo: "))
             self.combustivel = input("Digite o tipo de combustivel do veiculo: ")
             self.capacidade_carregamento = int(input("Digite a capacidade de carregamento do veiculo: "))
             print('Veiculo cadastrado com sucesso!')
             