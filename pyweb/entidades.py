class Cliente:
    def __init__(self, nome, email, cpf=None, cep=None):
        self.nome = nome
        self.cpf = cpf
        self.cep = cep
        self.email = email


class Produto:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
