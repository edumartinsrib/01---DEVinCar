import re

class Validacoes():
    
    @staticmethod
    def valida_cpf():
      while True:
        cpf = input("Digite o CPF: ")
    
        if re.match("[0-9]{11}" , cpf):
            return cpf
        else:
            print("CPF inválido")
            continue
        
    @staticmethod
    def valida_placa():
      while True:
        placa = input("Digite a placa (padrão novo e mercosul): ")
        
        if re.match("[A-Z]{3}[0-9]{4}" , placa):
            return placa
        elif re.match("[A-Z]{3}[0-9][0-9A-Z][0-9]{2}" , placa):
            return placa
        else:
            print("Placa inválida")
            continue

