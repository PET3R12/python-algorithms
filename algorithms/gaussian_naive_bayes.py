import math

def wczytaj_dane(path: str) -> dict:
    wartosci = []
    klasy = []
    with open(path, 'r') as f:
        for row in f.readlines():
            row = row.replace('\n', '').split(sep=',')
            klasy.append(row[-1])
            row = row[:-1]
            wartosci.append([float(element) for element in row])
    unikalne = []
    [unikalne.append(element) for element in klasy if element not in unikalne]
    s = {klucz: [] for klucz in unikalne}
    for key, value in s.items():
        for i in range(len(wartosci)):
            if klasy[i] == key:
                value.append(wartosci[i])
    return s, len(wartosci)

def bayes(train: dict, test: list):
    n = 0
    for k, v in train.items():
        n += len(v)
    prawdopodobienstwa = {}
    statystyki = {klucz: [] for klucz in train}
    for k, v in train.items():
        liczba_obiektow_klasy = len(v)
        prawdopodobienstwa[k] = liczba_obiektow_klasy/n
        for i in range(len(v[0])):
            kolumna = [wiersz[i] for wiersz in v]
            srednia = sum(kolumna)/len(kolumna)
            wariancja = sum((element - srednia)**2 for element in kolumna)/len(kolumna)
            statystyki[k].append((srednia, wariancja))

    predykcje = []
    for element in test:




    


        

if __name__ == "__main__":
    tab = wczytaj_dane("algorithms/iris.data")
    # [print(element) for element in tab]
    print(tab[0].values())