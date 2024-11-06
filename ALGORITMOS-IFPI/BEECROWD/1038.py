def main():
    
    item_01,quantidade_item = map(int,input().split())
    
    preço_total = 0
    
    if item_01 == 1:
        preço_total += 4.00
    elif item_01 == 2:
        preço_total += 4.50
    elif item_01 == 3:
        preço_total += 5.00
    elif item_01 == 4:
        preço_total += 2.00
    elif item_01 == 5:
        preço_total += 1.50
        
    preço_total = preço_total * quantidade_item

    print(f'Total: R$ {preço_total:.2f}')
    
main()