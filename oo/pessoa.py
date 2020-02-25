class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá {id(self)}"


if __name__ == "__main__":
    isabella = Pessoa(nome="Isabella")
    luiz = Pessoa(nome="Luíz")
    carlos = Pessoa(isabella, luiz, nome="Carlos", idade=30)
    print(f"{carlos.nome} - {carlos.idade}")
    print(id(carlos))
    for children in carlos.filhos:
        print(f"{id(children)}: {children.nome}")

    carlos.sobrenome = "Moreno"
    print(carlos.sobrenome)
    print(carlos.__dict__)
    print(isabella.__dict__)
    print(luiz.__dict__)
    del carlos.sobrenome
    print(carlos.__dict__)
    print(Pessoa.olhos)
    print(luiz.olhos)
    print(isabella.olhos)
    carlos.olhos = 1
    print(carlos.olhos)
