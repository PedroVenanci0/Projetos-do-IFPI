import time

def escrever_texto(texto):
    delay = 0.09
    for elements in texto:
        print(elements, end='', flush=True)  # Exibe o caractere sem quebra de linha e força a exibição imediata
        time.sleep(delay)  # Atraso antes de exibir o próximo caractere
    print()  # Move o cursor para a próxima linha após o texto ser exibido

def main():
    texto = "algodao"
    escrever_texto(texto,delay=0.09)
main()

# flush 