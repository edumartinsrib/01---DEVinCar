class Database:
    def __init__(self):
        self.bd_veiculos = []
        self.historico_vendas_veiculos = []
        
    def salvar_veiculo(self, veiculo):
        
        self.bd_veiculos.append(veiculo)
     
        
    def atualizar_veiculo(self, veiculo):
        for i in range(len(self.bd_veiculos)):
            if self.bd_veiculos[i].numero_chassi == veiculo.numero_chassi:
                self.bd_veiculos[i] = veiculo
                break
        
    def show_list_veiculos(self):
        print ('\nLista de veículos cadastrados:')
        ## imprimir todas classes dentro do array 
        for veiculo in self.bd_veiculos:
            print (veiculo.__dict__())
    