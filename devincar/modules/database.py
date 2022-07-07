from tinydb import TinyDB, Query
from prettytable import PrettyTable
from pathlib import Path
from .cls_veiculos import *
from .cls_caminhonete import *
from .cls_carro import *
from .cls_moto import *




class Database:
    caminho_banco = Path().cwd() / 'devincar/data'
    
    def __init__(self):
        self.dados_externos = TinyDB(self.caminho_banco / 'database.json')
        self._historico_vendas = TinyDB(self.caminho_banco / 'historico_vendas.json')
        self.dados_local = []
    
    def carrega_classes_inicial(self):
        for dado in self.dados_externos.all():
            if dado['tipo_veiculo'] == 'Carro':
                novo_carro = Carro()
                novo_carro.carregamento_inicial(numero_chassi=dado['numero_chassi'],
                                                           data_fabricacao=dado['data_fabricacao'],
                                                           nome=dado['nome'],
                                                           placa=dado['placa'],
                                                           valor=dado['valor'],
                                                           cpf_comprador=dado['cpf_comprador'],
                                                           cor=dado['cor'],
                                                           data_atual=dado['data_atual'],
                                                           potencia=dado['potencia'],
                                                           qtd_portas=dado['qtd_portas'],
                                                           combustivel=dado['combustivel'])
                self.dados_local.append(novo_carro)
            elif dado['tipo_veiculo'] == 'Moto':
                novo_moto = Moto()
                novo_moto.carregamento_inicial(numero_chassi = dado['numero_chassi'],
                                                           data_fabricacao=dado['data_fabricacao'],
                                                           nome=dado['nome'],
                                                           placa=dado['placa'],
                                                           valor=dado['valor'],
                                                           cpf_comprador=dado['cpf_comprador'],
                                                           cor=dado['cor'],
                                                           data_atual=dado['data_atual'],
                                                           potencia=dado['potencia'],
                                                           qtd_rodas=dado['qtd_rodas'])
                self.dados_local.append(novo_moto)
            elif dado['tipo_veiculo'] == 'Caminhonete':
                novo_caminhonete = Caminhonete()
                novo_caminhonete.carregamento_inicial(numero_chassi = dado['numero_chassi'],
                                                           data_fabricacao=dado['data_fabricacao'],
                                                           nome=dado['nome'],
                                                           placa=dado['placa'],
                                                           valor=dado['valor'],
                                                           cpf_comprador=dado['cpf_comprador'],
                                                           cor=dado['cor'],
                                                           data_atual=dado['data_atual'],
                                                           potencia=dado['potencia'],
                                                           qtd_portas=dado['qtd_portas'],
                                                           combustivel=dado['combustivel'],
                                                           capacidade_carregamento=dado['capacidade_carregamento'])
                self.dados_local.append(novo_caminhonete)
    
    def retorna_dados_local(self):
        return self.dados_local
    
    def salvar_veiculo(self, veiculo):
        self.dados_local.insert(veiculo)
        self.dados_externos.insert(veiculo.__dict__)
    
    def alterar_veiculo(self, veiculo):
        try:
            for veiculo_salvo in self.dados_local:
                if veiculo_salvo['placa'] == veiculo.placa:
                    veiculo_salvo = veiculo
                    self.dados_externos.update(veiculo.__dict__, Query().placa == veiculo.placa)
                    print("Veículo alterado com sucesso")
                    return True
        except Exception as e:
            print(e)
            return False
            
    def listar_todos_veiculos_menu(self):
        my_table = PrettyTable()
        
        my_table.field_names = ['numero_chassi', 'Tipo', 'Nome/Modelo', 'Data de Fabricação', 'Placa', 'Valor']
        for veiculo in self.dados_local:
            my_table.add_row([veiculo.numero_chassi, veiculo.tipo_veiculo, veiculo.nome, veiculo.data_fabricacao, veiculo.placa, veiculo.valor])
        print(my_table)
        
    def verifica_existencia_veiculo(self, key, valor):
        if self.dados_externos.contains(Query()[key] == valor) == True:
            return True
        return False

    def get_veiculo(self, key, valor):
        return self.dados_externos.get(Query()[key] == valor)

    def vender_veiculo(self, key, valor_filtro, valor):
        self.dados_externos.update({'cpf_comprador': valor}, Query()[key] == valor_filtro)
        print("Veículo vendido com sucesso")
        
