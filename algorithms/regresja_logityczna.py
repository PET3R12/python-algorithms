import math

from cross_validation import kroswalidacja, wczytaj_zbior

def srednia(tab: list) -> list:
    srednie = []
    n = len(tab[0])
    for i in range(n):
        kolumna = []
        for element in tab:
            kolumna.append(element[i])
        srednie.append(sum(kolumna)/len(kolumna))
    return srednie

def odchylenie(tab: list) -> list:
    srednie = srednia(tab)
    odchylenia = []
    kolumny = []
    n_kol = len(tab[0])
    n_wierszy = len(tab)
    for i in range(n_kol):
        kolumna = []
        for element in tab:
            kolumna.append(element[i])
        kolumny.append(kolumna)
    for i in range(n_kol):
        suma = 0
        for element in kolumny[i]:
            suma += (element - srednie[i])**2
        odchylenie = (suma/(n_wierszy-1))**(1/2)
        odchylenia.append(odchylenie)
    return odchylenia

def skalowanie(tab: list, srednie: list, odchylenia: list) -> list:
    przeskalowane = []
    
    n_row = len(tab)
    n_col = len(tab[0])

    for i in range(n_row):
        row_p = []
        for j in range(n_col):
            x = tab[i][j]
            x_p = (x - srednie[j])/odchylenia[j]
            if j != n_col-1:
                row_p.append(x_p)
            else:
                row_p.append(x)
        przeskalowane.append(row_p)
    return przeskalowane

def regresja_logistyczna(train: list, test: list) -> float:
    n_cech = len(train[0]) - 1
    n_obiektow = len(train)
    wektor_wag = n_cech * [0.0]
    b = 0.0
    learning_rate = 0.01

    przeskalowane_train = skalowanie(train, srednia(train), odchylenie(train))

    for w in range(100):
        gradient_j = n_cech * [0.0]
        gradient_b = 0.0

        for wiersz in przeskalowane_train:
            z = b
            for i in range(n_cech):
                z += wektor_wag[i] * wiersz[i] 
            y_p = 1/(1+math.e**((-1) * z))
            error = y_p - wiersz[-1]
            for i in range(n_cech):
                gradient_j[i] += error * wiersz[i]
            gradient_b += error
        for i in range(n_cech):
            gradient_j[i] = gradient_j[i]/n_obiektow
        gradient_b = gradient_b / n_obiektow
        for i in range(len(wektor_wag)):
            wektor_wag[i] = wektor_wag[i] - learning_rate * gradient_j[i]
        b = b - learning_rate * gradient_b


    przeskalowane_test = skalowanie(test, srednia(train), odchylenie(train))
    poprawne_predykcje = 0
    for wiersz in przeskalowane_test:
        z = b
        for i in range(n_cech):
            z += wektor_wag[i] * wiersz[i] 
        y_p = 1/(1+math.e**((-1) * z))
        if y_p >= 0.5:
            predykcja = 1
        else:
            predykcja = 0
        
        if predykcja == wiersz[-1]:
            poprawne_predykcje += 1
    
    accuracy = poprawne_predykcje/len(przeskalowane_test)

    return accuracy



if __name__ == "__main__":
    tab = wczytaj_zbior("algorithms/australian.csv")
    # s = srednia(tab)
    # o = odchylenie(tab)
    # p = skalowanie(tab)
    # print(p[1][0])
    # print(o[0])
    # print(len(tab[0]))
    k = kroswalidacja(tab, 6, regresja_logistyczna)
    print(k)