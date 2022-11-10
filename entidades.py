class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def bom_dia(self):
        print(f'Bom dia, meu nome é: {self.nome}')


if __name__ == '__main__':
    maria = Cliente(1, "Maria")
    print(maria.id, maria.nome)
    maria.bom_dia()
