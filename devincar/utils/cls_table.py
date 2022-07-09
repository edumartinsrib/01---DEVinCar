from rich.console import Console
from rich.table import Table


class Tables():
    @staticmethod
    def carrega_tabela(self, campos, valores):
        for campo in campos:
            self.cabeçalho.append(campo)

        for valor in valores:
            self.valores_tabela.append([valor.numero_chassi, valor.tipo_veiculo, valor.nome,
                                       valor.data_fabricacao, valor.placa, valor.valor, valor.status])
        return self.valores_tabela

    @staticmethod
    def monta_tabela(self):
        table = Table()
        self.adiciona_colunas(table)
        self.adiciona_linhas(table)
        
        console = Console()
        console.print(table)

    def adiciona_colunas(self, table):
        for coluna in self.cabeçalho:
            table.add_column(str(coluna))
        
        