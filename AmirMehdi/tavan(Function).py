def tavan(paye , andis):
    if andis == 0:
        return 1
    else:
        return paye * tavan(paye , andis - 1)

paye = int(input())
andis = int(input())
print(tavan(paye, andis))