import matplotlib.pyplot as plt

def srednia(elementy: list) -> float:
    return sum(elementy)/len(elementy)

def sczytywacz(path: str):
    l = []
    x = []
    y = []
    with open(path) as f:
        for element in f.read().split():
            l.append(int(element))
    for i in range(len(l)):
        if i % 2 == 0:
            x.append(l[i])
        else:
            y.append(l[i])
    return x, y


def odchylenie(zbior: list) -> float:
    ma = srednia(zbior)
    wynik = 0
    for element in zbior:
        wynik += (element - ma)**2
    return (wynik/(len(zbior) - 1))**(1/2)

def wspolczynnik_korelacji(zbior_x: list, zbior_y: list) -> float:
    suma_iloczynow = 0
    for i in range(len(zbior_x)):
        suma_iloczynow += zbior_x[i]*zbior_y[i]
    suma_x = sum(zbior_x)
    suma_y = sum(zbior_y)
    suma_x2 = sum([x**2 for x in zbior_x])
    suma_y2 = sum([x**2 for x in zbior_y])
    n = len(zbior_x)
    return (n * suma_iloczynow - suma_x * suma_y)/((n* suma_x2 - suma_x**2) * (n*suma_y2 - suma_y**2))**(1/2)

def wspolczynnik_b(zbior_x: list, zbior_y: list) -> float:
    return wspolczynnik_korelacji(zbior_x, zbior_y) * odchylenie(zbior_y)/odchylenie(zbior_x)

def wspolczynnik_a(zbior_x: list, zbior_y: list) -> float:
    return srednia(zbior_y) - wspolczynnik_b(zbior_x, zbior_y) * srednia(zbior_x)
    
def regresja(zbior_x: list, zbior_y: list) -> None:
    plt.plot(zbior_x, zbior_y, 'o')
    a = wspolczynnik_a(zbior_x, zbior_y)
    b = wspolczynnik_b(zbior_x, zbior_y)
    y = [b * x + a for x in zbior_x]
    print(y)
    plt.plot(zbior_x, y)
    plt.show()

def przewidywana_wartosc(x: int, zbior_x: list, zbior_y: list) -> float:
    return wspolczynnik_b(zbior_x, zbior_y) * x + wspolczynnik_a(zbior_x, zbior_y)

if __name__ == "__main__":
    zbior_x = sczytywacz("algorithms/tab.txt")[0]
    zbior_y = sczytywacz("algorithms/tab.txt")[1]
    regresja(zbior_x, zbior_y)
    print(f"przewidywana wartość = {przewidywana_wartosc(6, zbior_x, zbior_y)}")
