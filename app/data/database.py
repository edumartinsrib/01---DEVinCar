class Database:
    def __init__(self):
        self.bd_veiculos = []
        self.historico_veiculos = []
        
    def salvar_veiculo(self, veiculo):
        self.bd_veiculos.append(veiculo)
        self.historico_veiculos.append(veiculo)
    
    
##gerar bases automática de veiculos