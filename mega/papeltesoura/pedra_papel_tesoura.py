import random


def jogar():
    opcoes = ["Pedra", "Papel", "Tesoura"]
    escolha = random.choice(opcoes)
    print("O computador escolheu:", escolha)


if __name__ == "__main__":
    jogar()