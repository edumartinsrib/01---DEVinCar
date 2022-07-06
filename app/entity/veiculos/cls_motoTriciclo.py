from .cls_veiculos import Veiculos


class Moto(Veiculos):
     
        tipo_veiculo = 'Moto/Triciclo'
        
        def __init__(self):
             super().__init__()
             self.potencia: int = None
             self.qtd_rodas: int = None
            
        def cadastrar_veiculo(self):
               super().cadastrar_veiculo(Moto.tipo_veiculo)
               self.potencia = int(input('Digite a potencia: '))
               self.qtd_rodas = int(input('Digite a quantidade de rodas: '))
               super().salvar_veiculo()
               print('Veiculo cadastrado com sucesso!')

       
               
        