from dataclasses import dataclass
from getpass import getpass
from hashlib import sha256

@dataclass
class Usuario:
    user: str
    senha: str

def menu():
    opcoes = [1,2,0]
    while True:
        try:
            print("MENU\n1 - Entrar\n2 - Cadastrar\n0 - Sair")
            selecao = int(input("Opção: "))
            if selecao in opcoes:
                if selecao == 0:
                    print("Até mais.")
                    return None
                else:
                    return selecao
            else:
                print("Opção inválida.")
        except ValueError:
            print("Opção inválida.")