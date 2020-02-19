class Pessoa:
    def __init__(self, *filhos, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá {id(self)}"


if __name__ == "__main__":
    isabella = Pessoa(nome='Isabella')
    luiz = Pessoa(nome='Luíz')
    carlos = Pessoa(isabella, luiz, nome='Carlos', idade=30)
    print(f'{carlos.nome} - {carlos.idade}')
    print(id(carlos))
    for children in carlos.filhos:
        print(f'{id(children)}: {children.nome}')
