from tinydb import TinyDB
from prettytable import PrettyTable
from pathlib import Path

class HistoricoVendas():
    field_names = ['numero_chassi', 'Tipo', 'Nome/Modelo', 'Data de Fabricação', 'Placa', 'Valor', 'Cor', 'CPF do Comprador', 'Data de Venda']
    
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
        
    def listar_vendas(self):
        print('\nHistórico de vendas:')
        my_table = PrettyTable()
        
        my_table.field_names = ['numero_chassi', 'Tipo', 'Nome/Modelo', 'Data de Fabricação', 'Placa', 'Valor', 'Cor', 'CPF do Comprador', 'Data de Venda']
        for veiculo in self.dados_vendas_locais:
            my_table.add_row([veiculo['numero_chassi'], veiculo['tipo_veiculo'], veiculo['nome'], 
                              veiculo['data_fabricacao'], veiculo['placa'], veiculo['valor'],
                              veiculo['cor'], veiculo['cpf_comprador'], veiculo['data_venda']])
        print(my_table)
        
    def listar_vendas_por_tipo(self, tipo_veiculo):
        print('\nHistórico de vendas:')
        my_table = PrettyTable()
        
        my_table.field_names = self.field_names
        for veiculo in self.dados_vendas_locais:
            if veiculo['tipo_veiculo'] == tipo_veiculo:
                my_table.add_row([veiculo['numero_chassi'], veiculo['tipo_veiculo'], veiculo['nome'], 
                              veiculo['data_fabricacao'], veiculo['placa'], veiculo['valor'],
                              veiculo['cor'], veiculo['cpf_comprador'], veiculo['data_venda']])
        print(my_table)
        
    def maior_valor_venda (self):
        try:    
            veiculo_maior_valor = max(self.dados_vendas_locais, key=lambda x: x['valor'])
            print(f'O veículo com maior valor de venda foi:')
            my_table = PrettyTable()
            my_table.field_names = self.field_names
            my_table.add_row([veiculo_maior_valor['numero_chassi'], veiculo_maior_valor['tipo_veiculo'], veiculo_maior_valor['nome'], 
                              veiculo_maior_valor['data_fabricacao'], veiculo_maior_valor['placa'], veiculo_maior_valor['valor'],
                              veiculo_maior_valor['cor'], veiculo_maior_valor['cpf_comprador'], veiculo_maior_valor['data_venda']])
            print(my_table)
        except ValueError:
            print('Nenhuma venda registrada')
                        
    def menor_valor_venda(self):
        try:
            veiculo_menor_valor = min(self.dados_vendas_locais, key=lambda x: x['valor'])
            print(f'O veículo com maior valor de venda foi:')
            my_table = PrettyTable()
            my_table.field_names = self.field_names
            my_table.add_row([veiculo_menor_valor['numero_chassi'], veiculo_menor_valor['tipo_veiculo'], veiculo_menor_valor['nome'], 
                              veiculo_menor_valor['data_fabricacao'], veiculo_menor_valor['placa'], veiculo_menor_valor['valor'],
                              veiculo_menor_valor['cor'], veiculo_menor_valor['cpf_comprador'], veiculo_menor_valor['data_venda']])
            print(my_table)
            
        except ValueError:
            print('Nenhuma venda registrada')
        

    