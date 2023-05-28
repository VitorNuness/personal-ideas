from dataclasses import dataclass
from getpass import getpass
from hashlib import sha256

@dataclass
class Usuario:
    user: str
    senha: str