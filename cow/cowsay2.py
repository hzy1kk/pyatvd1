import cowsay

def desenhar():
    
    mensagem = "Estudando Python com Cowsay!"

    desenho = cowsay.draw(mensagem, cow=cowsay.cow)
    print(desenho)

if __name__ == "__main__":
    desenhar()
