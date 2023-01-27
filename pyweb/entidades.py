class Cliente:
    def __init__(self, nome, email, cpf=None, cep=None, id=None, data_cadastro=None):
        self.nome = nome
        self.cpf = cpf
        self.cep = cep
        self.email = email
        self.id = id
        self.data_cadastro = data_cadastro


class Produto:
    def __init__(self, nome, categoria, preco, id=None):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.id = id
