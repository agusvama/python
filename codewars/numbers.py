def iq_test(numbers):
    pares = list()
    impares = list()
    numbers = numbers.split(" ")
    for n in numbers:
        if int(n) % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    #print pares
    #print impares
    if len(pares) > len(impares):
        #print numbers.index(impares[0])
        return (numbers.index(impares[0])) + 1
    else:
        #print numbers.index(pares[0])
        return (numbers.index(pares[0])) + 1

if __name__ == "__main__":
    print iq_test("2 4 7 8 10")
    print iq_test("1 2 2")
    print iq_test("23 52 13 21 27 11 37 33 25 47 47 13")
