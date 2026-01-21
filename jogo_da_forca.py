import random


def escolher_linha_aleatoria(arquivo):
    linha_escolhida = None
    with open("words.txt", 'r') as f:
        for i, linha in enumerate(f, start=1):
            if random.randint(1, i) == 1:
                linha_escolhida = linha.strip()
    return linha_escolhida

try:
    with open("words.txt", "r") as arquivo:
        conteudo = arquivo.read()
        if conteudo:
            palavra = escolher_linha_aleatoria(arquivo)
        else:
            print("O arquivo words.txt está vazio")
            exit()
except FileNotFoundError:
    print("O arquivo words.txt não foi encontrado")
    exit()

    

print("Bem-vindo ao Jogo da Forca!\n\n")
incognita = ""
for letra in  palavra:
    incognita = incognita + '_'
tentativas = 6
letras_tentadas = ""
    
fim = False
while fim == False:
    print(f"Palavra: {incognita}\n\n")
    print(f"Tentativas restantes: {tentativas}\n")
    print(f"Letras tentadas: {letras_tentadas}\n\n")
    print("Digite uma letra: ")
    letra = input()
    if len(letra) != 1 or letra.isalpha() == False:
        print("Opcao invalida. Por favor digite novamente")
        continue
    if letras_tentadas == "":
        letras_tentadas = letras_tentadas + letra
    else:
        letras_tentadas = letras_tentadas + ", " + letra
    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                aux = i+1
                incognita = incognita[:i] + letra + incognita[aux:]
    else:
        tentativas = tentativas - 1
    
    if tentativas == 0:
        print(f"Fim de jogo! A palavra era: {palavra}")
        break
    if "_" in incognita:
        fim = False
    else:
        print(f"Parabéns! Você acertou a palavra: {palavra}")
        fim = True