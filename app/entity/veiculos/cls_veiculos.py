from uuid import uuid4
from datetime import datetime
from data.database import Database as db
from entity.menu.menu_principal import Menu_Principal as menu


class Veiculos:
    cores_disponiveis = {
        1: "Azul",
        2: "Amarelo",
        3: "Vermelho",
        4: "Verde",
        5: "Preto",
        6: "Branco",
        7: "roxo",
    }

    tipos_veiculos = {
        1: "Carro",
        2: "Moto",
        3: "Caminhonete",
    }

    def __init__(self):
        self.tipo_veiculo = None
        self.numero_chassi: str = uuid4().fields[-1].to_bytes(8, "big").hex()
        self.data_fabricacao: str = None
        self.nome: str = None
        self.placa: str = None
        self.valor: float = None
        self.cpf_comprador: str = 0
        self.cor: str = None
        self.data_atual: str = datetime.now().strftime("%d/%m/%Y")

    def cadastrar_veiculo(self, tipo_veiculo):
        print(f"Cadastrando {tipo_veiculo}")
        self.tipo_veiculo = tipo_veiculo
        self.nome = input("Digite o nome (modelo) do veiculo: ")
        self.placa = input("Digite a placa do veiculo: ")
        self.valor = float(input("Digite o valor do veiculo: "))
        while True:
            self.exibe_cores_disponiveis(tipo_veiculo)
            if tipo_veiculo == "Caminhonete":
                self.cor = "Roxa"
                break

            cor_escolhida = int(input("Digite a cor para o veiculo: "))
            if cor_escolhida in self.cores_disponiveis:
                self.cor = self.cores_disponiveis[cor_escolhida]
                break
            else:
                print("Opção inválida")

        self.data_fabricacao = input("Digite a data de fabricação do veiculo: ")

    def alterar_veiculo(self):
        while True:
            print("Escolha o veículo para edição a partir do: ")
            menu().get_menu(menu.menu_edicao_veiculo)
            opcao = input("Digite a opção desejada: ")
            if opcao in menu.menu_edicao_veiculo:
                sub_opcao = input(
                    f"Digite o {menu.menu_edicao_veiculo[opcao]} para pesquisa: "
                )
                veiculo = db.get_veiculo(
                    menu.menu_edicao_veiculo[opcao], sub_opcao
                )
                if veiculo:
                    while True:
                        print(veiculo)
                        novo_valor = input(
                            f"Digite o novo valor para o {veiculo['tipo_veiculo']}: "
                        )
                        try:
                            novo_valor = float(novo_valor)
                            veiculo.valor = novo_valor
                            break
                        except ValueError:
                            print("Valor inválido")
                        
                        if veiculo.tipo_veiculo != "Caminhonete":
                            self.exibe_cores_disponiveis(veiculo.tipo_veiculo) 
                            cor_escolhida = int(input("Digite a cor para o veiculo: "))
                            if cor_escolhida in self.cores_disponiveis:
                                veiculo.cor = self.cores_disponiveis[cor_escolhida]
                                break
                        

                print("Veículo não encontrado")

            else:
                print("Opção inválida")

    ##vender veículo e informar CPF do comprador
    def vender_veiculo(self):
        while True:
            print("Escolha o veículo para venda a partir do: ")
            menu().get_menu(menu.menu_edicao_veiculo)
            opcao = input("Digite a opção desejada: ")
            if opcao in menu.menu_edicao_veiculo:
                sub_opcao = input(
                    f"Digite o {menu.menu_edicao_veiculo[opcao]} para pesquisa: "
                )
                if db.verifica_existencia_veiculo(
                    menu.menu_edicao_veiculo[opcao], sub_opcao
                ):
                    cpf_comprador = input("Digite o CPF do comprador: ")
                    db.vender_veiculo(
                        menu.menu_edicao_veiculo[opcao], sub_opcao, cpf_comprador
                    )
                else:
                    print("Veículo não encontrado")

            else:
                print("Opção inválida")

    def exibe_cores_disponiveis(self, tipo_veiculo):
        if tipo_veiculo == "Caminhonete":
            return "Este veiculo está disponível apenas na cor Roxa"
        print([f"{key} - {value}" for key, value in self.cores_disponiveis.items()])
        """ for cor in self.cores_disponiveis:
            print(f"{cor} - {self.cores_disponiveis[cor]}") """

    def listar_todos_veiculos(self):
        print(f"Listando todos os veiculos cadastrados".center(50, "-"))
        db.listar_todos_veiculos_menu()

    def salvar_veiculo(self):
        db.salvar_veiculo(self)
