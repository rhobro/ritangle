from math import floor, log10

def round_sf(x, sf=3):
    return round(x, sf-int(floor(log10(abs(x))))-1)

def decode(ans, mult):
    return floor(round_sf(ans) * mult)

def submit(ans, key):
    print(f"Answer: {ans}")
    print(f"Code: {decode(ans, key)}")