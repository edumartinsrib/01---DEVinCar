from tinydb import TinyDB
from utils import Tables as PersonalTable

class HistoricoVendas():
     
    def __init__(self):
        self.historico_vendas = TinyDB('devincar/database/historico_vendas.json')
        self.dados_vendas_locais = self.carrega_dados_vendas()
    
    def carrega_dados_vendas(self):
        self.dados_vendas_locais = []
        for venda in self.historico_vendas.all():
            self.dados_vendas_locais.append(venda)
        return self.dados_vendas_locais

    def adicionar_venda(self, veiculo):
        self.historico_vendas.insert(veiculo.__dict__)
        self.dados_vendas_locais.append(veiculo.__dict__)
           
    def listar_vendas_por_valor(self, valor_index, campos_relatorio):
        try:
            if self.dados_vendas_locais != []:
                if valor_index == 'maior':
                    valores_relatorio = [max(self.dados_vendas_locais, key=lambda x: x['valor'])]
                elif valor_index == 'menor':
                    valores_relatorio = [min(self.dados_vendas_locais, key=lambda x: x['valor'])]
            else:
                valores_relatorio = []
                
            PersonalTable().monta_tabela(valores=valores_relatorio, campos_relatorio=campos_relatorio)
        except Exception as e:
            print(e)

            
            

    