import calculator

options = {
    1: calculator.getSum
}


def menu():
    selection = int(input("seleziona operazione:\n"
                          "1 - somma\n"))
    n1 = int(input("primo numero"))
    n2 = int(input("secondo numero"))
    return options[selection](n1, n2)


while True:
    res = menu()
    print(res)
