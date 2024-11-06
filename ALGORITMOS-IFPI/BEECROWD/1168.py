

def Caseleds(leds):

    match leds:

        case "0" | "9" | "6":
            return 6
        case "1":
            return 2
        case "2" | "5" | "3":
            return 5
        case "4":
            return 4
        case "7":
            return 3
        case "8":
            return 7 

def main():

    numero_de_paineis = int(input())

    for i in range(numero_de_paineis):

        numero_do_painel = input()
        somatorio_leds = 0

        for elements in numero_do_painel:

            qtd_leds = Caseleds(elements)
            somatorio_leds += qtd_leds
        
        print(f"{somatorio_leds} leds")

main()

# def number_lads(leds):

#     Lista_leds = {
#         "0":6, "1":2, "2":5, "3":5, "4":4, "5":5, "6":6, "7":3, "8":7, "9":6, 
#     }
#     return Lista_leds.get(leds)

# def main():

#     numero_paineis = int(input())

#     for i in range(numero_paineis):

#         leds = input()
#         somatorio_leds = 0

#         for elements in leds:

#             qtd_leds = number_lads(elements)
#             somatorio_leds += qtd_leds

#         print(f"{somatorio_leds} leds")
        
# main()