from datetime import datetime
from re import match


class Validacoes():

    @staticmethod
    def valida_cpf():
        while True:
            cpf = input("Digite o CPF: ")

            if bool(match("^[0-9]{11}$", cpf)):
                return cpf
            else:
                print("CPF inválido")
                continue

    @staticmethod
    def valida_placa(db):
        while True:
            placa = input("Digite a placa - apenas números (padrão antigo e mercosul): ").upper()

            if db.verifica_existencia_veiculo('placa', placa) == True:
                print("\nPlaca já cadastrada!")
                continue

            if bool(match("^[A-Z]{3}[0-9]{4}$", placa)):
                return placa
            elif bool(match("^[A-Z]{3}[0-9][0-9A-Z][0-9]{2}$", placa)):
                return placa
            else:
                print("Placa inválida")
                continue

    # validadata
    @staticmethod
    def valida_data():
        while True:
            try:
                data = input("Digite a data (dd/mm/aaaa): ")
                data = datetime.strptime(data, "%d/%m/%Y")

                # não permitir data superior a data atual
                if data > datetime.now():
                    print("Data inválida")
                    continue
                else:
                    return data.strftime("%d/%m/%Y")

            except ValueError:
                print("Data inválida")

    @staticmethod
    def valida_inteiro(texto_input):
        while True:
            try:
                input_resultado = int(input(texto_input))
                if input_resultado <= 0:
                    print("O valor deve ser maior que zero")
                    continue
                return input_resultado
            except ValueError:
                print("Número inválido")
                continue

    @staticmethod
    def valida_float(texto_input):
        while True:
            try:
                input_resultado = float(input(texto_input))
                if input_resultado <= 0:
                    print("O valor deve ser maior que zero")
                    continue
                return input_resultado
            except ValueError:
                print("Número inválido")
                continue

    @staticmethod
    def valida_cores_disponiveis(array_cores):
        while True:
            try:
                input_resultado = input("Escolha a opção de cor disponível para o veiculo:  ")
                if input_resultado in array_cores:
                    return array_cores[input_resultado]
                else:
                    print("Opção inválida")
                    continue
            except ValueError:
                print("Opção inválida")
                continue

    @staticmethod
    def valida_string(texto_input):
        while True:
            try:
                input_resultado = str(input(texto_input))
                if input_resultado == "":
                    print("O campo não pode estar vazio")
                    continue
                return input_resultado
            except ValueError:
                print("Texto inválido")
                continue
