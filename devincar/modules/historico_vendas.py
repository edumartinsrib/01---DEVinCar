from tinydb import TinyDB
from prettytable import PrettyTable
from pathlib import Path

class HistoricoVendas():
    caminho_banco = Path().cwd() / 'devincar/data'
    field_names = ['numero_chassi', 'Tipo', 'Nome/Modelo', 'Data de Fabricação', 'Placa', 'Valor', 'Cor', 'CPF do Comprador', 'Data de Venda']
    
    def __init__(self):
        self.historico_vendas = TinyDB(self.caminho_banco / 'historico_vendas.json')
        self.dados_vendas_locais = self.carrega_dados_vendas()
    
    def carrega_dados_vendas(self):
        self.dados_vendas_locais = []
        for venda in self.historico_vendas.all():
            self.dados_vendas_locais.append(venda)
        return self.dados_vendas_locais

    def adicionar_venda(self, veiculo):
        self.historico_vendas.insert(veiculo)
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
        maior_valor = 0
        for veiculo in self.dados_vendas_locais:
            if veiculo['valor'] > maior_valor:
                maior_valor = veiculo.valor
        if maior_valor == 0:
            return print('Nenhuma venda registrada')
        else:
            print(f'O veículo com maior valor de venda foi:')
            my_table = PrettyTable()
            my_table.field_names = self.field_names
            my_table.add_row([veiculo['numero_chassi'], veiculo['tipo_veiculo'], veiculo['nome'], 
                              veiculo['data_fabricacao'], veiculo['placa'], veiculo['valor'],
                              veiculo['cor'], veiculo['cpf_comprador'], veiculo['data_venda']])
            print(my_table)
                        
    def menor_valor_venda(self):
        menor_valor = 0
        for veiculo in self.dados_vendas_locais:
            if veiculo['valor'] > menor_valor:
                menor_valor = veiculo.valor
        if menor_valor == 0:
            return print('Nenhuma venda registrada')
        else:
            print(f'O veículo com maior valor de venda foi:')
            my_table = PrettyTable()
            my_table.field_names = self.field_names
            my_table.add_row([veiculo['numero_chassi'], veiculo['tipo_veiculo'], veiculo['nome'], 
                              veiculo['data_fabricacao'], veiculo['placa'], veiculo['valor'],
                              veiculo['cor'], veiculo['cpf_comprador'], veiculo['data_venda']])
            print(my_table)
        

    