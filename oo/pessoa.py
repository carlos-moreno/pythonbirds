class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá, meu nome é  {self.nome}"

    @staticmethod
    def metodo_statico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f"{cls} - olhos {cls.olhos}"


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_classe_pai = super().cumprimentar()
        return f'{cumprimentar_classe_pai}. Aperto de mão'

if __name__ == "__main__":
    isabella = Pessoa(nome="Isabella")
    luiz = Homem(nome="Luíz")
    carlos = Homem(isabella, luiz, nome="Carlos", idade=30)
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
    print(luiz.olhos, luiz.olhos)
    carlos.olhos = 1
    print(carlos.olhos)
    print(carlos.metodo_statico(), Pessoa.metodo_statico())
    print(carlos.nome_e_atributos_de_classe(), Pessoa.nome_e_atributos_de_classe())
    print(carlos.cumprimentar())
    print(luiz.cumprimentar())
    print(isabella.cumprimentar())
