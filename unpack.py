def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

def summation(benjamins, ones):
    return (benjamins * 100) + ones

coins = [100, 22, 16]
dollars = {"ones": 3000, "benjamins": 450}

sum = total(*coins) # unpacking
print(sum, "Knuts")

totalDollar = summation(**dollars) # named arguments
print(f"{totalDollar} Dollars")