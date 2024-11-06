def main():
    string = "A B C D E"

    NovaString = ''

    for elements in string:

        if ord(elements) == ord(" "):
            continue
        
        NovaString += "\n" + elements

    print(NovaString)
main()

def main():

    string = "A B C D E"
    NovaString = ''

    for elements in string:

        if ord(elements) != ord(" "):
            NovaString += elements

    print(NovaString)

main()