from tinydb import TinyDB, Query
from prettytable import PrettyTable

db = TinyDB('app/data/db.json')

class Database:
    def __init__(self):
        self.bd_veiculos = []
        self.historico_vendas_veiculos = []
        
    def salvar_veiculo(self, veiculo):
        db.insert(veiculo.__dict__)
        self.atualiza_lista_veiculos()
    
    def atualiza_lista_veiculos(self):
        self.bd_veiculos = db.all()
    
    ##listar todos os veiculos cadastrados em forma de menu
    def listar_todos_veiculos_menu(self):
        self.atualiza_lista_veiculos()
        my_table = PrettyTable()
        
        my_table.field_names = ['numero_chassi', 'Tipo', 'Nome/Modelo', 'Data de Fabricação', 'Placa', 'Valor']
        for veiculo in self.bd_veiculos:
            my_table.add_row([veiculo['numero_chassi'], veiculo['tipo_veiculo'], veiculo['nome'], veiculo['data_fabricacao'], veiculo['placa'], veiculo['valor']])
        print(my_table)
        
    @staticmethod
    def atualizar_veiculo( veiculo):
        db.update(veiculo.__dict__(), Query().numero_chassi == veiculo.numero_chassi)
    
    @staticmethod 
    def show_veiculo(numero_chassi):
        if db.get(Query().numero_chassi == numero_chassi) != None:
            veiculo = db.get(Query().numero_chassi == numero_chassi)
            return veiculo
        return 'Veiculo não encontrado'
    
    @staticmethod
    def exibir_todos_veiculos():
        return db.all()

