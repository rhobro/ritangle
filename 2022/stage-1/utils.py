import numpy as np

def round_sf(x, sf=3):
    return round(x, sf-int(np.floor(np.log10(abs(x))))-1)

def decode(ans, mult):
    return np.floor(round_sf(ans) * mult)

def submit(ans, key):
    print(f"Answer: {ans}")
    print(f"Code: {decode(ans, key)}")