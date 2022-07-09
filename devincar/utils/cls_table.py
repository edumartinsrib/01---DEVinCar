from rich.console import Console
from rich.table import Table
from modules import *

class Tables():
    @staticmethod
    def monta_tabela(valores, campos_relatorio):
        my_table = Table(title='Relatório de Veículos', show_header=True, header_style="bold green")
        
        header, campos = (campos_relatorio.values(), campos_relatorio.keys())

        for info_header in header:
            my_table.add_column(str(info_header))
            
        for valor in valores:
            my_table.add_row(*Tables.ajusta_valores(campos, valor))
               
        console = Console()
        console.print(my_table)

    @staticmethod
    def ajusta_valores(campos, valores):
        dados = []
        
        for campo in campos:
            
            if campo in valores:
                dados.append(str(valores[campo]))
            else:
                dados.append('-')

        return tuple(dados)
        
