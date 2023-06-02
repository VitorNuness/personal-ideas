from dataclasses import dataclass
from getpass import getpass
from hashlib import sha256
import os

@dataclass
class Usuario:
    usuario: str
    senha: str

def pedir_usuario():
    usuario = input("USUÁRIO: ").lower()
    return usuario

def pedir_senha():
    senha = getpass("SENHA: ")
    return senha


def verificar_arquivo():
    arquivo = open('usuarios.txt', 'r+') if os.path.exists('usuarios.txt') else []
    return arquivo

def verificar_usuario(usuario):
    arquivo = verificar_arquivo()
    if usuario in arquivo:
        return "Usuário já existe."
    else:
        return None

def cadastro():
    while True:
        usuario = pedir_usuario()
        senha = pedir_senha()
        verificar_usuario(usuario) 
        return "Cadastro realizado com sucesso."