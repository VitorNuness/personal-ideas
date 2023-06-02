import unittest
from unittest.mock import patch
from bib import *

class TestPedirUsuario(unittest.TestCase):

    @patch('builtins.input', lambda _:"VITOR")
    def test_pedir_usuario(self):
        usuario = "vitor"
        self.assertEqual(pedir_usuario(), usuario)

class TestPedirSenha(unittest.TestCase):

    @patch('bib.getpass', lambda _:"123")
    def test_pedir_senha(self):
        senha = "123"
        self.assertEqual(pedir_senha(), senha)


class TestVerificarArquivo(unittest.TestCase):

    def test_verificar_arquivo_nao_existe(self):
        def setUp(self) -> None:
            try:
                os.remove("usuarios.txt")
            except:
                pass
        self.assertEqual(verificar_arquivo(), [])

    def test_verificar_arquivo_existe(self):
        arquivo = 'usuarios.txt'
        self.assertEqual(verificar_arquivo(), arquivo)

class TestCadastro(unittest.TestCase):

    @patch('bib.getpass', lambda *_:"123")
    def test_cadastro(self):
        input = {
            "vitor",
            "123"
        }
        with patch('builtins.input', lambda *_:"vitor"):
            self.assertEqual(cadastro(), "Cadastro realizado com sucesso.")
