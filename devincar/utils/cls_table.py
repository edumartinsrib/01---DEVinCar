from modules import *
from rich.console import Console
from rich.table import Table


class Tables():
    @staticmethod
    def monta_tabela(valores, campos_relatorio):
        console = Console()
        my_table = Table(title='Relatório de Veículos', show_header=True, header_style="bold green")

        header, campos = (campos_relatorio.values(), campos_relatorio.keys())

        if valores == []:
            return console.print('[bold red] Nenhum veículo encontrado!')

        for info_header in header:
            my_table.add_column(str(info_header), justify='center')

        for valor in valores:
            my_table.add_row(*Tables.ajusta_valores(campos, valor))

        console.print(my_table)
        console.print(
            f'[bold green]Total de veículos: [bold white] {len(valores)} [bold green] | Total de valor: [bold white]R$ {Tables.calcula_valor_total(valores)}')

    @staticmethod
    def ajusta_valores(campos, valores):
        dados = []

        for campo in campos:
            if campo in valores:
                if campo == 'valor':
                    dados.append(f'[bold green]R$ {valores[str(campo)]}')
                elif campo == 'status':
                    if valores[campo] == 'disponivel':
                        dados.append(f'[bold blue]{valores[str(campo)]}')
                    elif valores[campo] == 'vendido':
                        dados.append(f'[bold red]{valores[str(campo)]}')
                else:
                    dados.append(str(valores[str(campo)]))
            else:
                dados.append('-')

        return tuple(dados)

    @staticmethod
    def calcula_valor_total(valores):
        valor_total = 0.0
        for valor in valores:
            valor_total += valor['valor']
        return str(valor_total)
