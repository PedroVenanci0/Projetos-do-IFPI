def main():

    preferencia_de_horario = int(input("Se deseja transformar o horário militar para o AM/PM, pressione '0', caso contrário, '1'.\n>> "))
    print("Ótimo!! Agora nos informe a hora desejada.\n")

    if preferencia_de_horario == 0:
        horario = list(map(int, input("Informe o horário a ser convertido. ex: (hh:mm:ss).\n>> ").split(":")))
        hora, minuto, segundo = horario

        if int(hora) < 23 and int(hora) >= 0 and int(minuto) < 60 and int(minuto) >= 0 and int(segundo) < 60 and int(segundo) >= 0:

            if hora > 12 and hora < 23:
                hora -= 12
                print(f"Seu horário inserido corresponde a: {hora}:{minuto}:{segundo} PM")
            elif hora == 12:
                print(f"Seu horário inserido corresponde a: {hora}:{minuto}:{segundo} PM")
            elif hora >= 0:
                print(f"Seu horário inserido corresponde a: {hora}:{minuto}:{segundo} AM")
        else:
                print("Valor Invalido")

    elif preferencia_de_horario == 1:

        horario = list(map(str, input("Informe o horário a ser convertido. ex: (hh:mm:ss pm/am).\n>> ").split(":")))
        hora, minuto, segundo, AmPm = horario

        if int(hora) < 23 and int(hora) >= 0 and int(minuto) < 60 and int(minuto) >= 0 and int(segundo) < 60 and int(segundo) >= 0:

            if "pm" in AmPm.lower() and int(hora) > 12:
                hora = int(hora) - 12
                print(f"Seu horário inserido corresponde a: {hora}:{minuto}:{segundo} {AmPm}")
                
            elif "am" in AmPm.lower():
                print(f"Seu horário inserido corresponde a: {hora}:{minuto}:{segundo} {AmPm}")

        else:
                print("Valor Invalido")
            
     
main()