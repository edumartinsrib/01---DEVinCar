from modules import *
from tinydb import Query, TinyDB
from utils import Tables as PersonalTable

from .cls_historico_vendas import HistoricoVendas


class Database:
    def __init__(self):
        self.dados_externos = TinyDB('devincar/database/database.json')
        self.dados_local = []
        self.historico_vendas = HistoricoVendas()

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
                                                potencia=dado['potencia'],
                                                qtd_portas=dado['qtd_portas'],
                                                status=dado['status'],
                                                data_venda=dado['data_venda'],
                                                combustivel=dado['combustivel'])
                self.dados_local.append(novo_carro)

            elif dado['tipo_veiculo'] == 'MotoTriciclo':
                novo_moto = MotoTriciclo()
                novo_moto.carregamento_inicial(numero_chassi=dado['numero_chassi'],
                                               data_fabricacao=dado['data_fabricacao'],
                                               nome=dado['nome'],
                                               placa=dado['placa'],
                                               valor=dado['valor'],
                                               cpf_comprador=dado['cpf_comprador'],
                                               cor=dado['cor'],
                                               potencia=dado['potencia'],
                                               status=dado['status'],
                                               data_venda=dado['data_venda'],
                                               qtd_rodas=dado['qtd_rodas'])
                self.dados_local.append(novo_moto)
            elif dado['tipo_veiculo'] == 'Caminhonete':
                novo_caminhonete = Caminhonete()
                novo_caminhonete.carregamento_inicial(numero_chassi=dado['numero_chassi'],
                                                      data_fabricacao=dado['data_fabricacao'],
                                                      nome=dado['nome'],
                                                      placa=dado['placa'],
                                                      valor=dado['valor'],
                                                      cpf_comprador=dado['cpf_comprador'],
                                                      cor=dado['cor'],
                                                      potencia=dado['potencia'],
                                                      qtd_portas=dado['qtd_portas'],
                                                      combustivel=dado['combustivel'],
                                                      capacidade_carregamento=dado['capacidade_carregamento'],
                                                      data_venda=dado['data_venda'],
                                                      status=dado['status'])
                self.dados_local.append(novo_caminhonete)

    def retorna_dados_local(self):
        return self.dados_local

    def salvar_veiculo(self, veiculo):
        self.dados_local.append(veiculo)
        self.dados_externos.insert(veiculo.__dict__)

    def atualizar_veiculo(self, veiculo):
        try:
            for veiculo_salvo in self.dados_local:
                if veiculo_salvo.placa == veiculo.placa:
                    veiculo_salvo = veiculo
                    self.dados_externos.update(
                        veiculo.__dict__, Query().placa == veiculo.placa)
                    return True
        except Exception as e:
            print(e)
            return False

    def vender_veiculo(self, veiculo):
        for veiculo_salvo in self.dados_local:
            if veiculo_salvo.placa == veiculo.placa:
                veiculo_salvo = veiculo
                self.dados_externos.update({'cpf_comprador': veiculo.cpf_comprador, 'status': veiculo.status,
                                           'data_venda': veiculo.data_venda}, Query()['placa'] == veiculo.placa)
                self.historico_vendas.adicionar_venda(veiculo)

    def listar_veiculos(self, valor_index, valor_filtro, tipo_veiculo, campos_relatorio):
        valores_relatorio = []

        for veiculo in self.dados_local:
            if valor_filtro == 'Todos':
                valores_relatorio.append(veiculo.__dict__)
            elif getattr(veiculo, valor_index) == valor_filtro and tipo_veiculo == 'Todos':
                valores_relatorio.append(veiculo.__dict__)
            elif getattr(veiculo, valor_index) == valor_filtro and getattr(veiculo, 'tipo_veiculo') == tipo_veiculo:
                valores_relatorio.append(veiculo.__dict__)

        PersonalTable().monta_tabela(valores=valores_relatorio,
                                     campos_relatorio=campos_relatorio)

    def verifica_existencia_veiculo(self, key, valor):
        if self.dados_externos.contains(Query()[key] == valor) == True:
            return True
        return False

    def verifica_existencia_veiculo_por_placa(self, placa):
        for veiculo in self.dados_local:
            if veiculo.placa == placa:
                return True
        return False

    def verifica_disponibilidade_veiculo(self, placa):
        for veiculo in self.dados_local:
            if veiculo.placa == placa and veiculo.cpf_comprador == 0:
                return True
        return False

    def get_veiculo(self, placa_veiculo):
        for veiculo in self.dados_local:
            if veiculo.placa == placa_veiculo:
                return veiculo
        return None
