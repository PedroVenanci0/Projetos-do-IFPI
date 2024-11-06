def main():

    print("===============================")
    print(">>> SEQUÊNCIA DE FIBONACCI <<<")
    print("===============================")
    
    numero_N = int(input('\nDigite o número de termos da sequência: '))
    

    while numero_N < 2:
        print('\nValor INVÁLIDO!! O número de termos deve ser maior ou igual a 2.')
        numero_N = int(input('\nDigite o número de termos da sequência: '))
        
    primeiro_termo = 0
    segundo_termo = 1
    
    fibonacci = [primeiro_termo, segundo_termo]
    
    for i in range(2, numero_N):
        proximo_termo = primeiro_termo + segundo_termo
        fibonacci.append(proximo_termo)
    
        primeiro_termo = segundo_termo
        segundo_termo = proximo_termo
    
    sequencia_fibonacci = ", ".join(map(str, fibonacci))
    
    print(f'\n>> Os {numero_N} primeiros termos da sequência de Fibonacci são: {sequencia_fibonacci}\n')
main()
