def main():
    numero_x, numero_y = map(int, input().split())
    while numero_x != numero_y:
        if numero_x > numero_y:
            print ('Decrescente')
        elif numero_x < numero_y:
            print ('Crescente')
        numero_x, numero_y = map(int, input().split())
main()