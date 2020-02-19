class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f"Olá {id(self)}"


if __name__ == "__main__":
    p = Pessoa('Carlos', 30)
    print(f'{p.nome} - {p.idade}')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
