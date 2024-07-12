import itertools

def comb(L):
    for i in itertools.permutations(L, 3):
        print(i)

comb([1, 2, 3])