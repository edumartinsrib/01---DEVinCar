from tinydb import TinyDB, Query
from prettytable import PrettyTable

db = TinyDB('app/data/db.json')

class Database:
    def __init__(self):
        self.dados_local = []
        

    @staticmethod
    def salvar_veiculo(veiculo):
        db.insert(veiculo.__dict__)
    
    @staticmethod
    def alterar_veiculo(veiculo):
        db.update(veiculo.__dict__, Query().numero_chassi == veiculo.numero_chassi)
    
    @staticmethod
    def listar_todos_veiculos_menu():
        """listar todos os veiculos cadastrados em forma de menu"""
        my_table = PrettyTable()
        
        my_table.field_names = ['numero_chassi', 'Tipo', 'Nome/Modelo', 'Data de Fabricação', 'Placa', 'Valor']
        for veiculo in db.all():
            my_table.add_row([veiculo['numero_chassi'], veiculo['tipo_veiculo'], veiculo['nome'], veiculo['data_fabricacao'], veiculo['placa'], veiculo['valor']])
        print(my_table)
        
    @staticmethod
    def verifica_existencia_veiculo(key, valor):
        if db.contains(Query()[key] == valor) == True:
            return True
        return False
    
    @staticmethod
    def get_veiculo(key, valor):
        return db.get(Query()[key] == valor)
    
    ##atualizar apenas cpf do comprador
    @staticmethod
    def vender_veiculo(key, valor_filtro, valor):
        db.update({'cpf_comprador': valor}, Query()[key] == valor_filtro)
        print("Veículo vendido com sucesso")
        

