def main():
    
    dias_idade = int(input())
    
    anos = dias_idade // 365
    meses = (dias_idade % 365) // 30
    dias = (dias_idade % 365) % 30
    
    print (f'{anos} ano(s)')
    print (f'{meses} mes(es)')
    print (f'{dias} dia(s)')
        
main()