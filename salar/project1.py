
def fact(number1):
    if number1 == 0 or number1 == 1:
        return 1
    return number1 * fact(number1 - 1)


def combination(number1 , number2):
    comb = fact(number1) // (fact(number2) * fact(number1 - number2))
    return comb


number1 = int (input())
number2 = int (input())
print(combination(number1 , number2))