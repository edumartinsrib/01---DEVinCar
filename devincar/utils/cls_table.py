from rich.console import Console
from rich.table import Table


class Tables():
    @staticmethod
    def monta_tabela(titulo, campos, valores):
        my_table = Table(title=titulo, show_header=True, header_style="bold green")
        
        for campo in campos:
            my_table.add_column(str(campo))

        for valor in valores:
            my_table.add_row(*Tables.ajusta_valores(campos, valor.__dict__))
               
        console = Console()
        console.print(my_table)

    @staticmethod
    def ajusta_valores(campos, valores):
        dados = []
        
        for campo in campos:
            if campo in valores:
                
                dados.append(valores[campo])
            else:
                dados.append('-')
        print(dados)
        return tuple(valores)
        #valor_lista = zip*next([x for x in valores.values()])
        #return valor_lista 
        