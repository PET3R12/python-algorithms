from typing import Callable

import random

def wczytaj_zbior(path: str) -> list:
    o = []
    with open(path, 'r') as f:
        for linia in f.readlines():
            o.append([float(element) for element in linia.split()])
    return o

def podziel(tab: list, n: int) -> list:
    kopia = tab[:]
    n_folda = len(kopia)//n
    output = []
    for i in range(n):
        fold = []
        for j in range(n_folda):
            index = random.randrange(len(kopia))
            fold.append(kopia[index])
            kopia.pop(index)
        output.append(fold)
    return output

def kroswalidacja(tab: list, n: int, funkcja: Callable[[list, list], float]):
    podzbiory = podziel(tab, n)
    wyniki = []
    for i in range(n):
        test = podzbiory[i]
        train = podzbiory[:]
        train.pop(i)
        l = []
        for element in train:
            for wiersz in element:
                l.append(wiersz)
        train = l
        wyniki.append(funkcja(train, test))
    return sum(wyniki)/len(wyniki)

if __name__ == "__main__":
    l = wczytaj_zbior("algorithms/australian.csv")
    p = podziel(l, 6)
    # [print(element) for element in l]
    # [print(element, "\n") for element in p]
    # print(l)

